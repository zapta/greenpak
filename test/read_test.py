
import random
from greenpak import driver, utils, i2c

port = "/dev/tty.usbmodem1101"
#port = "/dev/tty.usbserial-DK0C3UQC"

print("\nConnecting.", flush=True)
i2c_driver = i2c.GreenPakI2cAdapter(port=port)
#i2c_driver = i2c.GreenPakI2cDriver(port=port)

gp_driver = driver.GreenpakDriver(
    i2c_driver, device_type="SLG46826", device_control_code=1)


print("\nReading entire mem space.", flush=True)
#mem = gp_driver.read_eeprom_bytes(0, 256)
#mem = gp_driver.read_nvm_bytes(0, 256)
mem = gp_driver.read_register_bytes(0, 256)


bad_set = set()

random.seed(0)  # Repeatable rand.
ok_count = 0
err_count = 0
#for i in range(256):
for _ in range(5000):
    #a = 255 - i
    a = random.randint(0, 255)
    #b = gp_driver.read_eeprom_bytes(a, 1)[0]
    #b = gp_driver.read_nvm_bytes(a, 1)[0]
    b = gp_driver.read_register_bytes(a, 1)[0]
    if b == mem[a]:
      ok = True
      status = "ok   "
      ok_count += 1
    else:
       ok = False
       status = "ERROR"
       err_count += 1
       bad_set.add(a)

       
    print(f"addr {a:02x}, ref: {mem[a]:02x}, read: {b:02x}  {status}     {ok_count}/{err_count}")
    if not ok:
      for i in range(5):
         b = gp_driver.read_eeprom_bytes(a, 1)[0]
         print(f"  {b:02x}")

print(f"Ok: {ok_count}, Errors: {err_count}")
bad_list = list(bad_set)
bad_list.sort()
for a in bad_list:
   print(f"Bad address: {a:02x}")
bad_list_str = []
for a in bad_list:
   bad_list_str.append(f"{a:02x}")
print(f"Bad addresses: {bad_list_str}")



