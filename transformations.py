import numpy as np
import math
def scale_shape_15(screen, obj):
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
    return new_obj


def rotate_shape_45(screen, obj):
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

    # TODO: move the shape to the center
    print(new_obj)
    return new_obj



# def mirror_shape_x(screen, obj):
#     mirror_axis_angle = -45  # angle of mirror axis in degrees
#     mirror_axis_x, mirror_axis_y = screen[0] // 2, screen[1] // 2  # center of the screen

#     # Step 1: rotate the shape
#     obj = rotation(obj, mirror_axis_angle)

#     # Step 2: mirror the shape along the x-axis
#     for shape_type, shapes in obj.items():
#         for i, shape in enumerate(shapes):
#             if shape_type == 'line':
#                 _, x1, y1, x2, y2 = shape
#                 obj[shape_type][i] = (_, x1, 2 * mirror_axis_y - y1, x2, 2 * mirror_axis_y - y2)
#             elif shape_type == 'circle':
#                 _, x, y, radius = shape
#                 obj[shape_type][i] = (_, x, 2 * mirror_axis_y - y, radius)
#             elif shape_type == 'curve':
#                 _, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
#                 obj[shape_type][i] = (_, start_x, 2 * mirror_axis_y - start_y, end_x, 2 * mirror_axis_y - end_y, cp_x, 2 * mirror_axis_y - cp_y)

#     # Step 3: rotate the shape back
#     obj = rotation(obj, -mirror_axis_angle)

#     return obj

def mirror_shape_x(screen, obj):
    mirror_axis_x = _get_biggest_x(obj)
    for shape_type, shapes in obj.items():
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                _, x1, y1, x2, y2 = shape
                obj[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - x1), y1, mirror_axis_x + (mirror_axis_x - x2), y2)
            elif shape_type == 'circle':
                _, x, y, radius = shape
                obj[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - x), y, radius)
            elif shape_type == 'curve':
                _, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                obj[shape_type][i] = (_, mirror_axis_x + (mirror_axis_x - start_x), start_y, mirror_axis_x + (mirror_axis_x - end_x), end_y, mirror_axis_x + (mirror_axis_x - cp_x), cp_y)

    # TODO: move the shape left by the width
    return obj  

def mirror_shape_y(screen, obj):
    mirror_axis_y = _get_biggest_y(obj)
    for shape_type, shapes in obj.items():
        for i, shape in enumerate(shapes):
            if shape_type == 'line':
                _, x1, y1, x2, y2 = shape
                obj[shape_type][i] = (_, x1, mirror_axis_y + (mirror_axis_y - y1), x2, mirror_axis_y + (mirror_axis_y - y2))
            elif shape_type == 'circle':
                _, x, y, radius = shape
                obj[shape_type][i] = (_, x, mirror_axis_y + (mirror_axis_y - y), radius)
            elif shape_type == 'curve':
                _, start_x, start_y, end_x, end_y, cp_x, cp_y = shape
                obj[shape_type][i] = (_, start_x, mirror_axis_y + (mirror_axis_y - start_y), end_x, mirror_axis_y + (mirror_axis_y - end_y), cp_x, mirror_axis_y + (mirror_axis_y - cp_y))

    # TODO: move the shape up by the height
    print(obj)
    return obj

def shear_shape(screen, obj, shear_const=1, axis='x'):
    # TODO: make it work by mouse dragging
    new_obj = {}
    current_center_x, current_center_y = get_center(obj)
    for key, value in obj.items():
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
        new_obj[key] = new_value

    # Move the shape to the initial center
    new_center_x, new_center_y = get_center(obj)
    dx = current_center_x - new_center_x
    dy = current_center_y - new_center_y
    for key, value in new_obj.items():
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

    return new_obj

def _get_biggest_x(obj):
    biggest_x = 0
    for shape_type in obj:
        for shape in obj[shape_type]:
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

def _get_biggest_y(obj):
    biggest_y = 0
    for shape_type in obj:
        for shape in obj[shape_type]:
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

def get_center(obj):
    x_total = 0
    y_total = 0
    count = 0
    center_x = center_y = 0
    # iterate through lines
    for line in obj['line']:
        x_total += (line[1] + line[3])/2
        y_total += (line[2] + line[4])/2
        count += 1

    # iterate through circles
    for circle in obj['circle']:
        x_total += circle[1]
        y_total += circle[2]
        count += 1

    # iterate through curves
    for curve in obj['curve']:
        x_total += (curve[1] + curve[3] + curve[5])/3
        y_total += (curve[2] + curve[4] + curve[6])/3
        count += 1

    # calculate the average of the centers
    if(count > 0):
        center_x = x_total / count
        center_y = y_total / count
    print(center_x, center_y)
    return (center_x, center_y)

