import matplotlib.pyplot as mat
import numpy as num

def line_graph():
    starting_coordinate_input = input('Enter the starting x coordinates (x, x): ')
    starting_coordinate = starting_coordinate_input.split(',')

    ending_coordinate_input = input('Enter the starting y coordinates (y, y): ')
    ending_coordinate = ending_coordinate_input.split(',')

    xpoints = num.array([starting_coordinate[0], ending_coordinate[0]])
    ypoints = num.array([starting_coordinate[1], ending_coordinate[1]])

    marker = input('Enter the line marker: ')
    line_color = input('Enter the line color (r, g, b): ')
    linewidth = int(input('Enter the line width (1 is small and 20 is big): '))
    linestyle = input('Enter the line style (1: solid, 2: dashed, 3: dotted): ')
    if linestyle == '1':
        line_style = '-'
    elif linestyle == '2':
        line_style = '--'
    elif linestyle == '3':
        line_style = ':'

    mat.plot(xpoints, ypoints, marker=marker, color=line_color, linewidth=linewidth, linestyle=line_style)
    mat.show()

def bar_graph():
    x_axis_labels = input('Enter the x-axis labels (comma separated): ')
    x_axis_labels = x_axis_labels.split(',')

    y_axis_values = input('Enter the y-axis values (comma separated): ')
    y_axis_values = y_axis_values.split(',')
    mat.bar(x_axis_labels, y_axis_values)
    mat.show()

def histogram():
    x_axis_values = input('Enter the x-axis values (comma separated): ')
    x_axis_values = x_axis_values.split(',')
    mat.hist(x_axis_values)
    mat.show()

def pie_chart():
    pie_chart_values = input('Enter the values for the pie chart (comma separated): ')
    pie_chart_values = pie_chart_values.split(',')
    labels = [pie_chart_values[i] for i in range(len(pie_chart_values))]
    mat.pie(pie_chart_values, labels=labels)
    mat.show()


graph_choice = input('Make a (l)ine, (b)ar graph, (h)istogram, or (p)ie chard? ')
if graph_choice == 'l':
    line_graph()
elif graph_choice == 'b':
    bar_graph()
elif graph_choice == 'h':
    histogram()
elif graph_choice == 'p':
    pie_chart()