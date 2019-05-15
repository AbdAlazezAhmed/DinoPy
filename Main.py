import numpy as np
from grabscreen import grab_screen
from directkeys import Up , Down , PressKey , ReleaseKey
import time
import cv2

def main () :
    while(True) :
        #Resize the game window to about less than quarter of the screen at 1920*1080 resolution
        screen = cv2.cvtColor(grab_screen(region=(0,0,700,500)),cv2.COLOR_RGB2GRAY)
        
        i = 0 # submission for the jump region
        z = 0 # submission for the dock region
        j = 250 # start of jump region
        k = 180 # start of dock region

        while j < 340 :
            i = i + screen[337, j]
            j = j+1
        while k < 230:
            z = z + screen[337, k]
            k = k+1
            
        upR = i/(340-250) # the mean of average for the jump region
        DownR = z / (290-180) # the mean of average for the dock region
        if screen[499 , 699] > 127 :
            if upR<244: # Jump
                PressKey(Up)
                print( upR)
            elif screen[306,280]<127  : #dock
                PressKey(Down)
                print( screen[297,292])
            
            elif DownR<244: # stop jumping
                ReleaseKey(Up)
                print( DownR)
            elif DownR>250: # go down by docking
                PressKey(Down)
                print( DownR)
            if screen[310,150]<127  : # stop going down
                ReleaseKey(Down)
                print( screen[297,292])
            
        else :
            if upR>22 : # Jump
                PressKey(Up)
                print( screen[337,294])
            elif screen[306,280]>127 : #dock
                PressKey(Down)
                print( screen[297,292])

            elif DownR>22: # stop jumping
                ReleaseKey(Up)
                print( DownR)
            elif DownR<22: # go down by docking
                PressKey(Down)
                print( DownR)
            if screen[310,150]>127  :  # stop going down
                ReleaseKey(Down)
                print( screen[297,292])


main()
