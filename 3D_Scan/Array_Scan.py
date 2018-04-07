# DESCRIPTION
# Program to read a laserline and turn it into an array of heights

# Notes:
	# 1)	Make sure Username matches your computer
	# 2)	Double check sleep times and image rendering

# Initializing the Program
import cv2
import time
import numpy as np
import xlsxwriter
#import Rpi.GPIO as GPIO		# Suppressed for run on PC
import os, shutil

# USER INPUTS ----------------------------------------------------------

INPUT_PIN = 4           # Sets our input pin

xcount = 48				# Number of slices
scan_max = 3			# Number of pictures taken

gap = 20				# Pixel Width of slice 
H = 540					# Pixel Height of Window
W = 960					# Pixel Width of Window
zscale = 1				# Conversion pixel height to dist
xscale = 1				# Conversion pixel width to dist
ydist = 1				# Travel increment of scanner

location = '/home/pi/RoboticsCourse_3D_Scanner/3D_Scan/testfiles'
#location = '/home/enmar/RoboticsCourse_3D_Scanner/3D_Scan/testfiles/'
basename = 'laserline'
filetype = '.jpg'

controlrec = 0			# Record images? Yes = 1, No = 0

# Function Setup -------------------------------------------------

def centroid( mask ):
	M = cv2.moments(mask,True)
	m00 = M['m00']
	if m00 == 0:
		x = -100 
		y = -100
	else:
		x = int( M['m10']/m00 )
		y = int( M['m01']/m00 )
	return x,y

def draw(image, centroids, color):
	cv2.polylines(image, np.array([centroids],dtype = np.int32), False, color, 3)
	cv2.imshow('EML4840: Video', image)
	
def remember(points, point):
	if point[0] <= 0 and point[1] <= 0:
		return points
	if len(points) != 0:
		if points[-1] == point:
			return points
	points.append((x, y))	
	return points
	
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

# Capture Loop ---------------------------------------------------------
 
if (controlrec == 1):

	#GPIO.setmode(GPIO.BCM)           # Set's GPIO pins to BCM GPIO numbering
	#GPIO.setup(INPUT_PIN, GPIO.IN)   # Set our input pin to be an input

	cleardata()						  # Deletes Pictures

	for scan in range(0,scan_max):
		
		# Wait for button press
		#while True: 
		#	var = GPIO.input(INPUT_PIN)	
		#	if ( var == True) & (var_old == False):
		#		break	
		#	var_old = var
		#	time.sleep(.01)
		
		# take pic	
		while True:
			cap = cv2.VideoCapture(0)
			okay, frame = cap.read()
			cap.release()
			if okay == False:
				continue	
			index = str(scan)
			filename = location + basename + index + filetype
			cv2.imwrite(filename, frame)
			time.sleep(1)
			break
		
		# Feedback	
		print(scan)
		print(filename)

		
	
			
		
		

# Calculation Loop -----------------------------------------------------


Xmatrix = [[0 for x in range(xcount)] for y in range(scan_max)]
Ymatrix = [[0 for x in range(xcount)] for y in range(scan_max)]
Zmatrix = [[0 for x in range(xcount)] for y in range(scan_max)]

for scan in range(0,scan_max):

	# Setting up Variables	
	index = str(scan)
	filename = location + basename + index + filetype
	
	c = []
	xarr = []
	yarr = []
	zdist = [] 
	
	# Reading the Image
	imS = cv2.imread(filename)
	#imS = cv2.resize(img, (W, H))		
	#cv2.imshow('image',imS) 				# Feedback: Resized image

	for i in range(0,xcount): 
		
		# Slicing Math
		inc = i*gap
		pos1 = -W + inc
		pos2 =  W + gap + inc
		width = W*2
		
		#imS = cv2.resize(img, (W, H))
		cv2.line(imS, (pos1, 1), (pos1, H), (0,0,0), width)
		cv2.line(imS, (pos2, 1), (pos2, H), (0,0,0), width)
		
		#cv2.imshow("Slice", imS)			# Feedback: Slicing Animation
		
		# Masking Process
		hsv = cv2.cvtColor(imS, cv2.COLOR_BGR2HSV)
		h = 225 * 176/255
		s = 240
		v = 120
		lower = (h - 10, 100, 100)
		upper = (h + 15, 255, 255)
		mask = cv2.inRange(hsv, lower, upper)
		for j in range(1):
			mask = cv2.erode(mask, None, iterations = 1)
			mask = cv2.dilate(mask, None, iterations = 1)
		
		#cv2.imshow('mask', mask)			# Feedback: Masking Animation
		
		x,y = centroid(mask)
		c = remember(c, (x,y))
		draw(imS, c, (28,172,244))			# Feedback: Drawing Animation
		
		xarr.append(x)
		yarr.append(y)
		
		time.sleep(0.001)
		
		if cv2.waitKey(1) > -1:
			break

	# Processing heights (Z)
	yarr = np.array(yarr)
	
	for i in range(0,xcount):
		if yarr[i] < 0:
			yarr[i] = H
	
	
	zpix = H - yarr 
	jump = zpix[0]
	zpix = zpix - jump

	for i in range(0,xcount):
		if zpix[i] < 0:
			zpix[i] = 0

	zdist = zpix * zscale

			
	# Building the matrix
		
	Xmatrix[scan][:] = np.array(range(xcount)) * gap * xscale
	Ymatrix[scan][:] = scan * np.array([1 for x in range(xcount)]) * ydist
	Zmatrix[scan][:] = zdist
	 

	# Feedback
	print('Index =', scan)
	print()
	print('c =', c)
	print()
	print('xarr = ', xarr)	
	print()
	print('yarr = ', yarr)
	print()
	print('zdist = ', zdist)
	print()
	#print('kek =', kek)
	print()

print('Xmatrix = ', Xmatrix)
print()
print('Ymatrix = ', Ymatrix)
print()
print('Zmatrix = ', Zmatrix)

# Exporting data -------------------------------------------------------



workbook = xlsxwriter.Workbook('Matrices.xlsx')
worksheet = workbook.add_worksheet('Zmatrix')

for i in range(0,scan_max):
	for j in range(0, xcount):
		worksheet.write(i, j, Zmatrix[i][j])
		
worksheet = workbook.add_worksheet('Ymatrix')

for i in range(0,scan_max):
	for j in range(0, xcount):
		worksheet.write(i, j, Ymatrix[i][j])
		
worksheet = workbook.add_worksheet('Xmatrix')

for i in range(0,scan_max):
	for j in range(0, xcount):
		worksheet.write(i, j, Xmatrix[i][j])

workbook.close()


# Hold Image untill Key-Press
cv2.waitKey(0)
cv2.destroyAllWindows()

# End of Program
