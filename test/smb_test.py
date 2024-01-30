#This file contains example purely for exercising the greenpak driver using
#SMBUs adapter. There is no other purpose and it does nothing useful.

import sys
sys.path.append('./src/greenpak/')
from greenpak import driver, utils, i2c
from i2c import GreenPakI2cInterface, GreenPakSMBusAdapter
from utils import hex_dump

# def hexdump(data, showaddr=0):
#     offset = 0
#     while offset < len(data):
#         line = format(showaddr + offset, '4x') + ':'
#         count = min(len(data) - offset, 16)
#         for i in range(count):
#             line += ' ' + format(data[offset + i], '02x')
#         print(line)
#         offset += count

print("Testing...")
i2c_driver = i2c.GreenPakSMBusAdapter()

# --- Test of emptiness  ---
print("empty read/write to non-attached ...")
#Use some invalid (not connected) address, to test them empty reads/writes.
bad_addr = 0x20
i2c_driver.read(bad_addr, 0, False)
i2c_driver.write(bad_addr, bytearray(), False)
good_addr = 0x8
print("empty read/write to an attached...")
if None != i2c_driver.read(good_addr, 0, False):
  print("RD: found it.")
if True == i2c_driver.write(good_addr, bytearray(), False):
   print("WR: found it.")

#print("GreenPakSMBusAdapter is subclass of GreenPakI2cInterface:", issubclass(GreenPakSMBusAdapter, GreenPakI2cInterface))
#print("Type of GreenPakSMBusAdapter instance:", type(i2c_driver))

slg_code = 0b0010
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=slg_code)
print( gp_driver.get_device_type() )

found = True

try:
  reg_bytes = gp_driver.read_register_bytes(0, 256)
  print("~ Dumping reg mem ... ~")
  hex_dump(reg_bytes)
except Exception as e:
    print(f' Likely NO device at your control code 0x{slg_code:02x} !')
    found = False

if not found:
  print("Scanning for GreenPak control codes:")
  for control_code in gp_driver.scan_greenpak_devices():
      print(f"* Potential GreenPak device at control code 0x{control_code:02x}")
      slg_code = control_code
      found = True

if found:
  gp_driver.set_device_control_code(slg_code)
  gp_driver.reset_device()
  reg_bytes = gp_driver.read_register_bytes(0, 256)
  #print("Type of reg_bytes:", type(reg_bytes))
  print("~ Dumping reg mem ... ~")
  hex_dump(reg_bytes)
  nvm_bytes = gp_driver.read_nvm_bytes(0, 256)
  print("~ Dumping nvm mem ... ~")
  hex_dump(nvm_bytes)
  eep_bytes = gp_driver.read_eeprom_bytes(0, 256)
  print("~ Dumping eep mem ... ~")
  hex_dump(eep_bytes)
