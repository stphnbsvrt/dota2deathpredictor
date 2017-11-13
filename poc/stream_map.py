from d2dpredictor import getmap
import cv2
import json

maps = []
deaths = []
while(True):

	cv2.imshow('window', getmap.get_map())
	key = cv2.waitKey(25)
	if key != -1:
		cv2.destroyAllWindows()
		break
