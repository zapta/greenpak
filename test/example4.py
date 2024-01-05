from greenpak import driver, i2c

def scan():
  for control_code in gp_driver.scan_greenpak_devices():
    print(f"* Found control code {control_code}")
  for addr in range(0, 128):
    if i2c_driver.write(addr, bytearray(), silent=True):
        print(f"* Found I2C address 0x{addr:02x}")

# Initially all three devices respond to control code 1.
i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

# At this points, all the devices are at the Renesas's default control code 1.
print("Scan before:")
scan()

# Move the devices to their permanent address. In this example we assume that each device
# has two control code input pins that are hard wired to a unique combination.
for device_type in ["SLG47004", "SLG46826"]:
    if gp_driver.scan_greenpak_device(0b0001):
        gp_driver.set_device_type(device_type)
        gp_driver.program_control_code("01XX")
        gp_driver.reset_device()

# Here the devices are at their designated addresses and can be programmed individually.
print("Scan after:")
scan()
assert not gp_driver.scan_greenpak_device(0b0001)



