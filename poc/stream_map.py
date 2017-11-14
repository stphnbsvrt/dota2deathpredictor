from d2dpredictor import game_info
import cv2
import json

maps = []
deaths = []
while(True):

	image = game_info.get_image()
	cv2.imshow('window', game_info.get_map(image))
	key = cv2.waitKey(25)
	if key != -1:
		cv2.destroyAllWindows()
		break
