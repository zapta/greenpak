
import random
from greenpak import driver, utils, i2c

# port = "/dev/tty.usbmodem1101"
port = "/dev/tty.usbserial-DK0C3UQC"

print("\nConnecting.", flush=True)
# i2c_driver = i2c.GreenPakI2cAdapter(port=port)
i2c_driver = i2c.GreenPakI2cDriver(port=port)

gp_driver = driver.GreenpakDriver(
    i2c_driver, device_type="SLG46826", device_control_code=1)


# Read the entire NVM memory.
print("\nReading entire NVM.", flush=True)
nvm = gp_driver.read_nvm_bytes(0, 256)

# Read random bytes and compare to reference NVM bytes.
print("\nRandom test.", flush=True)
random.seed(0)  # Repeatable rand.
ok_count = 0
err_count = 0
for _ in range(500):
    a = random.randint(0, 255)
    b = gp_driver.read_nvm_bytes(a, 1)[0]
    if b == nvm[a]:
      status = "ok   "
      ok_count += 1
    else:
       status = "ERROR"
       err_count += 1
    print(f"addr {a:02x}, ref: {nvm[a]:02x}, read: {b:02x}  {status}     {ok_count}/{err_count}")

print(f"Ok: {ok_count}, Errors: {err_count}")



