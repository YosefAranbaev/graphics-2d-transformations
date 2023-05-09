def get_biggest_x(shape_dictionary):
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

def get_biggest_y(shape_dictionary):
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

def get_center(shape_dictionary):
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