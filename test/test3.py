import sys
import os

# sys.path.insert(0, os.path.abspath('../src'))
# print(f"*** sys.path: {sys.path}")

from greenpak import driver, i2c, utils


#port="/dev/tty.usbmodem101"
port="/dev/tty.usbmodem1101"
#port="COM14"
#port="COM17"

# config_file = "test_data/slg46826_blinky_slow.txt"
#config_file = "test_data/slg46826_blinky_fast.txt"

devices = ["SLG46824", "SLG46826", "SLG46827", "SLG47004"]

for d in devices:
    print(f"Processing {d}", flush=True)
    data = utils.read_hex_config_file(f"../src/greenpak/data_files/{d}_default.hex")
    #  utils.write_bits_config_file(f"_{d}.txt", data)
    print(f"{d} F9 = {data[0xf9]:09b}")


# for a in devices:
#    for b in devices:
#       if a < b:
#          print(f"diff _{a}.txt _{b}.txt")
      