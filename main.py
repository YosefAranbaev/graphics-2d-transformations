import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
import csv
from shapes import line, circle, curve
from transformations import mirror_shape_x, mirror_shape_y, shear_shape, rotate_shape_45, scale_shape_15, move_shape
from shape_utils import get_center, get_topmost_point, get_rightmost_point, get_leftmost_point

class App:
    def read_points(self, path):
        with open(path, 'r', encoding='utf-8-sig', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) < 4:
                    messagebox.showerror('Invalid row in the input file', 'Row must start from: Shape, R, G, B')
                    return

                color = '#{:02x}{:02x}{:02x}'.format(int(row[1]), int(row[2]), int(row[3]))
                if row[0] == 'line' and len(row) >= 8:
                    x1, y1, x2, y2 = int(row[4]), int(row[5]), int(row[6]), int(row[7])
                    self.initial_points['line'].append([color, x1, y1, x2, y2])
                elif row[0] == 'circle' and len(row) >= 7:
                    x, y, radius = int(row[4]), int(row[5]), int(row[6])
                    self.initial_points['circle'].append([color, x, y, radius])
                elif row[0] == 'curve' and len(row) >= 10:
                    start_x, start_y, end_x, end_y, cp_x, cp_y = int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9])
                    self.initial_points['curve'].append([color, start_x, start_y, end_x, end_y, cp_x, cp_y])
                else:
                    messagebox.showerror('Invalid row in the input file', 'Unknown shape or missing parameters')
                    return

    def draw_figure(self, shape_dictionary):
        for ln in shape_dictionary['line']:
            color, x1, y1, x2, y2 = ln[0], ln[1], ln[2], ln[3], ln[4]
            line(self.canvas, color, x1, y1, x2, y2)

        for cir in shape_dictionary['circle']:
            color, x, y, radius = cir[0], cir[1], cir[2], cir[3]
            circle(self.canvas, color, x, y, radius)

        for cur in shape_dictionary['curve']:
            color, start_x, start_y, end_x, end_y, cp_x, cp_y = cur[0], cur[1], cur[2], cur[3], cur[4], cur[5], cur[6]
            curve(self.canvas, color, start_x, start_y, end_x, end_y, cp_x, cp_y)

    def center_figure(self):
        # calculate the center of the screen
        self.root.update_idletasks() 
        screen_width = self.root.winfo_width()
        screen_height = self.root.winfo_height()
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        # calculate the center of the figure
        current_figure_center_point = get_center(self.initial_points)

        # find dx and dy
        dx = center_x - current_figure_center_point[0]
        dy = center_y - current_figure_center_point[1]

        # move the figure to the center 
        self.initial_points = move_shape(self.initial_points, dx, dy)
        self.draw_figure(self.initial_points)

    def on_mouse_press(self, event):
        # ignore clicks on the control buttons
        if event.x < 358 and event.y < 40:
            return
        
        # shear the figure
        if self.shear_on == True:
            self.is_mouse_pressed = True
            self.call_shear_x(event.x)

    def on_mouse_release(self, event):
        self.is_mouse_pressed = False

    def on_mouse_motion(self, event):   
        if self.is_mouse_pressed:
            # ignore clicks on the control buttons
            if event.x < 358 and event.y < 40:
                return
            
            # shear the figure
            self.call_shear_x(event.x)

    def stop_shear(self):
        self.is_mouse_pressed = False
        self.shear_on = False

    def stop_move(self):
        self.move_on = False

    def call_shear_x(self, mouse_x):
        shape_center_point = get_center(self.current_points)
        shape_rightmost_point = get_rightmost_point(self.current_points)
        shape_leftmost_point = get_leftmost_point(self.current_points)
        
        dx = 0
        if mouse_x < shape_leftmost_point[0]:
            dx = shape_leftmost_point[0] - mouse_x
        elif mouse_x > shape_rightmost_point[0] :
            dx = shape_rightmost_point[0] - mouse_x
        else:
            dx = shape_center_point[0] - mouse_x
        
        shear_const_x = dx/1000

        self.canvas.delete("all")
        self.current_points = shear_shape(self.current_points, shear_const_x)
        self.draw_figure(self.current_points)

    def get_mouse_coordinates(self, event):
        # ignore clicks on the control buttons
        if event.x < 358 and event.y < 40:
            return
        
        # ignore not move process
        if not self.move_on:
            return
        
        mouse_x = event.x
        mouse_y = event.y

        self.coordinates.append((mouse_x, mouse_y))
        self.click_count += 1

        if self.click_count == 2:
            x1, y1 = self.coordinates[0]
            x2, y2 = self.coordinates[1]
            dx = x2 - x1
            dy = y2 - y1

            # move the figure
            self.canvas.delete("all")
            self.current_points = move_shape(self.current_points, dx, dy)
            self.draw_figure(self.current_points)

            # Reset click count and coordinates list
            self.click_count = 0
            self.coordinates = []

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("2D Painter")
        self.is_mouse_pressed = False
        self.shear_on = False
        self.move_on = False
        self.click_count = 0
        self.coordinates = []

        # calculate the canvas width and height as 60% of the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        canvas_width = int(screen_width * 0.6)
        canvas_height = int(screen_height * 0.6)

        # initialize the canvas
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.place(relx=0.5, rely=7.5, anchor='center')
        self.canvas.pack(expand=True, fill="both")

        # read points from the input and draw the figure
        self.initial_points = {'line': [], 'circle': [], 'curve': []}
        self.read_points('input.csv') 
        self.center_figure()
        self.current_points = self.initial_points.copy()

        def reload_button():
            self.stop_shear()
            self.stop_move()
            self.initial_points = {'line': [], 'circle': [], 'curve': []}
            self.canvas.delete("all")
            self.read_points('input.csv')
            self.center_figure()
            self.current_points = self.initial_points.copy()

        def move_button():
            self.stop_shear()
            self.move_on = True

            # Bind the mouse button event to the function
            self.root.bind("<Button-1>", self.get_mouse_coordinates)   

        def scale_button():
            self.stop_shear()
            self.stop_move()
            self.canvas.delete("all")
            self.current_points = scale_shape_15(self.canvas, self.current_points)
            self.draw_figure(self.current_points)
            
        def rotate_button():
            self.stop_shear()
            self.stop_move()
            self.canvas.delete("all")
            self.current_points = rotate_shape_45(self.canvas, self.current_points)
            self.draw_figure(self.current_points)
        
        def mirrorX_button():
            self.stop_shear()
            self.stop_move()
            self.canvas.delete("all")
            self.current_points = mirror_shape_x(self.current_points)
            self.draw_figure(self.current_points)
        
        def mirrorY_button():
            self.stop_shear()
            self.stop_move()
            self.canvas.delete("all")
            self.current_points = mirror_shape_y(self.current_points)
            self.draw_figure(self.current_points)
        
        def shear_button():
            self.stop_move()
            self.shear_on = True
            
            # Bind mouse press, release, and motion events to functions
            self.root.bind("<ButtonPress-1>", self.on_mouse_press)
            self.root.bind("<ButtonRelease-1>", self.on_mouse_release)
            self.root.bind("<Motion>", self.on_mouse_motion) 

        def show_help():
            self.stop_shear()
            self.stop_move()
            help_str = "Available Buttons:\n\n"
            help_str += "Load - load the drawing and center it on the screen\n"
            help_str += "Move - click on two points on the canvas to move the shape\n"
            help_str += "Scale - increase the shape size\n"
            help_str += "Rotate - rotate the shape\n"
            help_str += "MirrorX - mirror the shape along the x-axis \n"
            help_str += "MirrorY - mirror the shape along the y-axis \n"
            help_str += "shear - drag the shape left and right for shearing\n"
            help_str += "help - press for additional information\n"
            help_str += "exit - press exit to exit\n"
            messagebox.showinfo("Help", help_str)

        def exit_gui():
            self.stop_shear()
            self.stop_move()
            self.root.destroy()

        reload_btn = tk.Button(self.root, text="Reload", command=reload_button)
        reload_btn.place(x=10, y=10)

        move_btn = tk.Button(self.root, text="Move", command=move_button)
        move_btn.place(x=58, y=10)

        scale_btn = tk.Button(self.root, text="Scale", command=scale_button)
        scale_btn.place(x=100, y=10)

        rotate_btn = tk.Button(self.root, text="Rotate", command=rotate_button)
        rotate_btn.place(x=138, y=10)

        mirror_btn = tk.Button(self.root, text="MirrorX", command=mirrorX_button)
        mirror_btn.place(x=183, y=10)

        mirror_btn = tk.Button(self.root, text="MirrorY", command=mirrorY_button)
        mirror_btn.place(x=233, y=10)

        shear_btn = tk.Button(self.root, text="Shear", command=shear_button)
        shear_btn.place(x=283, y=10)

        help_btn = tk.Button(self.root, text="Help", command=show_help)
        help_btn.place(x=322, y=10)

        exit_btn = tk.Button(self.root, text="Exit", command=exit_gui)
        exit_btn.place(x=358, y=10)

        self.root.mainloop()

def main():
    app = App()
    app.create_gui()

if __name__ == '__main__':
    main()

