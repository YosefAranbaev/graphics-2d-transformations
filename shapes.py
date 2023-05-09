from tkinter import *

def pixel(canvas, x, y, color):
    """Draws a single pixel on the canvas."""
    x = int(x)
    y = int(y)
    canvas.create_line(x, y, x+1, y, fill=color)

def line(canvas, color, x1, y1, x2, y2):
    """Draws a line between two points on the canvas."""

    # Check if the canvas is None
    if canvas is None:
        return

    # Convert input coordinates to integers
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

    # Check if the input points have zero length
    if x1 == x2 and y1 == y2:
        return

    # Calculate the distance between two points
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the direction of the line
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Calculate the error and increment values
    err = dx - dy
    e2 = 0
    x, y = x1, y1

    # Draw the line by iterating over the pixels along the line
    while True:
        # Set the color of the current pixel
        pixel(canvas, x, y, color)

        # Stop the loop if we have reached the end point
        if x == x2 and y == y2:
            break

        # Update the error and position values
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def circle(canvas, color, center_x, center_y, radius):
    """Draws a circle from the given center point and radius."""
    x_offset, y_offset = 0, radius
    decision_parameter = 3 - 2 * radius

    _draw_circle_points(canvas, center_x, center_y, x_offset, y_offset, color)

    while y_offset >= x_offset:
        x_offset += 1

        # Update decision parameter based on current position
        if decision_parameter > 0:
            y_offset -= 1
            decision_parameter = decision_parameter + 4 * (x_offset - y_offset) + 10
        else:
            decision_parameter = decision_parameter + 4 * x_offset + 6

        _draw_circle_points(canvas, center_x, center_y, x_offset, y_offset, color)

def curve(canvas, color, start_x, start_y, end_x, end_y, cp_x, cp_y, lines_number=100):
    """Draws a quadratic bezier curve on the canvas."""
    # Calculate the curve points
    curve_points = []
    for i in range(lines_number):
        t = i / (lines_number - 1)
        x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * cp_x + t ** 2 * end_x
        y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * cp_y + t ** 2 * end_y
        curve_points.append((int(x), int(y)))

    # Draw the curve using create_line method
    for i in range(len(curve_points)-1):
        canvas.create_line(curve_points[i], curve_points[i+1], fill=color, width=2)

def _draw_circle_points(canvas, center_x, center_y, x_offset, y_offset, color):
    pixel(canvas, center_x + x_offset, center_y + y_offset, color)
    pixel(canvas, center_x - x_offset, center_y + y_offset, color)
    pixel(canvas, center_x + x_offset, center_y - y_offset, color)
    pixel(canvas, center_x - x_offset, center_y - y_offset, color)
    pixel(canvas, center_x + y_offset, center_y + x_offset, color)
    pixel(canvas, center_x - y_offset, center_y + x_offset, color)
    pixel(canvas, center_x + y_offset, center_y - x_offset, color)
    pixel(canvas, center_x - y_offset, center_y - x_offset, color)
