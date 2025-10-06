import matplotlib.pyplot as mat
import numpy as np
import time

starting_coordinate_input = input('Starting coordinate (seperated by comma): ')
starting_coordinate = starting_coordinate_input.split(',')

ending_coordinate_input = input('Ending coordinate (seperated by comma): ')
ending_coordinate = ending_coordinate_input.split(',')

line_style_input = input('Enter the line style (1: solid, 2: dashed, 3: dotted): ')
if line_style_input == '1':
    line_style = 'solid'
elif line_style_input == '2':
    line_style = 'dashed'
elif line_style_input == '3':
    line_style = 'dotted'

line_size_input = input('Enter the line size (as 1 being very small and 20 being large): ')
line_size = str(line_size_input)

marker_style_input = input('Enter the marker style (1: dot, 2: star, 3: triangle): ')
if marker_style_input == '1':
    marker_style = 'o'
elif marker_style_input == '2':
    marker_style = '*'
elif marker_style_input == '3':
    marker_style = '^'

xpoints = np.array([starting_coordinate[0], ending_coordinate[0]])
ypoints = np.array([starting_coordinate[1], ending_coordinate[1]])

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

mat.plot(xpoints, ypoints, linestyle=line_style, marker=marker_style, linewidth=line_size)
print('Please check the top right of your screen for your graph')
mat.show()
