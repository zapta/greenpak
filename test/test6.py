from greenpak import driver, i2c, utils
import random


print("Connecting.")
i2c_driver = i2c.GreenPakI2cDriver(port = "/dev/tty.usbserial-DK0C3UQC")
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

# print("Loading configuration from file.")
# data = utils.read_bits_config_file("test_data/slg46826_blinky_slow.txt")

print("Generating random data.")
data = bytearray()
for _ in range(256):
    data.append(random.randint(0, 255))
utils.hex_dump(data)

print("Programming the EEPROM with the random data.")
gp_driver.program_eeprom_pages(0, data)

print("Resetting the device.")
gp_driver.reset_device()
