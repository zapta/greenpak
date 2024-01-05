import greenpak as gp
import greenpak.utils as utils
import greenpak.i2c as i2c

print("Connecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
gp_driver = gp.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print ("Reading the configuration from device's NVM.")
data = gp_driver.read_nvm_bytes(0, 256)
utils.hex_dump(data)

print ("Writing configuration to a file.")
utils.write_hex_config_file("_output_file.hex", data)

