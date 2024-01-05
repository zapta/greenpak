from greenpak import driver, i2c

i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

# Scan for I2C devices, printing their addresses.
print("Scanning for I2C addresses:")
for addr in range(0, 128):
    if i2c_driver.write(addr, bytearray(), silent=True):
        print(f"* I2C device at address 0x{addr:02x}")

# Scan for GreenPak devices, printing their control codes. Each GreenPak devices
# occupies 4 consecutive I2C addresses, one for each of its memory spaces.
print("Scanning for GreenPak control codes:")
for control_code in gp_driver.scan_greenpak_devices():
    print(f"* Potential GreenPak device at control code 0x{control_code:02x}")

