# GreenPak Driver
A Python package to access and program Renesas GreenPak SPLD's.

This Python package provides a simple API to read/write/program Renseas GreenPak PLDs using a USB to I2C link. As of Dec 2023 it supports the Raspberry Pico board with the I2C Adapter firmware loaded into it . See [https://pypi.org/project/i2c-adapter](https://pypi.org/project/i2c-adapter) for more details.

Sample usage:
```python
import greenpak as gp

print("Connecting.")
driver = gp.GreenpakDriver(port="COM17", device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = gp.read_bits_file("slg46826_blinky_fast.txt")
gp.hex_dump(data)

print("Programming NVM.")
driver.program_nvm_pages(0, data)

print ("Reading NVM.")
data = driver.read_nvm_bytes(0, 256)
gp.hex_dump(data)

print("Reseting the device.")
driver.reset_device()
```
