# DESCRIPTION
# Program to read a laserline and turn it into an array of heights
# (Incomplete)

# Initializing the Program
import cv2
import time
import numpy as np
import os, shutil

# USER INPUTS ----------------------------------------------------------

INPUT_PIN = 4           # Sets our input pin

xcount = 48				# Number of slices
scan_max = 5			# Number of pictures taken
gap = 20				# Pixel Width of slice 
H = 540					# Pixel Height of Window
W = 960					# Pixel Width of Window
scale = 1				# Conversion pixels to inches (or mm)

location = '/home/jason/RoboticsCourse_3D_Scanner/3D_Scan/data/'
basename = 'camtest'
filetype = '.jpg'

# Capture Loop ---------------------------------------------------------
 
def cleardata():
	folder = location
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception as e:
			print(e)


for scan in range(0,scan_max):
	
	while True:
		cap = cv2.VideoCapture(0)
		okay, frame = cap.read()
		cap.release()
		if okay == False:
			continue
				
		index = str(scan)
		filename = location + basename + index + filetype
		cv2.imwrite(filename, frame)
		time.sleep(.5)
		break
	
	# Feedback	
	print(scan)
	print(filename)
	



# Delete Stored data

#cleardata()
		
	
			
		
		
