import random
from greenpak import driver, utils, i2c

VERBOSE = False
SEED = 0
ITERS = 10000


def randomize_eeprom(gpd: driver.GreenpakDriver):
    print(f"\n\n ------ Randomizing the EEPROM.")
    if SEED is not None:
        random.seed(SEED)
    data = bytearray()
    for _ in range(256):
        data.append(random.randint(0, 255))
    print("\nRandom data:")
    utils.hex_dump(data)
    print("\nProgramming the eeprom")
    gpd.program_eeprom_pages(0, data)
    print("Resetting the device.")
    gpd.reset_device()


def format_set(s: set):
    l = list(s)
    l.sort()
    l_str = []
    for b in l:
        l_str.append(f"{b:02x}")
    return str(l_str)


def test_mem_space(name: str, read_method) -> None:
    print(f"\n\n ------ Testing {name} memory space.")
    if SEED is not None:
        random.seed(SEED)
    mem = read_method(0, 256)
    good_set = set()
    bad_set = set()
    ok_count = 0
    err_count = 0
    print(f"Performing {ITERS} reads...")
    for _ in range(ITERS):
        a = random.randint(0, 255)
        b = read_method(a, 1)[0]
        ok = b == mem[a]
        if ok:
            status = "ok   "
            ok_count += 1
            good_set.add(a)
        else:
            status = "ERROR"
            err_count += 1
            bad_set.add(a)
        # Verbose log
        if VERBOSE or not ok:
            print(
                f"addr {a:02x}, ref: {mem[a]:02x}, read: {b:02x}  {status}     {ok_count}/{err_count}"
            )
    print(f"Ok  reads: {ok_count}")
    print(f"Err reads: {err_count}")
    print(f"Good address count: {len(good_set)}")
    print(f"Good/bad addresses: {format_set(bad_set.intersection(good_set))}")
    print(f"Bad only addresses: {format_set(bad_set)}")


# Main

print("\nConnecting.", flush=True)

# i2c_driver = i2c.GreenPakI2cDriver(port="/dev/tty.usbserial-DK0C3UQC")
i2c_driver = i2c.GreenPakI2cAdapter(port="/dev/tty.usbmodem1401")
gp_driver = driver.GreenpakDriver(
    i2c_driver, device_type="SLG46826", device_control_code=1
)

randomize_eeprom(gp_driver)
test_mem_space("EEPROM", gp_driver.read_eeprom_bytes)
test_mem_space("NVM", gp_driver.read_nvm_bytes)
test_mem_space("REGISTER", gp_driver.read_register_bytes)
