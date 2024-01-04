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


Programming a GreenPak device in circuit. Upon reset, the GreenPak device loads the
new configuration from its NVM memory.

.. code-block:: python
  :linenos:

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


Loading the configuration from the NVM space of a GreenPak device and writing it
to a file. This requires the device to be non locked.

.. code-block:: python
  :linenos:

  import greenpak as gp

  print("Connecting.")
  i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "COM17")
  gp_driver = gp.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)

  print ("\nReading the NVM.")
  data = gp_driver.read_nvm_bytes(0, 256)
  gp.hex_dump(data)

  print ("\nWriting to a file.")
  gp.write_config_file("_output_file.txt", data)


Scanning for I2C devices vs scanning for GreenPak devices. Each GreenPak devices appear at
four consecutive I2C addresses.

.. code-block:: python
  :linenos:

  import greenpak as gp

  # Scan for I2C devices, printing their addresses.
  i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
  for addr in range(0, 128):
      if i2c_driver.write(addr, bytearray(), silent=True):
          print(f"* I2C device at address 0x{addr:02x}")


  # Scan for GreenPak devices, printing their control codes. Each GreenPak devices
  # occupies 4 consecutive I2C addresses, one for each of its memory spaces.
  print("\nScanning:")
  for control_code in gp_driver.scan_greenpak_devices():
      print(f"* Potential GreenPak device at control code 0x{control_code:02x}")


Initial in-circuit programming of three factory reset GreenPak devices, one of type
SLG47004 and two of type SLG46826. This is an **experimental** example that may requires
some tweaks.

.. code-block:: python
  :linenos:

  import greenpak as gp

  # Initially all three devices respond to control code 1.
  i2c_driver = gp.drivers.GreenPakI2cAdapter(port = "/dev/tty.usbmodem1101")
  gp_driver = gp.GreenpakDriver(i2c_driver, device="SLG46826", control_code=0b0001)
  assert gp_driver.scan_greenpak_device(0b0001)
  
  # Init the control codes devices of each potential type. We assume that the 
  # devices are wired with two control codes pins.
  gp_driver.set_device_type("SLG47004")
  gp_driver.program_control_code("01XX")

  gp_driver.set_device_type("SLG46826")
  gp_driver.program_control_code("01XX")

  # The three devices should be at designated control codes. We assume that there
  # input pins are wired as 0b00, 0b01, 0b10 respectivly.
  assert not gp_driver.scan_greenpak_device(0b0001)  # No more at default control code
  assert gp_driver.scan_greenpak_device(0b0100)  # Device 1
  assert gp_driver.scan_greenpak_device(0b0101)  # Device 2
  assert gp_driver.scan_greenpak_device(0b0110)  # Device 3

  # At this point the devices are at their designated addresses and can be programmed
  # as usual. The programmed configuration of each device should maintain its
  # control code.
  
|

Installation
================

The Python API package is available from PyPi at https://pypi.org/project/greenpak and can be installed
on your computer using pip:

.. code-block:: shell

  pip install greenpak

|

API Reference
=============

.. automodule:: greenpak
  :members:
  :member-order: bysource

.. automodule:: greenpak.drivers
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

