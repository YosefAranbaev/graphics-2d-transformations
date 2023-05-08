import tkinter as tk
from tkinter import ttk, messagebox
import math

def apply_translation(vertices, x_offset, y_offset):
    return [(item[0] + x_offset, item[1] + y_offset, *item[2:]) for item in vertices]

def move_shape(vertices, dx, dy, canvas, update_callback):
    new_vertices = [(item[0] + dx, item[1] + dy, *item[2:]) for item in vertices]
    update_callback(new_vertices, canvas)

def scale_shape(vertices, scale_factor, pivot, canvas, update_callback):
    new_vertices = [
        ((pivot[0] + (x - pivot[0]) * scale_factor), (pivot[1] + (y - pivot[1]) * scale_factor), radius, group)
        if len(item) == 4 else
        ((pivot[0] + (x1 - pivot[0]) * scale_factor), (pivot[1] + (y1 - pivot[1]) * scale_factor),
        (pivot[0] + (x2 - pivot[0]) * scale_factor), (pivot[1] + (y2 - pivot[1]) * scale_factor), group)
        for x, y, radius, group in vertices if len(vertices) == 4
        for x1, y1, x2, y2, group in vertices if len(vertices) == 5
    ]
    update_callback(new_vertices, canvas)

def rotate_shape(vertices, angle, pivot, canvas, update_callback):
    new_vertices = []
    angle_rad = math.radians(angle)

    for item in vertices:
        if len(item) == 4:
            x, y, radius, group = item
            dx = x - pivot[0]
            dy = y - pivot[1]
            new_x = pivot[0] + (dx * math.cos(angle_rad) - dy * math.sin(angle_rad))
            new_y = pivot[1] + (dx * math.sin(angle_rad) + dy * math.cos(angle_rad))
            new_vertices.append((new_x, new_y, radius, group))
        elif len(item) == 5:
            x1, y1, x2, y2, group = item
            dx1 = x1 - pivot[0]
            dy1 = y1 - pivot[1]
            dx2 = x2 - pivot[0]
            dy2 = y2 - pivot[1]
            new_x1 = pivot[0] + (dx1 * math.cos(angle_rad) - dy1 * math.sin(angle_rad))
            new_y1 = pivot[1] + (dx1 * math.sin(angle_rad) + dy1 * math.cos(angle_rad))
            new_x2 = pivot[0] + (dx2 * math.cos(angle_rad) - dy2 * math.sin(angle_rad))
            new_y2 = pivot[1] + (dx2 * math.sin(angle_rad) + dy2 * math.cos(angle_rad))
            new_vertices.append((new_x1, new_y1, new_x2, new_y2, group))
        else:
            raise ValueError("Invalid vertex format: {}".format(item))

    canvas.delete("all")

     