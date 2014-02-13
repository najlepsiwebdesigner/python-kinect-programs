#!/usr/bin/env python
import freenect
import sys
import cv
import cv2
import frame_convert
import numpy as np
import serial, time
import math
import struct


ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2);



while True:
	depth, timestamp = freenect.sync_get_depth()
	height, width =  depth.shape
	y = math.floor(height / 2)
	x = math.floor(width / 2)

	distance = depth[x][y] 
	
	ser.write(str(distance))
	
	time.sleep(0.5);
	print ser.readline();
	
	# ser.write(b'FEST');
	# time.sleep(2);
	# print ser.readline();

