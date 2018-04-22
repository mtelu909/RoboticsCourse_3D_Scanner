import serial
import time
import numpy

ser = serial.Serial('/dev/ttyACM0',19200)
s = [0,1]
g = [0,1]
while True:
	read_serial=ser.readline()
	#time.sleep(.1)
	#s[0] = str(int (ser.readline(),16)) #16 = hexa!
	#meh = int(ser.readline(),16)
	#D=int (ser.readline(),10)
	#blee = s[0]
	#bloo = pow(blee,2)
	#print(s[0])
	#print(meh)
	#print(read_serial)
	#print(D)
	
	g[0]= str(int (ser.readline(), 16)) #16 = hexa!
	print(g[0])
	
