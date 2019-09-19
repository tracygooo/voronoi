#!/usr/bin/env python3

import pyautogui, sys
import numpy as np
import time
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

print('Press Ctrl-C to quit.')
data = []
i = 0
try:
    while True:
        time.sleep(3)
        data.append( pyautogui.position() )
        positionStr = 'X: ' + str( data[ i ][0]).rjust(4) + ' Y: ' + str(data[ i ][1]).rjust(4) + '\n'
        print( positionStr )
        #print(positionStr, end='')
        #print('\b' * len(positionStr), end='', flush=True)
        i += 1
except KeyboardInterrupt:
    print('\n')

data = np.array( data )

vor = Voronoi( data )
voronoi_plot_2d( vor )
plt.savefig( 'vor.png' , format = 'png' , dpi = 300 )
plt.show()
