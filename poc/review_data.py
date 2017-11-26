import cv2
import numpy as np

#maps
maps = np.load("output_maps.npy")
#0 is radiant kill, 1 is dire kill
deaths = np.load("output_deaths.npy")

#training maps
try:
    training_maps = np.load("training_maps.npy")
    training_deaths = np.load("training_deaths.npy")
except:
    pass

if(len(deaths) != len(maps)):
    print "Lengths don't match! Data is bad!"

for i in xrange(0, len(maps)):
    if(0 == deaths[i]):
        cv2.imshow('radiant kill', maps[i])
    elif(1 == deaths[i]):
        cv2.imshow('dire kill', maps[i])
    else:
        print "Data isn't binary! Data is bad!"
    
    
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        raise RuntimeError("not saving updated training data!")
    elif key & 0xFF != ord('n'):
        try:
            training_maps = np.append(training_maps, [maps[i]], 0)
            training_deaths = np.append(training_deaths, [deaths[i]], 0)
        except:
            training_maps = [maps[i]]
            training_deaths = [deaths[i]]

print "saving updated training data"
np.save("training_maps", training_maps)
np.save("training_deaths", training_deaths)
