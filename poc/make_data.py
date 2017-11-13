from d2dpredictor import getmap
import cv2
import numpy
import json

maps = []
deaths = []
print 'resuming in 5 seconds'
cv2.waitKey(5)
while(True):
    map = getmap.get_map()
    cv2.imshow('window', map)
    key = cv2.waitKey(50)

    if key & 0xFF == ord('d'):
        maps.append(map)
        deaths.append(1)
        print 'saved image as death'
    elif key & 0xfF == ord('g'):
        maps.append(map)
        deaths.append(0)
        print 'saved image as good'
    elif key & 0xFF == ord('q'):  
        numpy.save('output_maps.dat', maps)
        with open('output_deaths.dat', 'w') as f:
            json.dump(deaths, f)
        break
