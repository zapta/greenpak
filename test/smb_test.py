#This file contains example purely for exercising the greenpak driver using
#SMBUs adapter. There is no other purpose and it does nothing useful.

import sys
import random
import os

# Use this if you have built the GreenPak library package with the provided build script, and have
# installed it into your environment. ---->
sys.path.append('./src/greenpak/')
from greenpak import driver, utils, i2c
# from i2c import GreenPakI2cInterface, GreenPakSMBusAdapter
# from utils import hex_dump
#          ..... <--------------------
# Use this if you haven't built and/or installed GreenPak library, and you working with the sources
# as layed out in the repo  ---------->
# directory_path = os.path.join(os.path.dirname(__file__), '../src/')
# sys.path.insert(0, directory_path)
# from greenpak import driver
# from greenpak import i2c
# from greenpak import utils
# from greenpak.utils import hex_dump
#          ..... <--------------------

print("Testing...")
i2c_driver = i2c.GreenPakSMBusAdapter(traces=True)

# --- Test of emptiness  ---
print("empty read/write to non-attached ...")
#Use some invalid (not connected) address, to test them empty reads/writes.
bad_addr = 0x20
i2c_driver.gp_read(bad_addr, 0, 0)
i2c_driver.gp_write(bad_addr, 0, bytearray())
good_addr = 0x60
print("empty read/write to an attached...")
if None != i2c_driver.gp_read(good_addr, 0, 0):
  print("RD: found it.")
if True == i2c_driver.gp_write(good_addr, 0, bytearray()):
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
  utils.hex_dump(reg_bytes)
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
  #Note: re-setting device potentially will re-set it's I2C address immediately,
  #as would be the case after the blinky bitcode has been uploaded into reg memory
  #(below). Still can test this call if you like.
  #gp_driver.reset_device()
  reg_bytes = gp_driver.read_register_bytes(0, 256)
  print("~ Dumping reg mem ... ~")
  utils.hex_dump(reg_bytes)
  nvm_bytes = gp_driver.read_nvm_bytes(0, 256)
  print("~ Dumping nvm mem ... ~")
  utils.hex_dump(nvm_bytes)
  eep_bytes = gp_driver.read_eeprom_bytes(0, 256)
  print("~ Dumping eep mem ... ~")
  utils.hex_dump(eep_bytes)
  print("~tesing write to reg mem...~")
  data = utils.read_bits_config_file("./test/test_data/slg46826_blinky_slow.txt")
  gp_driver.write_register_bytes(0, data)

  print("~testing write register at an offset...~")
  reg_at_start = gp_driver.read_register_bytes(1, 1)
  regs_at_end  = gp_driver.read_register_bytes(0xf4, 4)

  assert len(reg_at_start) == 1
  assert len(regs_at_end) == 4

  if reg_at_start[0] != reg_bytes[1]:
     print("ERROR: test of 1 byte read failed.")
  if regs_at_end[0:4] != reg_bytes[0xf4:0xf4+4]:
     print("ERROR: test of 4 byte read failed.")

  print("~testing write to EEP memory...~")
  #note, eep_bytes holds currently read-out EEPROM data
  dummy_eep_data = [random.randint(0, 0xFF) for _ in range(256)]
  try:
     print(" ..writing dummy data to EEP..")
     gp_driver.program_eeprom_pages(0, bytearray(dummy_eep_data))
     print(" ..write ok.. Want to re-store your previous data...")
     gp_driver.program_eeprom_pages(0, eep_bytes)
     #do a read-back on original..
     rbtest = gp_driver.read_eeprom_bytes(0, 256)
     if rbtest != eep_bytes:
        raise RuntimeError("Failed to verify write to EEPROM!")
     print("restored ok.")
  except Exception as e:
     print("FAILED to write EEPROM. You may want to check its' contents.")
