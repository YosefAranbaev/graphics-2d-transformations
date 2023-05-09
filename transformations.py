import numpy as np
import math
def scale_shape_15(screen, obj):
    prev_figure_center_point = get_center(obj)

    print(obj)
    scale_factor = 1.5
    new_obj = {}
    for shape_type, shapes in obj.items():
        new_shapes = []
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                color, x1, y1, x2, y2 = shape
                cx, cy = 400, 300
                dx, dy = x1 - cx, y1 - cy
                new_dx = int(dx * scale_factor)
                new_dy = int(dy * scale_factor)
                new_x1, new_y1 = cx + new_dx, cy + new_dy
                
                dx, dy = x2 - cx, y2 - cy
                new_dx2 = int(dx * scale_factor)
                new_dy2 = int(dy * scale_factor)
                new_x2, new_y2 = cx + new_dx2, cy + new_dy2
                
                new_shapes.append((color, new_x1, new_y1, new_x2, new_y2))
            elif shape_type == 'circle':
                color, x, y, radius = shape
                cx, cy = 400, 300
                dx, dy = x - cx, y - cy
                new_x = int(dx * scale_factor) + cx
                new_y = int(dy * scale_factor) + cy
                new_radius = int(radius * scale_factor)
                new_shapes.append((color, new_x, new_y, new_radius))
            elif shape_type == 'curve':
                color, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                cx, cy = 400, 300
                
                dx, dy = start_x - cx, start_y - cy
                new_dx = int(dx * scale_factor)
                new_dy = int(dy * scale_factor)
                new_start_x, new_start_y = cx + new_dx, cy + new_dy
                
                dx, dy = end_x - cx, end_y - cy
                new_dx2 = int(dx * scale_factor)
                new_dy2 = int(dy * scale_factor)
                new_end_x, new_end_y = cx + new_dx2, cy + new_dy2
                
                dx, dy = cp_x - cx, cp_y - cy
                new_dx3 = int(dx * scale_factor)
                new_dy3 = int(dy * scale_factor)
                new_cp_x, new_cp_y = cx + new_dx3, cy + new_dy3
                
                new_shapes.append((color, new_start_x, new_start_y, new_end_x, new_end_y, new_cp_x, new_cp_y))

        new_obj[shape_type] = new_shapes

    # TODO: move the shape to the center
    print(new_obj)
    # return new_obj
    # move the figure back to the previous center point
    new_figure_center_point = get_center(new_obj)
    dx = prev_figure_center_point[0] - new_figure_center_point[0]
    dy = prev_figure_center_point[1] - new_figure_center_point[1]

    return move_shape(new_obj, dx, dy)


def rotate_shape_45(screen, obj):
    prev_figure_center_point = get_center(obj)
    print(obj)
    angle = math.pi/4
    new_obj = {}
    for shape_type, shapes in obj.items():
        new_shapes = []
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                color, x1, y1, x2, y2 = shape
                cx, cy = 400, 300
                dx, dy = x1 - cx, y1 - cy
                new_dx = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_x1, new_y1 = cx + new_dx, cy + new_dy
                
                dx, dy = x2 - cx, y2 - cy
                new_dx2 = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy2 = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_x2, new_y2 = cx + new_dx2, cy + new_dy2
                
                new_shapes.append((color, new_x1, new_y1, new_x2, new_y2))
            elif shape_type == 'circle':
                color, x, y, radius = shape
                cx, cy = 400, 300
                dx, dy = x - cx, y - cy
                new_dx = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_x, new_y = cx + new_dx, cy + new_dy
                new_shapes.append((color, new_x, new_y, radius))
            elif shape_type == 'curve':
                color, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                cx, cy = 400, 300
                
                dx, dy = start_x - cx, start_y - cy
                new_dx = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_start_x, new_start_y = cx + new_dx, cy + new_dy
                
                dx, dy = end_x - cx, end_y - cy
                new_dx2 = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy2 = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_end_x, new_end_y = cx + new_dx2, cy + new_dy2
                
                dx, dy = cp_x - cx, cp_y - cy
                new_dx3 = int(dx * math.cos(angle) - dy * math.sin(angle))
                new_dy3 = int(dx * math.sin(angle) + dy * math.cos(angle))
                new_cp_x, new_cp_y = cx + new_dx3, cy + new_dy3
                
                new_shapes.append((color, new_start_x, new_start_y, new_end_x, new_end_y, new_cp_x, new_cp_y))

        new_obj[shape_type] = new_shapes

    # move the figure back to the previous center point
    new_figure_center_point = get_center(new_obj)
    dx = prev_figure_center_point[0] - new_figure_center_point[0]
    dy = prev_figure_center_point[1] - new_figure_center_point[1]

    return move_shape(new_obj, dx, dy)

import numpy as np
from shape_utils import get_biggest_x, get_biggest_y, get_center

def move_shape(shape_dictionary, dx, dy):
    new_shape_dictionary = {}
    for key, value in shape_dictionary.items():
        new_value = []
        for shape in value:
            new_shape = []
            color = shape[0]
            if key == 'line':
                x1, y1, x2, y2 = shape[1:]
                new_shape = [color, x1 + dx, y1 + dy, x2 + dx, y2 + dy]
            elif key == 'circle':
                x, y, r = shape[1:]
                new_shape = [color, x + dx, y + dy, r]
            elif key == 'curve':
                start_x, start_y, end_x, end_y, cp_x, cp_y = shape[1:]
                new_shape = [color, start_x + dx, start_y + dy, end_x + dx, end_y + dy, cp_x + dx, cp_y + dy]
            new_value.append(new_shape)
        new_shape_dictionary[key] = new_value

    return new_shape_dictionary

def mirror_shape_x(shape_dictionary):
    prev_figure_center_point = get_center(shape_dictionary)

    mirror_axis_x = get_biggest_x(shape_dictionary)
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

    # move the figure back to the previous center point
    new_figure_center_point = get_center(shape_dictionary)
    dx = prev_figure_center_point[0] - new_figure_center_point[0]
    dy = prev_figure_center_point[1] - new_figure_center_point[1]

    return move_shape(shape_dictionary, dx, dy)  

def mirror_shape_y(shape_dictionary):
    prev_figure_center_point = get_center(shape_dictionary)

    mirror_axis_y = get_biggest_y(shape_dictionary)
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

    # move the figure back to the previous center point
    new_figure_center_point = get_center(shape_dictionary)
    dx = prev_figure_center_point[0] - new_figure_center_point[0]
    dy = prev_figure_center_point[1] - new_figure_center_point[1]

    return move_shape(shape_dictionary, dx, dy)  

def shear_shape(shape_dictionary, shear_const_x=0.1, shear_const_y=0.1):
    prev_figure_center_point = get_center(shape_dictionary)

    new_shape_dictionary = {}
    for key, value in shape_dictionary.items():
        new_value = []
        for shape in value:
            new_shape = []
            color = shape[0]
            if key == 'line':
                x1, y1, x2, y2 = shape[1:]
                x1 += shear_const_x * y1
                y1 += shear_const_y * x1
                x2 += shear_const_x * y2
                y2 += shear_const_y * x2
                new_shape = [color, x1, y1, x2, y2]
            elif key == 'circle':
                x, y, r = shape[1:]
                x += shear_const_x * y
                y += shear_const_y * x
                new_shape = [color, x, y, r]
            elif key == 'curve':
                start_x, start_y, end_x, end_y, cp_x, cp_y = shape[1:]
                start_x += shear_const_x * start_y
                end_x += shear_const_x * end_y
                cp_x += shear_const_x * cp_y
                start_y += shear_const_y * start_x
                end_y += shear_const_y * end_x
                cp_y += shear_const_y * cp_x
                new_shape = [color, start_x, start_y, end_x, end_y, cp_x, cp_y]
            new_value.append(new_shape)
        new_shape_dictionary[key] = new_value

    # move the figure back to the previous center point
    new_figure_center_point = get_center(new_shape_dictionary)
    dx = prev_figure_center_point[0] - new_figure_center_point[0]
    dy = prev_figure_center_point[1] - new_figure_center_point[1]

    return move_shape(new_shape_dictionary, dx, dy)