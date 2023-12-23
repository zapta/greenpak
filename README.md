# greenpak_driver
A Python package to access and program Renesas GreenPak SPLD's.

This Python package provides a simple API to read/write/program Renseas GreenPak PLDs using a USB to I2C link. As of Dec 2023 it supports the Raspberry Pico board with the I2C Adapter firmware loaded into it . See [https://pypi.org/project/i2c-adapter](https://pypi.org/project/i2c-adapter) for more details.

Installation
```
pip install greenpak_driver --upgrade
```

Sample usage:
```python

import greenpak_driver as gp

print("Connecting.")
driver = gp.GreenPakDriver(port="COM17", control_code=0b0001)

print("Loading configuration.")
data = gp.load_greenpak_bits_file("my_design.txt)
gp.dump_hex(data)

print("Programming NVM.")
driver.program_nvm_pages(0, data)

print ("Reading NVM.")
data = driver.read_nvm_bytes(0, 256)
gp.dump_hex(data)

print("Reseting the devic.e")
driver.reset_device()
```
