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
* `i2cdriver <https://pypi.org/project/i2cdriver/>`_ 

Wiring
======

TBD


Examples
========

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

  print ("Reading the NVM.")
  data = gp_driver.read_nvm_bytes(0, 256)
  gp.hex_dump(data)

  print("Resetting the device.")
  gp_driver.reset_device()

  Scan the I2C bus for devices:

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

|


Contact
=======

Bug reports and contributions are welcome. You can contact the team and fellow users at the 
gibhub repository at https://github.com/zapta/greenpak.



.. toctree::
  :maxdepth: 2
  :caption: Contents:

