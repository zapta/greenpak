import sys
import os

sys.path.insert(0, os.path.abspath('../src'))
import greenpak as gp
import greenpak.utils as utils
import greenpak.i2c as i2c
from random import randbytes



#port="/dev/tty.usbmodem101"
port="/dev/tty.usbmodem1101"
#port="COM14"
#port="COM17"

print("\nConnecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port = port)
gp_driver = gp.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("\nI2C scanning:")
for addr in range(0, 128):
  if i2c_driver.write(addr, bytearray(), silent=True):
    print(f"* I2C device at address 0x{addr:02x}")


print("\nRandom data.")
data = randbytes(256)
utils.hex_dump(data)

print("\nProgramming the EEPROM.")
gp_driver.program_eeprom_pages(0, data)

print ("\nReading the EEPROM.")
data = gp_driver.read_eeprom_bytes(0, 256)
utils.hex_dump(data)


