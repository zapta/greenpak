"""I2C drivers for the ``greenpak`` package."""

from i2c_adapter import I2cAdapter
from i2cdriver import I2CDriver
from typing_extensions import override


class GreenPakI2cInterface:
    """A base class for GreenPak compatible I2C driver implementations."""

    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        """Write the given bytes to the I2C device with address.

        :param addr: I2C device address in the range [0, 127]
        :type addr: int

        :param data: The data to write. A bytearray with 0 to 256 bytes.
            If ``data`` is empty, the implementation should still perform the write operation
            but with zero bytes. This is used for I2C scanning.
        :type data: int

        :param silent: If True, do not print diagnostic information in case of a write failure.
        :type silent: bool

        :returns: True if OK, False if an error.
        :rtype: bool
        """
        assert False, f"Class {self.__class__} does not implement write()"

    def read(
        self, addr: int, byte_count: int, silent: bool = False
    ) -> bytearray | None:
        """Read the given number of bytes from the I2C device with given address.

        :param addr: I2C device address in the range [0, 127]
        :type addr: int

        :param byte_count: The number of bytes to read. Should be in the range [0, 256]. If
            byte_count is zero, the implementation should still perform the read operation
            but with zero bytes. This is used for I2C scanning.
        :type byte_count: int

        :param silent: If True, do not print diagnostic information in case of a read failure.
        :type silent: bool

        :returns: The bytes read or None if an error.
        :rtype: bytearray
        """
        assert False, f"Class {self.__class__} does not implement read()"


class GreenPakI2cAdapter(GreenPakI2cInterface):
    """A GreenPakI2cInterface implementation for I2C Adapter boards."""

    def __init__(self, port):
        self.__i2c: I2cAdapter = I2cAdapter(port)

    @override
    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        return self.__i2c.write(addr, data, silent=silent)

    @override
    def read(self, addr: int, byte_count: int, silent: bool = False) -> bytearray:
        return self.__i2c.read(addr, byte_count, silent=silent)


class GreenPakI2cDriver(GreenPakI2cInterface):
    """A GreenPakI2cInterface implementation for I2C Adapter boards."""

    def __init__(self, port):
        self.__i2c: I2CDriver = I2CDriver(port, reset=True)

    @override
    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        ok1 = self.__i2c.start(addr, 0)
        ok2 = self.__i2c.write(data)
        self.__i2c.stop()
        return ok1 and ok2

    @override
    def read(
        self, addr: int, byte_count: int, silent: bool = False
    ) -> bytearray | None:
        ack = self.__i2c.start(addr, 1)
        if ack:
            data = self.__i2c.read(byte_count)
        self.__i2c.stop()
        return data if ack else None


class GreenPakSMBusAdapter(GreenPakI2cInterface):
    """An adpater to the Linux 'native' SMBus interface"""
    import smbus2
    from smbus2 import smbus2

    def __init__(self, i2cbusdev="/dev/i2c-0"):
        self.bus = self.smbus2.SMBus(i2cbusdev)
        self.isopen = True

    def __del__(self):
        if self.isopen:
            self.bus.close()

    def __empty_wr(self, addr: int):
        #The purpose of this is to probe for a slave at address, in a non-destuctive
        #way. With SMBus layer, we could use write_quick(), provided implementation
        #doesn't do/send anything beyond:
        #
        # " .... When using write_quick, the slave address is sent along with the read/write bit. 
        #        No additional data is transmitted. The read/write bit can be used to convey some 
        #        simple information. For instance, you might use the read/write bit to signal a 
        #        '1' or '0' to the device .... "
        #  (More details see for e.g.: https://www.nxp.com/docs/en/application-note/AN4471.pdf)
        #
        #The SMBus2 Linux/Python library provides interface for quick write only.
        #(A properly working 'quick' command should properly stop (send stop bit) transaction
        # after n/ack  received, not leaving in some unfinished state).
        self.bus.write_quick(addr)  #Can/will throw If no device at address

    def __empty_rd(self, addr: int):
        #A 'quick read' is not provided by SMBus layer because it is not universaly safe (e.g. as
        #I tested, SLG would hold the bus hostage until its reset.)[ google more for info ].
        #For an SLG, whichever memory block -reg,nvm,eeprom - we addressing, a read without
        #first setting the data pointer should be safe, as it will return data from last
        #address set through a previous read/write reqest. We discard the result.
        self.bus._set_address(addr, None)
        msg = self.smbus2.i2c_msg.read(address=addr, length=1)
        self.bus.i2c_rdwr(msg)

    @override
    def write(self, addr: int, data: bytearray, silent: bool = False) -> bool:
        try:
            if 0 == len(data):
                #special case as we not actually writing/sending data.
                #(assume caller probing for GP devs on bus).
                self.__empty_wr(addr)  #Can throw
            else:
                #assume data is sent/written
                self.bus.write_i2c_block_data(addr, data[0], data[1:])
        except Exception as e:
            if not silent:
                str = "SMBus: while writing to addr 0x%02x: caught exception: %s" % (addr, e)
                print(str)
            return False
        return True

    @override
    def read(
        self, addr: int, byte_count: int, silent: bool = False
    ) -> bytearray | None:
        try:
            if 0 == byte_count:
                #assume caller probing for GP devs on bus
                self.__empty_rd(addr)  #Can/will throw if no dev found.
                return bytearray()
            else:
                offset = 0
                data = []
                while byte_count > 0:
                    xferlen = min(self.smbus2.I2C_SMBUS_BLOCK_MAX, byte_count)
                    data.extend(self.bus.read_i2c_block_data(addr, offset, xferlen))
                    offset += xferlen
                    byte_count -= xferlen
                return bytearray(data)
        except Exception as e:
            if not silent:
                str = "SMBus: while reading at addr 0x%02x: caught exception: %s" % (addr, e)
                print(str)
        return None
