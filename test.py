#!/usr/bin/env python
import sys
import serial, time
import math
import struct


ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.write("\x01\x016\0x19\x03\x03")
while True:
	print ser.read();


