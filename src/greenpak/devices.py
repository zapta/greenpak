"""A library to manage and program GreenPAK devices using USB to I2C adapters."""

# Docs
# https://www.renesas.com/us/en/document/mat/system-programming-guide-slg468246?r=1572991
# https://www.renesas.com/us/en/document/mat/slg47004-system-programming-guide?r=1572991

from greenpak.i2c import GreenPakI2cInterface
from enum import Enum
from typing import Optional, List, Tuple, Set, Dict
import time
import re
from importlib import resources as impresources
from . import data_files
import copy


# from intelhex import IntelHex
import greenpak.utils as utils


# The byte that is used to trigger the erase page command.
ERASE_BYTE_ADDR: int = 0xE3


class DeviceTypeDescriptor:
    """Descriptor of a GreenPak device.

    :param device_type: The name of the device model. E.g. "SLG46826".
    :type device_type: str

    :param ro_nvm_pages: List of indexes of read-only NVM pages that can be erase/program by the user. Renesas call them
        'service pages'.
    :type ro_nvm_pages: List[int]

    :param erase_byte_addr: The address of the REGISTER space byte which is used to trigger a page erasure.
    :type erase_byte_addr: int

    :param erase_byte_mask: The fixed bit masked that is written to the erase byte to trigger erasure of a page.
    :type erase_byte_mask: int

    :param control_code_addr: The address in the NVM memory space of the byte that contains the control
        code setting of the device.
    :type control_code_addr: int

    :param default_config_file_name: The name of the data file which contains the default configuration of the device.
       That is, the configuration of a factory reset device, as read from the NVM.
    :type default_config_file_name: str
    """

    def __init__(
        self,
        device_type: str,
        ro_nvm_pages: List[int],
        erase_byte_addr: int,
        erase_byte_mask: int,
        control_code_addr: int,
        default_config_file_name: str,
    ):
        assert isinstance(device_type, str)
        assert len(device_type) > 0
        assert isinstance(ro_nvm_pages, list)
        assert len(set(ro_nvm_pages)) == len(ro_nvm_pages), "Duplicate pages"
        for page_index in ro_nvm_pages:
            assert isinstance(page_index, int)
            assert 0 <= page_index <= 15
        assert isinstance(erase_byte_addr, int)
        assert 0 <= erase_byte_addr <= 255
        assert isinstance(erase_byte_mask, int)
        assert 0 <= erase_byte_mask <= 255
        assert (erase_byte_mask & 0b00011111) == 0
        assert isinstance(control_code_addr, int)
        assert 0 <= control_code_addr < 256
        assert isinstance(default_config_file_name, str)

        self.device_type: str = device_type
        self.ro_nvm_pages: List[int] = ro_nvm_pages
        self.erase_byte_addr: int = erase_byte_addr
        self.erase_byte_mask: int = erase_byte_mask
        self.control_code_addr: int = control_code_addr
        fname = impresources.files(data_files) / default_config_file_name
        self.default_config: bytes = bytes(utils.read_hex_config_file(fname))


# List of supported device.
__DEVICE_LIST = [
    DeviceTypeDescriptor(
        "SLG46824", [15], 0xE3, 0b10000000, 0xCA, "SLG46824_default.hex"
    ),
    DeviceTypeDescriptor(
        "SLG46826", [15], 0xE3, 0b10000000, 0xCA, "SLG46826_default.hex"
    ),
    DeviceTypeDescriptor(
        "SLG46827", [15], 0xE3, 0b10000000, 0xCA, "SLG46827_default.hex"
    ),
    DeviceTypeDescriptor(
        "SLG47004", [8, 15], 0xE3, 0b11000000, 0x7F, "SLG47004_default.hex"
    ),
]

# Same as above, but as a dict keyed by device type.
__DEVICE_DICT: Dict[str, DeviceTypeDescriptor] = dict(
    [(d.device_type, d) for d in __DEVICE_LIST]
)


def device_type_descriptor(device_type: str) -> DeviceTypeDescriptor:
    """Return the GreenPak device descriptor for the given device type.

    :param device_type: The id of a supported device. For example "SLG46826". The function asserts
        that the ``device_type`` is supported.
    :type device_type: str

    :returns: A descriptor with the specification of the device type.
    :rtype: DeviceTypeDescriptor
    """
    return copy.deepcopy(__DEVICE_DICT[device_type])
