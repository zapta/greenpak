import sys
import os

sys.path.insert(0, os.path.abspath("../src"))
import greenpak as gp
import greenpak.utils as utils
import greenpak.i2c as i2c


# code1 = 1
# spec2 = "0010"
# code2 = 2

code1 = 2
spec2 = "0001"
code2 = 1

# code1 = 4
# spec2 = "0001"
# code2 = 1


# port="/dev/tty.usbmodem101"
port = "/dev/tty.usbmodem1101"
# port="COM14"
# port="COM17"


print("\nConnecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port=port)
gp_driver = gp.GreenpakDriver(
    i2c_driver, device_type="SLG46826", device_control_code=code1
)

print("\nI2C scanning:")
for addr in range(0, 128):
    if i2c_driver.write(addr, bytearray(), silent=True):
        print(f"* I2C device at address 0x{addr:02x}")


# For information only. Scan the I2C bus for greenpak device.
print("\nGreenPak scanning:")
devices = gp_driver.scan_greenpak_devices()
for control_code in devices:
    print(f"* Potential GreenPak device at control code 0x{control_code:02x}")


print("\nProgramming control code", flush=True)
gp_driver.program_control_code(spec2)

print("\nResetting device", flush=True)
gp_driver.reset_device()

print("\nI2C scanning:")
for addr in range(0, 128):
    if i2c_driver.write(addr, bytearray(), silent=True):
        print(f"* I2C device at address 0x{addr:02x}")

print("\nGreenPak scanning:")
devices = gp_driver.scan_greenpak_devices()
for control_code in devices:
    print(f"* Potential GreenPak device at control code 0x{control_code:02x}")

