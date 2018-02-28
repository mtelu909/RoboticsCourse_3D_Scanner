#DESCRIPTION
#Program to read a laserline and turn it into an array of heights
#(Incomplete)

#Initializing the Program
import cv2
import time
import numpy as np

#Reading the Image
img = cv2.imread('/home/jason/Desktop/laserline.jpg')

#Display Image
imS = cv2.resize(img, (960, 540))		
cv2.imshow('image',imS) 				#Feedback: show resized image

#Masking With lines
#Desc:	Draw a vertical line and give it a desired width. Results in
#		a rectangular box that is filled in.
cv2.line(imS, (100, 1), (100, 540), (0,0,0), 50)



cv2.imshow("lalala", imS)				#Feedback: One Masking line

for i in range(1,10):
	inc = i*50
	imS = cv2.resize(img, (960, 540))
	cv2.line(imS, (100+inc, 1), (100+inc, 540), (0,0,0), 50)
	cv2.line(imS, (200+inc, 1), (200+inc, 540), (0,0,0), 50)
	
	time.sleep(2)
	cv2.imshow("mask", imS)				#Feedback: Masking Animation
	if cv2.waitKey(1) > -1:
		break

	






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
