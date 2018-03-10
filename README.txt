This README breaks down the branches of this project.


MASTER:

This Project aims to build a 3D scanner capable of converting an image to a matrix of heights.

	Breakdown:

	1) Startup: 	Upon being turned on the machine heads to the "Zero" position

	2) Adjustment: 	Camera and laser are turned on and adjustments can be made to align camera 				and laser on screen.

	3) Calibration: Run the calibration script which scans a small region where an cubic 				object of known dimensions is placed.

	4) Scanning: 	Program sweeps the machine across the scan area and records images at 				certain known distance intervals.

	5) Processing:  Loads the stored images one by one and obtains the array of Z-heights and
			X-dists as matrices

	6) Post-Processing:	Turns matrix into a visual representation (surface,solid, etc.)


Motor-Controller:

Here The goal is to create an Arduino code capapble of controlling the distance of the can pillar usinng gearing math and/or ultrasonic sensor input.


ScanArray:

In this branch we shall attempt to break down a single laser line into an array of heights.
To do this we shall use the laserline.jpg and Array_Scan.py code included in the 3D_Scan Folder.



	Notes:

	- To run the code on your home computer you will have to change the filepath of the 		  laserline your are trying to process. The computers "username" is probably different 		  than the name attached.


