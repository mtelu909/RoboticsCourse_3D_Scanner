#DESCRIPTION
#Program to read a laserline and turn it into an array of heights
#(Incomplete)

#Initializing the Program
import cv2
import time
import numpy as np

#Setting up Functions
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

#Setting up Variables	
c = []
xarr = []
yarr = []

#Reading the Image
img = cv2.imread('/home/jason/RoboticsCourse_3D_Scanner/3D_Scan/laserline.jpg')

#Display Image
imS = cv2.resize(img, (960, 540))		
#cv2.imshow('image',imS) 				#Feedback: Resized image

#Masking With lines
#Desc:	Draw a vertical line and give it a desired width. Results in
#		a rectangular box that is filled in.
cv2.line(imS, (100, 1), (100, 540), (0,0,0), 50)



#cv2.imshow("line", imS)					#Feedback: Masking line

xcount = 48
gap = 20

for i in range(0,xcount): 
	
	#Slicing Math
	inc = i*gap
	pos1 = -960 + inc
	pos2 =  960 + gap + inc
	width = 960*2
	
	imS = cv2.resize(img, (960, 540))
	cv2.line(imS, (pos1, 1), (pos1, 540), (0,0,0), width)
	cv2.line(imS, (pos2, 1), (pos2, 540), (0,0,0), width)
	
	#cv2.imshow("Slice", imS)				#Feedback: Slicing Animation
	
	#Masking Process
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
	
	cv2.imshow('mask', mask)				#Feedback: Masking Animation
	
	x,y = centroid(mask)
	c = remember(c, (x,y))
	draw(imS, c, (28,172,244))				#Feedback: Drawing Animation
	
	xarr.append(x)
	yarr.append(y)
	
	time.sleep(0.1)
	
	if cv2.waitKey(1) > -1:
		break

print('c =', c)
print()
print('xarr = ', xarr)	
print()
print('yarr = ', yarr)





#Hold Image untill Key-Press
cv2.waitKey(0)
cv2.destroyAllWindows()

# NOTE1: 	We can also try cropping the original image to try and save
#			processing time maybe? Will definitely save storage space
#			...I think. 

#			import cv2
#			img = cv2.imread("lenna.png")
#			crop_img = img[y:y+h, x:x+w]
#			cv2.imshow("cropped", crop_img)
#			cv2.waitKey(0)
