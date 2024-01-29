import sys
import os

sys.path.insert(0, os.path.abspath('../src'))
print(f"*** sys.path: {sys.path}")

from greenpak import driver, i2c, utils


#port="/dev/tty.usbmodem101"
#port="/dev/tty.usbmodem1101"
port="COM20"
#port="COM14"
#port="COM17"

config_file = "test_data/slg46826_blinky_slow.txt"
#config_file = "test_data/slg46826_blinky_fast.txt"


print("\nConnecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port = port)
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("\nI2C scanning:")
for addr in range(0, 128):
  if i2c_driver.write(addr, bytearray(), silent=True):
    print(f"* I2C device at address 0x{addr:02x}")


# For information only. Scan the I2C bus for greenpak device. 
print("\nGreenPak scanning:")
devices = gp_driver.scan_greenpak_devices()
for control_code in devices:
  print(f"* Potential GreenPak device at control code 0x{control_code:02x}")

print("\nLoading configuration.")
data = utils.read_bits_config_file(config_file)
utils.hex_dump(data)

print("\nProgramming the NVM.")
gp_driver.program_nvm_pages(0, data)

print ("\nReading the NVM.")
data = gp_driver.read_nvm_bytes(0, 256)
utils.hex_dump(data)

print ("\nWriting config to a file.")
utils.write_bits_config_file("_output_file.txt", data)

print("\nResetting the device.")
gp_driver.reset_device()
