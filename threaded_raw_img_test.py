import cv2
# import numpy as np
# import time
import threading

'''
Using a THREADED example of camera capture using X cameras
REF: https://docs.python.org/2/library/threading.html#timer-objects

Note: not sure of threading is ARM compatible. This differs from multi-threading.
'''

def read_and_display_frame(camera_feed_index = -1):
	if camera_feed_index is not -1:
		ret0, frame = camera_feed[camera_feed_index]
		cv2.imshow('Feed ' + camera_feed_index, camera_feed[camera_feed_index])

fps = 30 #frames per second

# Define multiple camera sources
camera_feed = [cv2.VideoCapture(0), cv2.VideoCapture(1)]

# Create a thread for each feed that's called 30 times/sec (based on fps)
camera_thread = []
for i in range(len(camera_feed)):
	#TODO: I'm not sure if this works like it should, it should call read_and_display_frame with the k-args in {}
	camera_thread.append(threading.Timer(1/fps, read_and_display_frame, {camera_feed_index=i})) 
	camera_thread[i].start()

while (1):
	# Exit sequence
	# if cv2.waitKey(1) & 0xFF == ord('q'):
 #        break
 	if cv2.waitKey(1) == 27:
		break

# End sequence to clean up all elements
for i in range(len(camera_feed)):
	camera_thread[i].cancel()
	camera_feed[i].release()
cv2.destroyAllWindows()