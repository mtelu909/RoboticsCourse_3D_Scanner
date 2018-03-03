#!/usr/bin/env python3
# EML 4840 Robot Design
# Florida International University
# Department of Mechanical and Materials Engineering
# Jason Soto <jsoto103@fiu.edu>
# Miami, Spring 2018
 
import cv2 as cv
import time
import numpy as np

cap = cv.VideoCapture('/home/enmar/Desktop/balls03.mp4')

def centroid( mask ):
	M = cv.moments(mask,True)
	m00 = M['m00']
	if m00 == 0:
		x = -100 
		y = -100
	else:
		x = int( M['m10']/m00 )
		y = int( M['m01']/m00 )
	return x,y

def draw(image, centroids, color):
	cv.polylines(image, np.array([centroids],dtype = np.int32), False, color, 3)
	cv.imshow('EML4840: Video', image)
	
def remember(points, point):
	if point[0] <= 0 and point[1] <= 0:
		return points
	if len(points) != 0:
		if points[-1] == point:
			return points
	points.append((x, y))	
	return points
	
c = []
k = []
q = []
	
# MAIN LOOP
while True:
	ret, frame = cap.read()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	
	# YELLOW BALL
	h = 19
	s = 218
	v = 128	
	lower = (h - 10, 100, 100)
	upper = (h + 10, 255, 255)
	
	mask = cv.inRange(hsv, lower, upper)
	mask = cv.erode(mask, None, iterations = 4)
	mask1 = cv.dilate(mask, None, iterations = 4)
	
	x,y = centroid(mask1)
	c = remember(c, (x,y))
	draw(frame, c, (28,172,244))
	
	# GREEN BALL
	h = 50
	s = 155
	v = 90	
	lower = (h - 10, 100, 100)
	upper = (h + 10, 255, 255)
	
	mask = cv.inRange(hsv, lower, upper)
	mask = cv.erode(mask, None, iterations = 4)
	mask2 = cv.dilate(mask, None, iterations = 4)
	
	x,y = centroid(mask2)
	k = remember(k, (x,y))
	draw(frame, k, (34,157,63))
	

	# PINK BALL
	h = 157
	s = 128
	v = 150	
	lower = (h - 10, 100, 100)
	upper = (h + 10, 255, 255)
	
	mask = cv.inRange(hsv, lower, upper)
	mask = cv.erode(mask, None, iterations = 4)
	mask3 = cv.dilate(mask, None, iterations = 4)
	
	x,y = centroid(mask3)
	q = remember(q, (x,y))
	draw(frame, q, (139,108,210))	
	
	# MASK COMBINE
	result = cv.bitwise_and(frame, frame, mask = mask1 + mask2 + mask3)	
	
	
	
# Slow video
	time.sleep(.01)	
	
	
	#cv.imshow('frame', frame)
	#cv.imshow('gray', gray)
	#cv.imshow('hsv', hsv)
	cv.imshow('result', result)
	
	
	if cv.waitKey(1) > -1:
		break
		
cap.release()
cv.destroyAllWindows()


