import numpy as np
from PIL import ImageGrab
import PIL
import cv2

def get_map(image):
    return image[810:1070, 10:270]

def get_radiant_kills(image):
    return image[80:400, 440:480]
	
def get_radiant_deaths(image):
    return image[80:400, 480:520]	

def get_dire_kills(image):
    return image[400:700, 440:480]
	
def get_dire_deaths(image):
    return image[400:700, 480:520]
	
def get_image():
	b, g, r =  ImageGrab.grab((0, 0, 550, 1080)).split()
	img =   np.array(PIL.Image.merge("RGB", (r, g, b)).getdata(),dtype='uint8')\
	.reshape((b.size[1],b.size[0], 3))
	return img
