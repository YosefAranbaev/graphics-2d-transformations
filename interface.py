import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
import csv
from shapes import line, circle, curve
from transformations import mirror_shape_x, mirror_shape_y, shear_shape
from exception import exception

class App:
    # def __init__(self, master):
    #     self.create_gui()
    #     self.master = master
    #     master.title("2D Painter")

    #     # Read points from the input
    #     self.initial_points = {'line': [], 'circle': [], 'curve': []}
    #     self.read_points('input.csv')

    #     # Create a canvas for drawing shapes
    #     self.canvas = tk.Canvas(master, width=600, height=600, bg="white")
    #     self.canvas.pack()
    
    #     # Draw the figure
    #     self.draw_figure(self.initial_points)

    #     # Shear the shape with mouse grabbing
    #     # self.current_points = shear_shape(self.canvas, self.initial_points)
        
    #     # self.draw_figure(self.current_points)

    def read_points(self, path):
        with open(path, 'r', encoding='utf-8-sig', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # TODO: check the row has at least 4 parameters
                color = '#{:02x}{:02x}{:02x}'.format(int(row[1]), int(row[2]), int(row[3]))
                if row[0] == 'line':
                    # TODO: check the row has 8 parameters
                    x1, y1, x2, y2 = int(row[4]), int(row[5]), int(row[6]), int(row[7])
                    self.initial_points['line'].append([color, x1, y1, x2, y2])
                elif row[0] == 'circle':
                    # TODO: check the row has 7 parameters
                    x, y, radius = int(row[4]), int(row[5]), int(row[6])
                    self.initial_points['circle'].append([color, x, y, radius])
                elif row[0] == 'curve':
                    # TODO: check the row has 10 parameters
                    start_x, start_y, end_x, end_y, cp_x, cp_y = int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9])
                    self.initial_points['curve'].append([color, start_x, start_y, end_x, end_y, cp_x, cp_y])
                else:
                    exception('Unknown shape')
                    continue

    def draw_figure(self, points):
        for ln in points['line']:
            color, x1, y1, x2, y2 = ln[0], ln[1], ln[2], ln[3], ln[4]
            line(self.canvas, color, x1, y1, x2, y2)

        for cir in points['circle']:
            color, x, y, radius = cir[0], cir[1], cir[2], cir[3]
            circle(self.canvas, color, x, y, radius)

        for cur in points['curve']:
            color, start_x, start_y, end_x, end_y, cp_x, cp_y = cur[0], cur[1], cur[2], cur[3], cur[4], cur[5], cur[6]
            curve(self.canvas, color, start_x, start_y, end_x, end_y, cp_x, cp_y)


    def create_gui(self):
        print("hello")
        root = tk.Tk()
        root.geometry("400x400")
        self.canvas = tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.place(relx=0.5, rely=7.5, anchor='center')
        self.canvas.pack()
        def load_button():
            master = root
            master.title("2D Painter")
            self.canvas.delete("all")

            # Read points from the input
            self.initial_points = {'line': [], 'circle': [], 'curve': []}
            self.read_points('input.csv')
            # Create a canvas for drawing shapes
            # Draw the figure
            self.draw_figure(self.initial_points)
            # Shear the shape with mouse grabbing
            # self.current_points = shear_shape(self.canvas, self.initial_points)
            print("Load")

        def move_button():
            print("Move")

        def scale_button():
            x = simpledialog.askinteger("Scale", "Enter x value (0-1000):", minvalue=0, maxvalue=1000)
            y = simpledialog.askinteger("Scale", "Enter y value (0-1000):", minvalue=0, maxvalue=1000)
            if x is not None and y is not None:
                print(f"Scale {x} {y}")
            else:
                messagebox.showerror("Invalid values", "Please enter valid values.")

        def Rotate_button():
            x = simpledialog.askinteger("Rotate", "Enter x value (0-360):", minvalue=0, maxvalue=360)
            if x is not None:
                print(f"Scale {x}")
            else:
                messagebox.showerror("Invalid values", "Please enter valid values.")
        
        def MirrorX_button():
            # x = simpledialog.askinteger("MirrorX", "Enter x value (0-5):", minvalue=0, maxvalue=5)
            # if x is not None:
            self.canvas.delete("all")
            self.current_points = mirror_shape_x(self.canvas, self.initial_points)
            self.draw_figure(self.current_points)
            print(f"Scale")

            # else:
            #     messagebox.showerror("Invalid values", "Please enter valid values.")
        
        # def MirrorX_button():
            # x = simpledialog.askinteger("MirrorY", "Enter y value (0-5):", minvalue=0, maxvalue=5)
            # if x is not None:
            print(f"Scale")
            # else:
            #     messagebox.showerror("Invalid values", "Please enter valid values.")
        
        def MirrorY_button():
            # y = simpledialog.askinteger("MirrorY", "Enter y value (0-5):", minvalue=0, maxvalue=5)
            # if y is not None:
            self.canvas.delete("all")
            self.current_points = mirror_shape_y(self.canvas, self.initial_points)
            self.draw_figure(self.current_points)
            print(f"Scale")
            # else:
            #     messagebox.showerror("Invalid values", "Please enter valid values.")
        
        def Crop_button():
            # x = simpledialog.askinteger("Crop", "Enter x value (0-1000):", minvalue=0, maxvalue=1000)
            # y = simpledialog.askinteger("Crop", "Enter y value (0-1000):", minvalue=0, maxvalue=1000)
            # if x is not None and y is not None:
            self.canvas.delete("all")
            self.current_points = shear_shape(self.canvas, self.initial_points)
            self.draw_figure(self.current_points)
            # print(f"Scale {x} {y}")
            # else:
            #     messagebox.showerror("Invalid values", "Please enter valid values.")

        def show_help():
            help_str = "Available Buttons:\n"
            help_str += "Load\n"
            help_str += "Move\n"
            help_str += "Scale\n"
            help_str += "Rotate\n"
            help_str += "Mirror\n"
            help_str += "Crop\n"
            messagebox.showinfo("Help", help_str)

        def exit_gui():
            root.destroy()
            
            


        load_btn = tk.Button(root, text="Load", command=load_button)
        load_btn.place(x=10, y=10)

        move_btn = tk.Button(root, text="Move", command=move_button)
        move_btn.place(x=48, y=10)

        scale_btn = tk.Button(root, text="Scale", command=scale_button)
        scale_btn.place(x=90, y=10)

        Rotate_btn = tk.Button(root, text="Rotate", command=Rotate_button)
        Rotate_btn.place(x=128, y=10)

        Mirror_btn = tk.Button(root, text="MirrorX", command=MirrorX_button)
        Mirror_btn.place(x=173, y=10)

        Mirror_btn = tk.Button(root, text="MirrorY", command=MirrorY_button)
        Mirror_btn.place(x=223, y=10)

        Crop_btn = tk.Button(root, text="Crop", command=Crop_button)
        Crop_btn.place(x=275, y=10)

        help_btn = tk.Button(root, text="Help", command=show_help)
        help_btn.place(x=312, y=10)

        exit_btn = tk.Button(root, text="Exit", command=exit_gui)
        exit_btn.place(x=348, y=10)


        root.mainloop()
        
        


def main():
    # root = tk.Tk()
    app = App()
    app.create_gui()
    # root.mainloop()
    
    # Function to handle the move button click event
def move_button_clicked():
    # Get the x and y offsets from the user
    x_offset = float(x_offset_entry.get())
    y_offset = float(y_offset_entry.get())

    # Call the move_shape function to move the shape
    app.current_points = move_shape(app.current_points, x_offset, y_offset, app.canvas, app.draw_figure)

# Function to handle the scale button click event
def scale_button_clicked():
    # Get the scale factor and pivot coordinates from the user
    scale_factor = float(scale_factor_entry.get())
    pivot_x = float(pivot_x_entry.get())
    pivot_y = float(pivot_y_entry.get())

    # Call the scale_shape function to scale the shape
    app.current_points = scale_shape(app.current_points, scale_factor, (pivot_x, pivot_y), app.canvas, app.draw_figure)

# Function to handle the rotate button click event
def rotate_button_clicked():
    # Get the rotation angle and pivot coordinates from the user
    angle = float(angle_entry.get())
    pivot_x = float(pivot_x_entry.get())
    pivot_y = float(pivot_y_entry.get())

    # Call the rotate_shape function to rotate the shape
    app.current_points = rotate_shape(app.current_points, angle, (pivot_x, pivot_y), app.canvas, app.draw_figure)

# Function to handle the mirror X button click event
def mirror_x_button_clicked():
    # Call the mirror_x_shape function to mirror the shape along the X-axis
    app.current_points = mirror_x_shape(app.current_points, app.canvas, app.draw_figure)

# Function to handle the mirror Y button click event
def mirror_y_button_clicked():
    # Call the mirror_y_shape function to mirror the shape along the Y-axis
    app.current_points = mirror_y_shape(app.current_points, app.canvas, app.draw_figure)

# Function to handle the crop button click event
def crop_button_clicked():
    # Call the crop_shape function to crop the shape
    app.current_points = crop_shape(app.current_points, app.canvas, app.draw_figure)


if __name__ == '__main__':
    main()

