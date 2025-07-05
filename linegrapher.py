import matplotlib.pyplot as mat
import numpy as np
import time

starting_coordinate_input = input('Starting coordinate (seperated by comma): ')
starting_coordinate = starting_coordinate_input.split(',')

ending_coordinate_input = input('Ending coordinate (seperated by comma): ')
ending_coordinate = ending_coordinate_input.split(',')
xpoints = np.array([starting_coordinate[0], ending_coordinate[0]])
ypoints = np.array([starting_coordinate[1], ending_coordinate[1]])

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

mat.plot(xpoints, ypoints)
print('Please check the top right of your screen for your graph')
mat.show()
