import cv2
# import numpy as np
import time

'''
This is the most basic implementation of reading and displaying two cameras.
REF: http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

Lots of room for optimization:
	1. Leveraging hardware/CUDA optimization
	2. Threading (non-blocking code)
	3. Using multiprocessor (not sure if it'll work with ARMv5l)
'''

fps = 30 #frames per second

# Define camera sources
camera_feed_0 = cv2.VideoCapture(0)
camera_feed_1 = cv2.VideoCapture(1)

while (1):
	# Read camera
	ret0, frame0 = camera_feed_0.read()		#note: in Py you can return multiple variables, #pymagic
	ret1, frame1 = camera_feed_1.read()

	# Display camera feeds seperately
	cv2.imshow('Feed 0', frame0)
	cv2.imshow('Feed 1', frame1)

	# Exit sequence
	if cv2.waitKey(1) & 0xFF == ord('q'):
        break

	# System wait/delay
	time.sleep(1/fps) #in seconds

# End sequence to clean up all elements
camera_feed_0.release()	# without this, we might get the resources still being used errors
camera_feed_1.release()
cv2.destroyAllWindows()