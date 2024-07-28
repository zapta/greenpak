"""I2C drivers for the ``greenpak`` package."""

from typing_extensions import override
from typing_extensions import deprecated


class GreenPakI2cInterface:
    """A base class for GreenPak compatible I2C driver implementations."""

    def gp_write(self, i2c_addr: int, start: int, data: bytearray) -> bool:
        """New interface method: gp_write()

        :param i2c_addr: I2C device address in the range [0, 127]
        :type addr: int

        :param start: SLG memory/register start address for the write, range [0,256]
        :type start: int

        :returns: True if write succeeds
        :rtype: bool
        """

        assert False, f"Class {self.__class__} does not implement gp_write()"

    def gp_read(self, i2c_addr: int, start: int, byte_count: int) -> bytearray | None:
        """New interface method: gp_read()

        :param i2c_addr: I2C device address in the range [0, 127]
        :type addr: int

        :param start: SLG memory/register start address for the write, range [0,256]
        :type start: int

        :returns:  bytearray if the op went OK, None if an error happened.
        :rtype: bytearray
        """

        assert False, f"Class {self.__class__} does not implement gp_read()"


class GreenPakI2cAdapter(GreenPakI2cInterface):
    """A GreenPakI2cInterface implementation for I2C Adapter boards."""

    def __init__(self, port):
        from i2c_adapter import I2cAdapter

        print(f"Creating an i2c {type(self).__name__} driver.")
        self.__i2c: I2cAdapter = I2cAdapter(port)

    @override
    def gp_read(self, i2c_addr: int, start: int, byte_count: int) -> bytearray | None:
        # print(
        #     f"{self.__class__}.gp_read(): Addr: {i2c_addr:07b}, Start: 0x{start:02x}, count: {byte_count}"
        # )
        data = None
        # Write the reading start address.
        ok = self.__i2c.write(i2c_addr, bytearray([start]))
        if ok:
            data = self.__i2c.read(i2c_addr, byte_count)
            ok = data is not None
        return data if ok else None

    @override
    def gp_write(self, i2c_addr: int, start: int, data: bytearray) -> bool:
        # print(
        #     f"{self.__class__}.gp_write(): Addr: {i2c_addr:07b}, Start: 0x{start:02x}, count: {len(data)}"
        # )

        payload = bytearray()
        payload.append(start)
        payload.extend(data)
        # Setting silent=True since it's normal to have errors when erasing, per the errata.
        ok = self.__i2c.write(i2c_addr, payload, silent=True)
        # Clear errors in case we just wrote to 0xe3, per the errata.
        self.__i2c.write(i2c_addr, bytearray([]), silent=True)
        return ok


class GreenPakI2cDriver(GreenPakI2cInterface):
    """A GreenPakI2cInterface implementation for I2C Adapter boards."""

    def __init__(self, port, pullups=True):
        from i2cdriver import I2CDriver

        print(f"Creating an i2c {type(self).__name__}  driver.")
        self.__i2c: I2CDriver = I2CDriver(port, reset=True)
        # Per https://i2cdriver.com/i2cdriver.pdf
        # 4.7K on SCL/SDA if pullups is True, else, no pullups.
        self.__i2c.setpullups(0b100100 if pullups else 0b000000)

    @override
    def gp_read(self, i2c_addr: int, start: int, byte_count: int) -> bytearray | None:
        data = None
        # Start i2c write transaction.
        ok = self.__i2c.start(i2c_addr, 0)
        if ok:
            # Write start address to read.
            ok = self.__i2c.write(bytearray([start]))  #
        if ok:
            # Start i2c read transaction.
            ok = self.__i2c.start(i2c_addr, 1)
        if ok:
            # Read bytes.
            data = self.__i2c.read(byte_count)
        # Stop the i2c transaction.
        self.__i2c.stop()
        return data if ok else None

    @override
    def gp_write(self, i2c_addr: int, start: int, data: bytearray) -> bool:
        # Start i2c write transaction.
        ok = self.__i2c.start(i2c_addr, 0)
        if ok:
            # Write start address to write.
            ok = self.__i2c.write(bytearray([start]))  #
        if ok and len(data) > 0:
            ok = self.__i2c.write(data)
        # Stop the i2c transaction.
        self.__i2c.stop()
        return ok


class GreenPakSMBusAdapter(GreenPakI2cInterface):
    """An adpater to the Linux 'native' SMBus interface"""

    import smbus2
    from smbus2 import smbus2

    def __init__(self, i2cbusdev="/dev/i2c-0", traces=False):
        print(f"Creating an i2c {type(self).__name__} driver.")
        self.bus = self.smbus2.SMBus(i2cbusdev)
        self.isopen = True
        self.trace_errors = traces

    def __del__(self):
        if self.isopen:
            self.bus.close()

    def __empty_wr(self, addr: int):
        # The purpose of this is to probe for a slave at address, in a non-destuctive
        # way. With SMBus layer, we could use write_quick(), provided implementation
        # doesn't do/send anything beyond:
        #
        # " .... When using write_quick, the slave address is sent along with the read/write bit.
        #        No additional data is transmitted. The read/write bit can be used to convey some
        #        simple information. For instance, you might use the read/write bit to signal a
        #        '1' or '0' to the device .... "
        #  (More details see for e.g.: https://www.nxp.com/docs/en/application-note/AN4471.pdf)
        #
        # The SMBus2 Linux/Python library provides interface for quick write only.
        # (A properly working 'quick' command should properly stop (send stop bit) transaction
        # after n/ack  received, not leaving in some unfinished state).
        self.bus.write_quick(addr)  # Can/will throw If no device at address

    def __empty_rd(self, addr: int):
        # A 'quick read' is not provided by SMBus layer because it is not universaly safe (e.g. as
        # I tested, SLG would hold the bus hostage until its reset.)[ google more for info ].
        # For an SLG, whichever memory block -reg,nvm,eeprom - we addressing, a read without
        # first setting the data pointer should be safe, as it will return data from last
        # address set through a previous read/write reqest. We discard the result.
        self.bus._set_address(addr, None)
        msg = self.smbus2.i2c_msg.read(address=addr, length=1)
        self.bus.i2c_rdwr(msg)

    def __gp_wr_0xE3_reg(self, i2c_addr: int, regval: bytearray) -> bool:
        assert 1 == len(regval)
        assert 0 <= regval[0] <= 255, "regval must be in range 0 to 255"
        ewhat = None

        try:
            self.bus.write_i2c_block_data(i2c_addr, 0xE3, regval)
            return True
        except Exception as e:
            ewhat = e

        # Due to device(SLG46826x) NACK'ing us on erase request (ref. errata sheet), the smbus will
        # throw error, but we need to ignore it, otherwise whole erase/write will fail higher up the stack.

        if self.trace_errors == True and ewhat != None:
            print(
                f'{self.__class__.__name__}: "{ewhat}" while trying to write to reg 0xE3...'
            )
        import inspect

        stack = inspect.stack()
        for frame_info in stack:
            # ..but it can be anyone of 3 regions, and we don't know
            # at _this_ stack level where it is; upper driver has that nfo
            # So this is dirty as.
            if frame_info.function == "__erase_page":
                if self.trace_errors == True:
                    print(
                        f"{self.__class__.__name__}: ignoring error while erase page called (device errata)."
                    )
                return True

        return False

    @override
    def gp_read(self, i2c_addr: int, start: int, byte_count: int) -> bytearray | None:
        try:
            if 0 == byte_count:
                # assume caller probing for GP devs on bus
                self.__empty_rd(i2c_addr)  # Can/will throw if no dev found.
                return bytearray()
            offset = start
            data = []
            while byte_count > 0:
                xferlen = min(self.smbus2.I2C_SMBUS_BLOCK_MAX, byte_count)
                data.extend(self.bus.read_i2c_block_data(i2c_addr, offset, xferlen))
                offset += xferlen
                byte_count -= xferlen
            return bytearray(data)
        except Exception as e:
            if self.trace_errors == True:
                str = "SMBus: while reading i2c addr 0x%02x: caught exception: %s" % (
                    i2c_addr,
                    e,
                )
                print(str)
        return None

    @override
    def gp_write(self, i2c_addr: int, start: int, data: bytearray) -> bool:
        try:
            # Put them here so can trace in case of an exception (see below)
            regaddr = start
            bytesleft = len(data)
            offset = 0

            if 0 == len(data):
                # special case as we not actually writing/sending data.
                # (assume caller probing for GP devs on bus).
                self.__empty_wr(i2c_addr)  # Can throw
            elif 1 == len(data):
                if start == 0xE3:  # A non-volatile mem erase request, _possibly_
                    return self.__gp_wr_0xE3_reg(i2c_addr, data)
                else:
                    self.bus.write_i2c_block_data(i2c_addr, start, data)
            else:
                while bytesleft > 0:
                    xferlen = min(self.smbus2.I2C_SMBUS_BLOCK_MAX, bytesleft)
                    self.bus.write_i2c_block_data(
                        i2c_addr, regaddr, data[offset : offset + xferlen]
                    )
                    offset += xferlen
                    bytesleft -= xferlen
                    regaddr += xferlen
        except Exception as e:
            if self.trace_errors == True:
                str = (
                    "SMBus: while writing i2c addr 0x%02x, reg 0x%02x: caught exception: %s"
                    % (i2c_addr, regaddr, e)
                )
                print(str)
            return False

        return True
