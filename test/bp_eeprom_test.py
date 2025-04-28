import sys
import os

sys.path.insert(0, os.path.abspath('../src'))
print(f"*** sys.path: {sys.path}")

from greenpak import driver, i2c, utils
import random
from time import sleep

port="/dev/buspirate"


print("\nConnecting.")
i2c_driver = i2c.GreenPakBusPirate(port = port)
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("Generating random data.")
data = bytearray()
for _ in range(256):
    data.append(random.randint(0, 255))
utils.hex_dump(data)

print("Programming the EEPROM with the random data.")
gp_driver.program_eeprom_pages(0, data)

print ("\nReading the EEPROM.")
read_data = gp_driver.read_eeprom_bytes(0, 256)
utils.hex_dump(read_data)

if data == read_data:
    print ("EEPROM data verification succeeded.")
else:
    print ("EEPROM data verification failed.")

print("Erasing the EEPROM")
i2c_addr = gp_driver.get_device_control_code() << 3
for page in range(16):
    i2c_driver.gp_write(i2c_addr, 0xe3, [0x90 + page])
sleep(0.025)
read_data = gp_driver.read_eeprom_bytes(0, 256)
assert all(byte == 0 for byte in read_data)

print("Resetting the device.")
gp_driver.reset_device()
