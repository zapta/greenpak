from greenpak import driver, i2c, utils

print("Connecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("Loading configuration from file.")
data = utils.read_bits_config_file("test_data/slg46826_blinky_slow.txt")
utils.hex_dump(data)

print("Programming the NVM.")
gp_driver.program_nvm_pages(0, data)

print("Resetting the device.")
gp_driver.reset_device()
