import serial
import time
import numpy
from time import sleep

ser = serial.Serial('/dev/ttyACM0',9600) 
sleep(1)

# PI -> INO chars (works) ----------------------------------------------

#while True:
	#var1 = 'A'
	#var2 = 'Z'
	
	#ser.write(bytes(var1, 'UTF-8'))
	#sleep(1)
	#ser.write(bytes(var2, 'UTF-8'))
	#sleep(1)
	
# PI -> INO nums (limited)---------------------------------------------

#while True:
	#var1 = str(0)   # valid only for 0 to 9
	#var2 = str(9)
	
	#ser.write(bytes(var2, 'UTF-8'))
	#sleep(1)
	#ser.write(bytes(var2, 'UTF-8'))
	#sleep(1)

# PI -> INO nums (works)---------------------------------------------

#while True:
	#var1 = 0   # Valid range is 0 to 255
	#var2 = 255
	
	#ser.write(bytes([var1]))
	#sleep(1)
	#ser.write(bytes([var2]))
	#sleep(1)
	

# INO -> PI char (works)------------------------------------------------

while True:
	datain = ser.readline()
	datain = chr(int(datain, 16))
	print(datain)

	if(datain == 'B'):
		print('IT REGISTERS MWAHAHAH!')

## INO -> PI nums (works) -----------------------------------------------

#while True:
	#data = str(int (ser.readline(),10))
	#data = int(data)
	#print(data)
	
	#mult = data/10
	#if (mult).is_integer():
		#print('Hey this number is a multiple of 10!')
	
	
