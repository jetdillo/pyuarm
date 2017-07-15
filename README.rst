===============================
Dev branch forked from the uArm-Developer/pyuarm tree
===============================
===============================
pyuarm --- Drivers for the 4-DOF robot arms from ufactory.cc
===============================

## Branched off pyuarm-2.4.x

Overview
========

Latest features:
- Added firmware detection to get_uarm() to allow this code to be used to talk to both uArm Metal and uArm Swift devices. See protocol.py and swift_protocol.py and uarm.py for most of the details about this. 
- method variables added to allow for continued expansion of the package to other future USB VIDs and uArm firmware. 

- I've otherwise tried to mess with the code as little as possible since the ROS uarm package uses this as its driver interface to the uArm device. 
- Tested successfully with a uArm Swift and uArm Metal running Ubuntu 14.04 using ROS Indigo. 

Feedback/testing/PRs, etc. requested, Advice and assistance gladly given, but safety requires avoiding unnecessary conversation. 

Other pages (online)

- `project page on Github`_
- `Download Page`_ with releases
- This page, when viewed online is at https://pyuarm.readthedocs.io.

Features
========
- Auto uArm Port detection
- Provide firmware_helper, firmware upgrade online
- Provide Auto Calibration tool

Requirements
============
- Python 2.7x or Python 3.4x above
- uArmProtocol Firmware (Please use ``uarmcli firmware -d`` or ``python -m pyuarm.tools.firmware -d`` to upgrade your firmware)

Installation
============

pyuarm
------
This install a package that can be used from Python (``import pyuarm``).

To install for all users on the system, administrator rights (root) may be required.

From PyPI
~~~~~~~~~
pyuarm can be installed from PyPI, either manually downloading the files and installing as described below or using::

    pip install pyuarm

From source (tar.gz or checkout)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Download the archive from http://pypi.python.org/pypi/pyuarm.
Unpack the archive, enter the ``pyuarm-x.y`` directory and run::

    python setup.py install

.. _`project page on GitHub`: https://github.com/uArm-Developer/pyuarm
.. _`Download Page`: http://pypi.python.org/pypi/pyuarm
