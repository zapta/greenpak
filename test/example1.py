import greenpak as gp
import greenpak.utils as utils
import greenpak.i2c as i2c

print("Connecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
gp_driver = gp.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("Loading configuration.")
data = utils.read_bits_config_file("test_data/slg46826_blinky_slow.txt")
utils.hex_dump(data)

print("Programming the NVM.")
gp_driver.program_nvm_pages(0, data)

print("Resetting the device.")
gp_driver.reset_device()
