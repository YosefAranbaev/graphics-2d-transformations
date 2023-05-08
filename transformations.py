import numpy as np

def mirror_shape_y(shape_dictionary):
    mirror_axis_x = _get_biggest_x(shape_dictionary)
    for shape_type, shapes in shape_dictionary.items():
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                _, x1, y1, x2, y2 = shape
                shape_dictionary[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - x1), y1, mirror_axis_x + (mirror_axis_x - x2), y2)
            elif shape_type == 'circle':
                _, x, y, radius = shape
                shape_dictionary[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - x), y, radius)
            elif shape_type == 'curve':
                _, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                shape_dictionary[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - start_x), start_y, mirror_axis_x + (mirror_axis_x - end_x), end_y, mirror_axis_x + (mirror_axis_x - cp_x), cp_y)

    # TODO: move the shape left by the width
    return shape_dictionary  

def mirror_shape_x(shape_dictionary):
    mirror_axis_y = _get_biggest_y(shape_dictionary)
    for shape_type, shapes in shape_dictionary.items():
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                _, x1, y1, x2, y2 = shape
                shape_dictionary[shape_type][i] = (_, x1, mirror_axis_y + (mirror_axis_y - y1), x2, mirror_axis_y + (mirror_axis_y - y2))
            elif shape_type == 'circle':
                _, x, y, radius = shape
                shape_dictionary[shape_type][i] = (_, x, mirror_axis_y + (mirror_axis_y - y), radius)
            elif shape_type == 'curve':
                _, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                shape_dictionary[shape_type][i] = (_, start_x, mirror_axis_y + (mirror_axis_y - start_y), end_x, mirror_axis_y + (mirror_axis_y - end_y), cp_x, mirror_axis_y + (mirror_axis_y - cp_y))

    # TODO: move the shape up by the height
    return shape_dictionary

def shear_shape(shape_dictionary, shear_const=1, axis='x'):
    # TODO: make it work by mouse dragging
    new_shape_dictionary = {}
    current_center_x, current_center_y = _get_center(shape_dictionary)
    for key, value in shape_dictionary.items():
        new_value = []
        for shape in value:
            new_shape = []
            color = shape[0]
            if key == 'line':
                x1, y1, x2, y2 = shape[1:]
                if axis == 'x':
                    x1 += shear_const * y1
                    x2 += shear_const * y2
                elif axis == 'y':
                    y1 += shear_const * x1
                    y2 += shear_const * x2
                new_shape = [color, x1, y1, x2, y2]
            elif key == 'circle':
                x, y, r = shape[1:]
                if axis == 'x':
                    x += shear_const * y
                elif axis == 'y':
                    y += shear_const * x
                new_shape = [color, x, y, r]
            elif key == 'curve':
                start_x, start_y, end_x, end_y, cp_x, cp_y = shape[1:]
                if axis == 'x':
                    start_x += shear_const * start_y
                    end_x += shear_const * end_y
                    cp_x += shear_const * cp_y
                elif axis == 'y':
                    start_y += shear_const * start_x
                    end_y += shear_const * end_x
                    cp_y += shear_const * cp_x
                new_shape = [color, start_x, start_y, end_x, end_y, cp_x, cp_y]
            new_value.append(new_shape)
        new_shape_dictionary[key] = new_value

    # Move the shape to the initial center
    new_center_x, new_center_y = _get_center(shape_dictionary)
    dx = current_center_x - new_center_x
    dy = current_center_y - new_center_y
    for key, value in new_shape_dictionary.items():
        for shape in value:
            if key == 'line':
                shape[1] += dx
                shape[3] += dx
                shape[2] += dy
                shape[4] += dy
            elif key == 'circle':
                shape[1] += dx
                shape[2] += dy
            elif key == 'curve':
                shape[1] += dx
                shape[3] += dx
                shape[5] += dx
                shape[2] += dy
                shape[4] += dy
                shape[6] += dy

    return new_shape_dictionary

def _get_biggest_x(shape_dictionary):
    biggest_x = 0
    for shape_type in shape_dictionary:
        for shape in shape_dictionary[shape_type]:
            if shape_type == 'line':
                _, x1, _, x2, _ = shape
                if x1 > biggest_x:
                    biggest_x = x1
                if x2 > biggest_x:
                    biggest_x = x2
            elif shape_type == 'circle':
                _, x, _, radius = shape
                if x + radius > biggest_x:
                    biggest_x = x + radius
            elif shape_type == 'curve':
                _, start_x, _, end_x, _, cp_x, _ = shape
                if start_x > biggest_x:
                    biggest_x = start_x
                if end_x > biggest_x:
                    biggest_x = end_x
    return biggest_x

def _get_biggest_y(shape_dictionary):
    biggest_y = 0
    for shape_type in shape_dictionary:
        for shape in shape_dictionary[shape_type]:
            if shape_type == 'line':
                _, _, y1, _, y2 = shape
                if y1 > biggest_y:
                    biggest_y = y1
                if y2 > biggest_y:
                    biggest_y = y2
            elif shape_type == 'circle':
                _, _, y, radius = shape
                if y + radius > biggest_y:
                    biggest_y = y + radius
            elif shape_type == 'curve':
                _, _, start_y, _, end_y, _, cp_y = shape
                if start_y > biggest_y:
                    biggest_y = start_y
                if end_y > biggest_y:
                    biggest_y = end_y
                if cp_y > biggest_y:
                    biggest_y = cp_y
    return biggest_y

def _get_center(shape_dictionary):
    x_total = 0
    y_total = 0
    count = 0
    center_x = center_y = 0
    # iterate through lines
    for line in shape_dictionary['line']:
        x_total += (line[1] + line[3])/2
        y_total += (line[2] + line[4])/2
        count += 1

    # iterate through circles
    for circle in shape_dictionary['circle']:
        x_total += circle[1]
        y_total += circle[2]
        count += 1

    # iterate through curves
    for curve in shape_dictionary['curve']:
        x_total += (curve[1] + curve[3] + curve[5])/3
        y_total += (curve[2] + curve[4] + curve[6])/3
        count += 1

    # calculate the average of the centers
    if(count > 0):
        center_x = x_total / count
        center_y = y_total / count

    return (center_x, center_y)

