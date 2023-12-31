import greenpak as gp

print("Connecting.")
i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "COM18")
gp_driver = gp.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = gp.read_bits_file("test_data/blinky_nvm_slow.txt")
gp.hex_dump(data)

print("Programming NVM.")
gp_driver.program_nvm_pages(0, data)

print ("Reading NVM.")
data = driver.read_nvm_bytes(0, 256)
gp.hex_dump(data)

print("Reseting the device.")
gp_driver.reset_device()
