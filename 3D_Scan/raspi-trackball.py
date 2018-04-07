# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
 
def centroid( mask ):
	M = cv.moments(mask,True)
	m00 = M['m00']
	if m00 == 0: # Ops, don't want divide by zero!
		x = -100 
		y = -100
	else:
		x = int( M['m10']/m00 )
		y = int( M['m01']/m00 )
	return x,y



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	
	
	hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	
	#color = 46
	color = 188 * (176/356) 		# blue
	#color = 62 * (176/356)			#working Yellow
	#color = 3 * (176/356)
	
	colorLower = (color - 20, 80, 80)
	colorUpper = (color + 20, 255, 255)
	
	mask = cv.inRange(hsv, colorLower, colorUpper)
	mask = cv.erode(mask, None, iterations = 4)
	mask = cv.dilate(mask, None, iterations = 4)
	
	x,y = centroid(mask)
	
	cv.circle(image, (x,y), 10, (0,0,255), 10)
	
	#feedback
	cv.imshow('EML4840: Video', image)
	#cv.imshow('EML4840: Mask', mask)
	
	
	key = cv.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
