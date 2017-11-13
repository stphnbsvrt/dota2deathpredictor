import numpy as np
from PIL import ImageGrab
import PIL
import cv2

def get_map(map_bbox=(10, 810, 270, 1070)):
	map_b, map_g, map_r =  ImageGrab.grab(map_bbox).split()
	map =   np.array(PIL.Image.merge("RGB", (map_r, map_g, map_b)).getdata(),dtype='uint8')\
	.reshape((map_b.size[1],map_b.size[0], 3))
	return map
