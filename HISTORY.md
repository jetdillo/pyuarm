## [1.1.6] - 2016-04-30
### Updated - Alex Tan

### Fix
- read Analog, read EEPROM, read Digital, read Servo Angle, add pin number/ address / servo number before receive data

## [1.1.5] - 2016-04-29
### Updated - Alex Tan

### Fix
- uarm.py Fix MoveTo, Move, moveToOpts


## [1.1.4] - 2016-04-25
### Updated - Alex Tan

### Fix
- calibrate.py Fix is_all_calibrated, is_manual_calibrated, is_linear_calibrated, name issue
- uarm.py Fix PumpStatus , GripperStatus

### Changes

- Add Comment into calibrate.py
- Add Function Complete Flag
- Add Calibrate All Function


## [1.1.3] - 2016-04-25
### Updated - Alex Tan

### Fix
- calibrate.py is_all_calibrated, is_stretch_calibrated, is_manual_calibrated, is_linear_calibrated rename


## [1.1.2] - 2016-04-24
### Updated - Alex Tan

### Changes
- add setup.py for script install
- rename calibrate.py function names to match the Python Standard

## [1.1.1] - 2016-04-21
### Updated - Alex Tan

### Fix
- rename self.uarm to self.sp

### Changes
- Provide uarm isConnected Function


## [1.1.0] - 2016-04-18
### Updated - Alex Tan

### Fix
- Fix float decimal accuracy

### Changes
- Compatible with uArm Firmata v1.5
- New function *list_uarms()* will return all the available uArm ports
- New function *get_uarm()* will return the instance from first port of *list_uarms()*
- get Firmware version when initialize
- Move(x,y,z) Relative action control