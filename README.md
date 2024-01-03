# GreenPak Driver
A Python package to access and program Renesas GreenPak SPLD's.

This Python package provides a simple to use API to read/write/program Renseas GreenPak PLDs over a USB to I2C link. 

As of December 2023, the package supports the following USB to I2C interfaces and new ones can be easily added based on the examples in [drivers.py](https://github.com/zapta/greenpak/blob/main/src/greenpak/drivers.py): 
* [I2C Driver](https://pypi.org/project/i2cdriver/) (two variants, mini and full.)
* [I2C Adapter](https://pypi.org/project/i2c-adapter/) (four variants, including a bare Raspberry Pico.)

Sample usage using an [I2C Adapter](https://pypi.org/project/i2c-adapter):

```python
import greenpak as gp

print("Connecting.")
i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "COM17")
gp_driver = gp.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = gp.read_bits_file("test_data/slg46826_blinky_fast.txt")
gp.hex_dump(data)

print("Programming the NVM.")
gp_driver.program_nvm_pages(0, data)

print("Resetting the device.")
gp_driver.reset_device()
```

<br>

For full documentation see https://greenpak.readthedocs.io/en/latest
