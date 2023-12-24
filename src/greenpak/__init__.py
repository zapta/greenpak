# A library to manage and program GreenPAK devices using a I2CDriver or I2CDriver Mini adapters.

# Docs
# https://www.renesas.com/us/en/document/mat/system-programming-guide-slg468246?r=1572991
# https://www.renesas.com/us/en/document/mat/slg47004-system-programming-guide?r=1572991

from i2c_adapter import I2cAdapter
from enum import Enum
from typing import Optional, List, Tuple, Set
from dataclasses import dataclass
import time
import re

# TODO: Fix the 255 count limit issue.
# TODO: Examine transactions with the logic analyzer and make sure we don't make extra operation such as reads.
# TODO: Handle and verify device ids.
# TODO: Add prevention of bricking or locking.
# TODO: Add high level operation such as setting the I2C address.
# TODO: Convert the print messages to log messages.
# TODO: Add a more graceful handling of errors.
# TODO: Add a file with the main() of the command line tool.
# TODO: Find a cleaner way to handle the errata.


@dataclass(frozen=True)
class DeviceInfo:
    """Descriptor of a GreenPak device."""

    name: str
    ro_nvm_pages: List[int]
    erase_mask: int

    def assert_valid(self):
        """Assert that the product passes sanity check."""
        assert isinstance(self.name, str)
        assert len(self.name) > 0
        assert issubclass(self.ro_nvm_pages, list)
        assert len(set(self.ro_nvm_pages)) == len(self.ro_nvm_pages), "Duplicate pages"
        for page_id in self.ro_nvm_pages:
            assert isinstance(self.page_id, int)
            assert 0 <= page_id <= 15
        assert isinstance(self.erase_mask, int)
        assert 0 <= self.erase_mask <= 255
        assert (self.erase_mask & 0b00011111) == 0


_SUPPORTED_DEVICES = dict(
    [
        (d.name, d)
        for d in [
            DeviceInfo("SLG46824", [15], 0b10000000),
            DeviceInfo("SLG46826", [15], 0b10000000),
            DeviceInfo("SLG46827", [15], 0b10000000),
            DeviceInfo("SLG47004", [8, 15], 0b11000000),
        ]
    ]
)


class _MemorySpace(Enum):
    """The three memory spaces of GreenPAKS."""

    REGISTER = 1
    NVM = 2
    EEPROM = 3


def read_bits_file(file_name: str) -> bytearray:
    """Read an auto generated bit file and return as an array of 256 bytes"""
    result = bytearray()
    f = open(file_name, "r")
    first_line = True
    bits_read = 0
    byte_value = 0
    for line in f:
        line = line.rstrip()
        if first_line:
            assert re.match(r"index\s+value\s+comment", line)
            first_line = False
            continue
        assert bits_read < 2048
        m = re.match(r"^([0-9]+)\s+([0|1])\s.*", line)
        assert m
        bit_index = int(m.group(1))
        bit_value = int(m.group(2))
        assert bit_index == bits_read
        assert bit_value in (0, 1)
        # Least signiificant bit first
        byte_value = (byte_value >> 1) + (bit_value << 7)
        assert 0 <= byte_value <= 255
        bits_read += 1
        # Handle last bit of a byte
        if (bits_read % 8) == 0:
            result.append(byte_value)
            byte_value = 0
    assert bits_read == 2048
    assert len(result) == 256
    return result


def write_bits_file(file_name: str, data: bytearray) -> None:
    """Write a 256 bytes GP configuration as a bits file."""
    assert len(data) == 256
    with open(file_name, "w") as f:
        f.write("index\t\tvalue\t\tcomment\n")
        for i in range(len(data) * 8):
            byte_value = data[i // 8]
            # Lease significant bit first.
            bit_value = (byte_value >> (i % 8)) & 0x01
            f.write(f"{i}\t\t{bit_value}\t\t//\n")


def hex_dump(data: bytearray, start_addr: int = 0) -> None:
    """Dump a block of bytes in hex format."""
    end_addr = start_addr + len(data)
    row_addr = (start_addr // 16) * 16
    while row_addr < end_addr:
        items = []
        for i in range(16):
            addr = row_addr + i
            col_space = " " if i % 4 == 0 else ""
            if addr >= end_addr:
                break
            if addr < start_addr:
                items.append(f"{col_space}  ")
            else:
                items.append(f"{col_space}{data[addr - start_addr]:02x}")
        print(f"{row_addr:02x}: {" ".join(items)}", flush=True)
        row_addr += 16


class GreenpakDriver:
    """Each instance controls an I2C bus with one or more GreenPAK devices."""

    def __init__(self, port: str, device: str, control_code):
        """Initialize using a I2CDrivcer serial port and GreenPAK device control code.."""
        self.__i2c: I2cAdapter = I2cAdapter(port)
        self.set_device(device)
        self.set_control_code(control_code)

    def set_control_code(self, control_code: int) -> None:
        """Set the GreenPAK device control code to use. Should be in [0, 15]"""
        assert isinstance(control_code, int)
        assert 0 <= control_code <= 15
        self.__control_code = control_code

    def get_control_code(self) -> int:
        """Get the current GreenPAK device control code in use."""
        return self.__control_code

    def set_device(self, device: str) -> None:
        """Set device type. device string should be one of the supported devices."""
        assert isinstance(device, str)
        self.__device_info = _SUPPORTED_DEVICES[device]

    def get_device(self) -> str:
        """Return current device."""
        return self.__device_info.name

    def __i2c_device_addr(
        self, memory_space: _MemorySpace, control_code: int = None
    ) -> int:
        """Constructs the I2C device address for the given memory space."""
        assert memory_space in (
            _MemorySpace.REGISTER,
            _MemorySpace.NVM,
            _MemorySpace.EEPROM,
        )
        if control_code is None:
            control_code = self.__control_code
        assert 0 <= control_code << 15
        memory_space_table = {
            _MemorySpace.REGISTER: 0b000,
            _MemorySpace.NVM: 0b010,
            _MemorySpace.EEPROM: 0b011,
        }
        device_i2c_addr = control_code << 3 | memory_space_table[memory_space]
        assert 0 <= device_i2c_addr <= 127
        return device_i2c_addr

    def __read_bytes(
        self, memory_space: _MemorySpace, start_address: int, n: int
    ) -> bytearray:
        """An internal method to read a arbitrary block of bytes from a device's memory space."""
        # Sanity checks
        assert memory_space in (
            _MemorySpace.REGISTER,
            _MemorySpace.NVM,
            _MemorySpace.EEPROM,
        )
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # Construct the i2c address.
        device_i2c_addr = self.__i2c_device_addr(memory_space)

        # Write the start address to read.
        ok = self.__i2c.i2c_write(device_i2c_addr, bytearray([start_address]))
        assert ok
        resp_bytes = self.__i2c.i2c_read(device_i2c_addr, n)

        assert resp_bytes is not None
        assert n == len(resp_bytes)
        return resp_bytes

    def read_register_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's REGISTER memory space."""
        return self.__read_bytes(_MemorySpace.REGISTER, start_address, n)

    def read_nvm_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's NVM memory space."""
        return self.__read_bytes(_MemorySpace.NVM, start_address, n)

    def read_eeprom_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's EEPROM memory space."""
        return self.__read_bytes(_MemorySpace.EEPROM, start_address, n)

    def is_page_writeable(self, memory_space: MemoryError, page_id: int) -> bool:
        """Returns true if the page is writable by the user."""
        assert memory_space in (
            _MemorySpace.REGISTER,
            _MemorySpace.NVM,
            _MemorySpace.EEPROM,
        )
        assert 0 <= page_id <= 15
        is_read_only = (memory_space == _MemorySpace.NVM) and (
            page_id in self.__device_info.ro_nvm_pages
        )
        return not is_read_only

    def __write_bytes(
        self, memory_space: _MemorySpace, start_address: int, data: bytearray
    ) -> None:
        """An low level method to write a block of bytes to a device memory space.
        For NVM and EEPROM spaces, the block must exactly one page, the
        page must be erased, and user must wait for the operation to complete.
        """
        assert memory_space in (
            _MemorySpace.REGISTER,
            _MemorySpace.NVM,
            _MemorySpace.EEPROM,
        )
        n = len(data)
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # For NVM and EEPROM it must be exactly one page.
        if memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM):
            assert start_address % 16 == 0
            assert n == 16

        # Construct the device i2c address
        device_i2c_addr = self.__i2c_device_addr(memory_space)

        # We write the start address followed by the data bytes
        payload = bytearray()
        payload.append(start_address)
        payload.extend(data)

        # Write the data
        ok = self.__i2c.i2c_write(device_i2c_addr, bytearray(payload))
        assert ok
        # assert ack
        # ack = self.__i2c.write(bytearray(payload))
        # assert ack
        # self.__i2c.stop()

    def __read_page(self, memory_space: _MemorySpace, page_id: int) -> bool:
        """Read a 16 bytes page of a NVM or EEPROM memory spaces."""
        assert memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM)
        assert 0 <= page_id <= 15
        device_i2c_addr = self.__i2c_device_addr(memory_space)
        data = self.__read_bytes(memory_space, page_id << 4, 16)
        assert len(data) == 16
        return data

    def __erase_page(self, memory_space: _MemorySpace, page_id: int) -> None:
        """Erase a 16 bytes page of NVM or EEPROM spaces to all zeros. Page must be writable"""
        assert memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM)
        assert self.is_page_writeable(memory_space, page_id)

        # Erase only if not already erased.
        if self.__is_page_erased(memory_space, page_id):
            print(f"Page {memory_space.name}/{page_id:02d} already erased.", flush=True)
            return

        # Erase.
        print(f"Erasing page {memory_space.name}/{page_id:02d}.", flush=True)
        # We erase by writing to the register ERSR byte, and waiting.
        space_mask = {_MemorySpace.NVM: 0x00, _MemorySpace.EEPROM: 0x10}[memory_space]
        erase_mask = self.__device_info.erase_mask | space_mask | page_id
        # TODO: Find a cleaner solution for the errata's workaround.
        self.write_register_bytes(0xE3, bytearray([erase_mask]))
        # Allow the operation to complete. Datasheet says 20ms max.
        time.sleep(0.025)

        # Errata woraround. Perform a dummy write to clear the error from the previous write.
        # This is a workaround for the erase issue describe in the errata at:
        # https://www.renesas.com/us/en/document/dve/slg46824-errata?language=en
        device_i2c_addr = self.__i2c_device_addr(_MemorySpace.REGISTER)
        self.__i2c.i2c_write(device_i2c_addr, bytearray([0]), silent=True)

        # device_i2c_addr = self.__i2c_device_addr(_MemorySpace.REGISTER)
        # self.__i2c_device_addr()
        # assert self.__i2c.i2c_reset()

        # Verify that the page is all zeros.
        assert self.__is_page_erased(memory_space, page_id)

    def __is_page_erased(self, memory_space: _MemorySpace, page_id: int) -> bool:
        """Returns true if all 16 bytes of given MVM or EEPROM page are zero.
        Page must be writable..
        """
        assert memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM)
        assert self.is_page_writeable(memory_space, page_id)

        data = self.__read_page(memory_space, page_id)
        return all(val == 0 for val in data)

    def __program_page(
        self, memory_space: _MemorySpace, page_id: int, page_data: bytearray
    ) -> None:
        """Program a NVM or EEPROM 16 bytes page. Page must be writeable."""
        assert memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM)
        assert self.is_page_writeable(memory_space, page_id)
        assert len(page_data) == 16

        # Do nothing if the page already has the desired value.
        old_data = self.__read_page(memory_space, page_id)
        if old_data == page_data:
            print(f"Page {memory_space.name}/{page_id:02d} no change.", flush=True)
            return

        # Erase the page to all zeros.
        self.__erase_page(memory_space, page_id)

        # Write the new page data.
        print(f"Writing page {memory_space.name}/{page_id:02d}.", flush=True)
        self.__write_bytes(memory_space, page_id << 4, page_data)
        # Allow the operation to complete. Datasheet says 20ms max.
        time.sleep(0.025)

        # Read and verify the page's content.
        actual_page_data = self.__read_page(memory_space, page_id)
        assert actual_page_data == page_data

    def __program_pages(
        self, memory_space: _MemorySpace, start_page_id: int, pages_data: bytearray
    ) -> None:
        """Program one or mage 16 bytes pages of the NVM or EEPROM spaces."""
        assert memory_space in (_MemorySpace.NVM, _MemorySpace.EEPROM)
        assert 0 <= start_page_id <= 15
        assert 1 < len(pages_data)
        assert (len(pages_data) % 16) == 0
        assert (start_page_id << 4) + len(pages_data) <= 256

        num_pages = len(pages_data) // 16
        assert 0 < num_pages
        assert start_page_id + num_pages <= 16
        for i in range(0, num_pages):
            if not self.is_page_writeable(memory_space, i):
                print(
                    f"Page {memory_space.name}/{i} a read only page, skipping.",
                    flush=True,
                )
            else:
                page_data = pages_data[i << 4 : (i + 1) << 4]
                self.__program_page(memory_space, start_page_id + i, page_data)

    def write_register_bytes(self, start_address: int, data: bytearray) -> None:
        """Write a block of bytes to device's Register (RAM) space."""
        self.__write_bytes(_MemorySpace.REGISTER, start_address, data)

    def program_nvm_pages(self, start_page_id: int, pages_data: bytearray) -> None:
        """Program one or mage 16 bytes pages of the NVM space."""
        self.__program_pages(_MemorySpace.NVM, start_page_id, pages_data)

    def program_eeprom_pages(self, start_page_id: int, pages_data: bytearray) -> None:
        """Program one or mage 16 bytes pages of the EEPROM space."""
        self.__program_pages(_MemorySpace.EEPROM, start_page_id, pages_data)

    def reset_device(self) -> None:
        """Reset the device, loading the NVM to the REGISTER"""
        # Set register bit 1601 to reset the device.
        self.write_register_bytes(0xC8, bytearray([0x02]))
        # Allow the operation to complete.
        # TODO: Check with the datasheet what time period to use here.
        time.sleep(0.1)

    def scan_device(self, control_code: int) -> bool:
        """Test if a device exists at given control_code."""
        assert 0 <= control_code <= 15
        device_i2c_addr = self.__i2c_device_addr(_MemorySpace.REGISTER, control_code)
        ok = self.__i2c.i2c_write(device_i2c_addr, bytearray([0]), silent=True)
        return ok

    def scan_devices(self):
        """Find control_codes with responding devices."""
        result = []
        for control_code in range(16):
            if self.scan_device(control_code):
                result.append(control_code)
        return result
