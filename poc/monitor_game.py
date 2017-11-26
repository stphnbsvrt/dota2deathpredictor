from d2dpredictor import game_info
import cv2
import numpy as np

def simplify(image):
    return cv2.inRange(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 128, 255)

#maps
maps = []
#0 is radiant kill, 1 is dire kill
deaths = []

game_old = game_info.get_image()
dire_kills_old = simplify(game_info.get_dire_kills(game_old))
dire_deaths_old = simplify(game_info.get_dire_deaths(game_old))
rad_kills_old = simplify(game_info.get_radiant_kills(game_old))
rad_deaths_old = simplify(game_info.get_radiant_kills(game_old))
square = rad_deaths_old.shape[0] * rad_deaths_old.shape[1]
while(True):

    game_new = game_info.get_image()
    dire_kills_new = simplify(game_info.get_dire_kills(game_new))
    dire_deaths_new = simplify(game_info.get_dire_deaths(game_new))
    rad_kills_new = simplify(game_info.get_radiant_kills(game_new))
    rad_deaths_new = simplify(game_info.get_radiant_deaths(game_new))
    
    dire_err = np.sum((dire_kills_old.astype("float") - dire_kills_new.astype("float")) ** 2) / square
    rad_err = np.sum((rad_deaths_old.astype("float") - rad_deaths_new.astype("float")) ** 2) / square
    if (100 < dire_err) and (100 < rad_err):
        print 'dire kill detected! err = ' + str(dire_err)
        dire_kill_map = game_info.get_map(game_old)
        cv2.imshow('dire kill', dire_kill_map)
        maps.append(dire_kill_map)
        deaths.append(1)
    
    dire_err = np.sum((dire_deaths_old.astype("float") - dire_deaths_new.astype("float")) ** 2) / square
    rad_err = np.sum((rad_kills_old.astype("float") - rad_kills_new.astype("float")) ** 2) / square
    if (100 < dire_err) and (100 < rad_err):
        print 'radiant kill detected! err = ' + str(dire_err)
        radiant_kill_map = game_info.get_map(game_old)
        cv2.imshow('radiant kill', radiant_kill_map)
        maps.append(radiant_kill_map)
        deaths.append(0)
    

    #cv2.imshow('rad_kills', rad_kills_new)
    key = cv2.waitKey(1000)
    
    game_old = game_new
    dire_kills_old = dire_kills_new
    dire_deaths_old = dire_deaths_new
    rad_kills_old = rad_kills_new
    rad_deaths_old = rad_deaths_new
    
    if key != -1:
        print "saving %d maps and %d deaths!" % (len(maps), len(deaths))
        np.save("output_maps", maps)
        np.save("output_deaths", deaths)
        cv2.destroyAllWindows()
        break