"""Utilities to handles GreenPak configurations."""


from dataclasses import dataclass
import re
from importlib import resources as impresources
from intelhex import IntelHex


def read_hex_config_file(file_name: str) -> bytes:
    """Load GreenPak configuration from a hex file.

    :param file_name: Path to the input intelhex file. The file is expected to
       have exactly 256 byte values for the address range [0, 255].
    :type file_name: str

    :returns: The 256 configuration bytes.
    :rtype: bytearray.
    """
    ih = IntelHex()
    ih.loadhex(file_name)
    ih_dict = ih.todict()
    assert len(ih_dict) == 256
    result = bytearray()
    for addr in range(256):
        val = ih_dict[addr]
        assert isinstance(val, int)
        assert 0 <= val <= 255
        result.append(val)
    return result


def write_hex_config_file(file_name: str, data: bytearray | bytes) -> bytes:
    """Read GreenPak config from a hex file.

    :param file_name: Path to the output intelhex file.
    :type file_name: str

    :param data: The config bytes to write. Should have exactly 256 bytes.
    :type data: bytearray or bytes

    :returns: None
    """
    assert isinstance(file_name, str)
    assert isinstance(data, (bytearray, bytes))
    assert len(data) == 256
    ih = IntelHex()
    ih.frombytes(data)
    ih.write_hex_file(file_name)


def read_bits_config_file(file_path: str) -> bytearray:
    """Read a GreenPak SPLD config file.

    Reads the config file, converts to configuration bytes, and asserts that there were no errors.
    Config files are text files with the values of the GreenPak configuration bits. These are the
    output files of the Renesas GreenPAK Designer.

    :param file_path: Path to the file to read.
    :type file_path: str

    :returns: The configuration bits as a bytearray of 256 bytes, in the same representation as the GreenPak's NVM memory.
    :rtype: bytearray
    """
    result = bytearray()
    f = open(file_path, "r")
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


def write_bits_config_file(file_name: str, data: bytearray | bytes) -> None:
    """Write a GreenPak SPLD config file.

    Writes the given configuration bytes, in the same representation as the GreenPak NVM memory,
    as a GreenPak config file. Config files are text files with the values of the GreenPak
    configuration bits. These are th output files of the Renesas GreenPAK Designer.

    :param file_path: Path to the output file.
    :type file_path: str

    :param data: The configuration bytes to write. ``len(data)`` is asserted to be 256.
    :type data: bytearray or bytes
    """
    assert isinstance(data, (bytearray, bytes))
    assert len(data) == 256
    with open(file_name, "w") as f:
        f.write("index\t\tvalue\t\tcomment\n")
        for i in range(len(data) * 8):
            byte_value = data[i // 8]
            # Bit order in file is least significant bit first.
            bit_value = (byte_value >> (i % 8)) & 0x01
            f.write(f"{i}\t\t{bit_value}\t\t//\n")


def hex_dump(data: bytearray | bytes, start_addr: int = 0) -> None:
    """Print bytes in hex format.

    This utility help function is useful to print binary data such
    as GreenPak configuration bytes.

    :param data: The bytes to dump.
    :type data: bytearray or bytes

    :param start_addr: Allows to assign an index other than zero to the first byte.
    :type start_addr: int

    ."""
    assert isinstance(data, (bytearray, bytes)), type(data)
    assert isinstance(start_addr, int)
    assert start_addr >= 0
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
        print(f'{row_addr:02x}: {" ".join(items)}', flush=True)
        row_addr += 16
