import serial
import os
import sys
import time

swift_msg="#254 P2203\n"
metal_msg="#255 P203\n"

ser=serial.Serial("/dev/ttyUSB1",115200)

proto_version="none"
ser.flushInput()
ser.write(swift_msg)
time.sleep(2)
results=ser.read(ser.in_waiting)
print results
if "OK" in results:
   proto_version="swift"
else: 
   ser.flushInput()
   ser.write(metal_msg)
   time.sleep(2)
   results=ser.read(ser.in_waiting)
   if "OK" in results:
      proto_version="metal"
   else:
      proto_version="none"
print proto_version
ser.close()
         
