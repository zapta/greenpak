.. I2C Adapter API documentation master file, created by
   sphinx-quickstart on Sun Dec 31 17:40:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. See rst cheat sheet at 
   https://docs.anaconda.com/restructuredtext/index.html

Overview
========
``greenpak`` is Python package that provides access and programming of Renesas GreenPak
SPLD's via I2C bus adapters. This is done via a simple to use API that is abstracted
at the GreenPak model level.

The package supports all USB to I2C adapters that are supported by the following
python drivers and support for new drivers can be easily added.

* `i2c_adapter <https://pypi.org/project/i2c-adapter/>`_
* `i2cdriver <https://i2cdriver.com/>`_ 

|

Wiring
======

:Important:
  Do not exceed the max voltages of the I2C adapter and the GreenPak device(s). If necessary,
  use I2C level shifter to adapt the SDA/SCL signal level.

.. csv-table:: 
   :header: "I2C Adapter pin", "GreenPak pin", "Comments"
   :widths: 15, 15, 50

   "GND", "GND", "Common ground"
   "VCC", "VDD, VDD2", "Optional, if circuit is not self powered."
   "SDA", "SDA", "I2C data line. Should have a pullup resistor."
   "SCL", "SCL", "I2C clock line. Should have a pullup resistor."

|

Examples
========

Programming a device
--------------------

Programming a GreenPak device in circuit. Upon reset, the GreenPak device loads the
new configuration from its NVM memory.

.. code-block:: python
  :linenos:

  from greenpak import driver, i2c, utils

  print("Connecting.")
  i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
  gp_driver = gp.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

  print("Loading configuration from file.")
  data = utils.read_bits_config_file("test_data/slg46826_blinky_slow.txt")
  utils.hex_dump(data)

  print("Programming the NVM.")
  gp_driver.program_nvm_pages(0, data)

  print("Resetting the device.")
  gp_driver.reset_device()

  
Reading device configuration
----------------------------

Loading the configuration from the NVM space of a GreenPak device and writing it
to a file. This requires the device to be non locked.

.. code-block:: python
  :linenos:

  from greenpak import driver, i2c, utils

  print("Connecting.")
  i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
  gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

  print ("Reading the configuration from device's NVM.")
  data = gp_driver.read_nvm_bytes(0, 256)
  utils.hex_dump(data)

  print ("Writing configuration to a file.")
  utils.write_hex_config_file("_output_file.hex", data)

Scanning the I2C bus 
--------------------

Scanning for I2C devices vs scanning for GreenPak devices. Each GreenPak devices appear at
four consecutive I2C addresses.

.. code-block:: python
  :linenos:

  from greenpak import driver, i2c

  i2c_driver = i2c.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
  gp_driver = driver.GreenpakDriver(i2c_driver, device_type="SLG46826", device_control_code=0b0001)

  # Scan for I2C devices, printing their addresses.
  print("Scanning for I2C addresses:")
  for addr in range(0, 128):
      if i2c_driver.write(addr, bytearray(), silent=True):
          print(f"* I2C device at address 0x{addr:02x}")

  # Scan for GreenPak devices, printing their control codes. Each GreenPak devices
  # occupies 4 consecutive I2C addresses, one for each of its memory spaces.
  print("Scanning for GreenPak control codes:")
  for control_code in gp_driver.scan_greenpak_devices():
      print(f"* Potential GreenPak device at control code 0x{control_code:02x}")

Assigning initial addresses
---------------------------

Initial in-circuit programming of three factory reset GreenPak devices, one of type
SLG47004 and two of type SLG46826. This is an **experimental** example that may requires
some tweaks.

.. code-block:: python
  :linenos:

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

|

Installation
=============

The Python API package is available from PyPi at https://pypi.org/project/greenpak and can be installed
on your computer using pip:

.. code-block:: shell

  pip install greenpak

|

API Reference
=============

.. automodule:: greenpak.driver
  :members:
  :member-order: bysource

.. automodule:: greenpak.utils
  :members:
  :member-order: bysource

.. automodule:: greenpak.i2c
  :members:
  :member-order: bysource

|


Contact
=======

Bug reports and contributions are welcome. You can contact the team and fellow users at the 
gibhub repository at https://github.com/zapta/greenpak.



.. toctree::
  :maxdepth: 2
  :caption: Contents:

