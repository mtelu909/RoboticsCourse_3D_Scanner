# DESCRIPTION
# Program to read a laserline and turn it into an array of heights
# (Incomplete)

# Initializing the Program
import cv2
import time
import numpy as np
import os, shutil
import xlsxwriter

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
 


workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

array = [['a1', 'a2', 'a3'],
         ['a4', 'a5', 'a6'],
         ['a7', 'a8', 'a9'],
         ['a10', 'a11', 'a12', 'a13', 'a14']]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()	

print(array)


# Delete Stored data

#cleardata()
		
	
			
		
		
