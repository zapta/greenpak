import greenpak as gp


port="/dev/tty.usbmodem1101"
#port="COM14"
#port="COM17"

#config_file = "test_data/slg46826_blinky_slow.txt"
config_file = "test_data/slg46826_blinky_fast.txt"


print("\nConnecting.")
i2c_driver = gp.drivers.GreenPakI2cAdapter(port = port)
gp_driver = gp.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

print("\nScanning")
for addr in range(0, 128):
  if i2c_driver.write(addr, bytearray(), silent=True):
    print(f"* I2C device at address 0x{addr:02x}")


# For information only. Scan the I2C bus for greenpak device. 
print("\nScanning:")
devices = gp_driver.scan_greenpak_devices()
for control_code in devices:
  print(f"* Potential GreenPak device at control code 0x{control_code:02x}")

print("\nLoading configuration.")
data = gp.read_config_file(config_file)
gp.hex_dump(data)

print("\nProgramming the NVM.")
gp_driver.program_nvm_pages(0, data)

print ("\nReading the NVM.")
data = gp_driver.read_nvm_bytes(0, 256)
gp.hex_dump(data)

print ("\nWriting config to a file.")
gp.write_config_file("_output_file.txt", data)

print("\nResetting the device.")
gp_driver.reset_device()
