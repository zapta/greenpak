import greenpak as gp

print("Connecting.")

i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "COM17")

gp_driver = gp.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = gp.read_bits_file("test_data/slg46826_blinky_fast.txt")
gp.hex_dump(data)

print("Programming the NVM.")
gp_driver.program_nvm_pages(0, data)

print ("Reading the NVM.")
data = gp_driver.read_nvm_bytes(0, 256)
gp.hex_dump(data)

print("Resetting the device.")
gp_driver.reset_device()
