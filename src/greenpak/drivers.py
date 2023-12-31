# I2C driver wrappers for various I2C boards.


from i2c_adapter import I2cAdapter
from typing import override


class GreenPakI2cDriver:
    """GreenPak compatible I2C driver."""

    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        """Write the given bytes to the I2C device with address.
        addr: i2c device address in the range [0, 127]
        data: a bytearray with 0 to 256 bytes to write.
        silent: if True, do not print diagnostic information in case of a write failure.
        Returns True if OK, False if an error.
        """
        assert False, f"Class {self.__class__} does not implement write()"

    def read(
        self, addr: int, byte_countcount: int, silent: bool = False
    ) -> bytearray | None:
        """Read the given number of bytes from the I2C device with given address.
        addr: i2c device address in the range [0, 127]
        byte_count: number of bytes to read in the range [0, 256]
        silent: if True, do not print diagnostic information in case of a read failure.
        Returns a bytearray of len count with the bytes read or None if an error.
        """
        assert False, f"Class {self.__class__} does not implement write()"


class GreenPakI2cAdaper(GreenPakI2cDriver):
    """A greenpak I2C driver using an I2C Adapter board."""

    def __init__(self, port):
        self.__i2c: I2cAdapter = I2cAdapter(port)

    @override
    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        return self.__i2c.write(addr, data, silent=silent)

    @override
    def read(self, addr: int, byte_count: int, silent: bool = False) -> bool:
        return self.__i2c.read(addr, byte_count, silent=silent)
