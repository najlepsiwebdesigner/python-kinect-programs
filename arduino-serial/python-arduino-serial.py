import serial, time
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2);

ser.write(b'FORWARD');

time.sleep(0.1);

ser.write(b'STOP');


while True:
	print ser.readline();
