# GreenPak Driver
A Python package to access and program Renesas GreenPak SPLD's.

This Python package provides a simple to use API to read/write/program Renseas GreenPak PLDs over a USB to I2C link. 

As of May 2025, the package supports the following USB to I2C interfaces and new ones can be easily added based on the examples in [i2c.py](https://github.com/zapta/greenpak/blob/main/src/greenpak/i2c.py): 
* [I2C Driver](https://pypi.org/project/i2cdriver/) (two variants, mini and full.)
* [I2C Adapter](https://pypi.org/project/i2c-adapter/) (four variants, including a bare Raspberry Pico.)
* [Bus Pirate](https://dangerousprototypes.com/docs/Bus_Pirate) (v2, v3 and v4)

Sample usage using an [I2C Adapter](https://pypi.org/project/i2c-adapter):

```python
from greenpak import driver, i2c, utils

print("Connecting.")
i2c_driver = i2c.GreenPakI2cAdapter(port="COM17")
gp_driver = driver.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = utils.read_bits_file("test_data/slg46826_blinky_fast.txt")
utils.hex_dump(data)

print("Programming the NVM.")
gp_driver.program_nvm_pages(0, data)

print("Resetting the device.")
gp_driver.reset_device()
```

<br>

For full documentation see https://greenpak.readthedocs.io/en/latest
