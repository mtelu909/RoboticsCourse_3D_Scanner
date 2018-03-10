# DESCRIPTION
# Program to read a laserline and turn it into an array of heights
# (Incomplete)

# Initializing the Program
import cv2
import time
import numpy as np

j = 1


location = '/home/enmar/RoboticsCourse_3D_Scanner/3D_Scan/'
basename = 'laserline'
count = str(j)
filetype = '.jpg'

filename = location + basename + count + filetype

img = cv2.imread(filename)
imS = cv2.resize(img, (960, 540))		
cv2.imshow('image',imS) 				# Feedback: Resized image

print(filename)

# Hold Image untill Key-Press
cv2.waitKey(0)
cv2.destroyAllWindows()

# End of Program
