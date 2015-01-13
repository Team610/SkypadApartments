import cv2
import time
import numpy as np

fps = 30 #frames per second

camera_feed_0 = cv2.VideoCapture(0)
camera_feed_1 = cv2.VideoCapture(0)

while (1):
	#Read camera
	ret0, frame0 = camera_feed_0()
	ret1, frame1 = camera_feed_1()

	#System wait/delay
	time.sleep(1/fps) #in seconds