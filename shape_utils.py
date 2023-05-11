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

def get_topmost_point(shape_dictionary):
    topmost_y = float('inf')
    x_total = 0
    count = 0

    # Iterate through lines
    for line in shape_dictionary.get('line', []):
        x_total += (line[1] + line[3]) / 2
        topmost_y = min(topmost_y, line[2], line[4])
        count += 1

    # Iterate through circles
    for circle in shape_dictionary.get('circle', []):
        x_total += circle[1]
        topmost_y = min(topmost_y, circle[2])
        count += 1

    # Iterate through curves
    for curve in shape_dictionary.get('curve', []):
        x_total += (curve[1] + curve[3] + curve[5]) / 3
        topmost_y = min(topmost_y, curve[2], curve[4], curve[6])
        count += 1

    if count > 0:
        center_x = x_total / count
        return (center_x, topmost_y)

    return None

def get_rightmost_point(shape_dictionary):
    rightmost_x = float('-inf')
    y_total = 0
    count = 0

    # Iterate through lines
    for line in shape_dictionary.get('line', []):
        rightmost_x = max(rightmost_x, line[1], line[3])
        y_total += (line[2] + line[4]) / 2
        count += 1

    # Iterate through circles
    for circle in shape_dictionary.get('circle', []):
        rightmost_x = max(rightmost_x, circle[1] + circle[3])
        y_total += circle[2]
        count += 1

    # Iterate through curves
    for curve in shape_dictionary.get('curve', []):
        rightmost_x = max(rightmost_x, curve[1], curve[3], curve[5])
        y_total += (curve[2] + curve[4] + curve[6]) / 3
        count += 1

    if count > 0:
        center_y = y_total / count
        return (rightmost_x, center_y)

    return None

def get_leftmost_point(shape_dictionary):
    leftmost_x = float('inf')
    y_total = 0
    count = 0

    # Iterate through lines
    for line in shape_dictionary.get('line', []):
        leftmost_x = min(leftmost_x, line[1], line[3])
        y_total += (line[2] + line[4]) / 2
        count += 1

    # Iterate through circles
    for circle in shape_dictionary.get('circle', []):
        leftmost_x = min(leftmost_x, circle[1] - circle[3])
        y_total += circle[2]
        count += 1

    # Iterate through curves
    for curve in shape_dictionary.get('curve', []):
        leftmost_x = min(leftmost_x, curve[1], curve[3], curve[5])
        y_total += (curve[2] + curve[4] + curve[6]) / 3
        count += 1

    if count > 0:
        center_y = y_total / count
        return (leftmost_x, center_y)

    return None

def get_figure_width(shape_dictionary):
    leftmost_point = get_leftmost_point(shape_dictionary)
    rightmost_point = get_rightmost_point(shape_dictionary)

    if leftmost_point is not None and rightmost_point is not None:
        width = abs(rightmost_point[0] - leftmost_point[0])
        return width

    return None

def get_figure_height(shape_dictionary):
    topmost_point = get_topmost_point(shape_dictionary)
    biggest_y = get_biggest_y(shape_dictionary)

    if topmost_point is not None and biggest_y is not None:
        height = abs(biggest_y - topmost_point[1])
        return height

    return None
