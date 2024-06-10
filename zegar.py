import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.center_x = 200
        self.center_y = 200
        self.radius = 180
        self.update_clock()

    def draw_hand(self, angle, length, width, color):
        angle = math.radians(angle)
        end_x = self.center_x + length * math.sin(angle)
        end_y = self.center_y - length * math.cos(angle)
        self.canvas.create_line(self.center_x, self.center_y, end_x, end_y, width=width, fill=color)

    def update_clock(self):
        self.canvas.delete("all")

        # Draw clock face
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius, 
                                self.center_x + self.radius, self.center_y + self.radius)

        for i in range(12):
            angle = math.radians(i * 30)
            x1 = self.center_x + (self.radius - 20) * math.sin(angle)
            y1 = self.center_y - (self.radius - 20) * math.cos(angle)
            x2 = self.center_x + self.radius * math.sin(angle)
            y2 = self.center_y - self.radius * math.cos(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2)

        # Get current time
        now = time.localtime()
        hours = now.tm_hour % 12
        minutes = now.tm_min
        seconds = now.tm_sec

        # Draw the hands
        hour_angle = (hours + minutes / 60) * 30
        minute_angle = (minutes + seconds / 60) * 6
        second_angle = seconds * 6

        self.draw_hand(hour_angle, self.radius * 0.5, 6, 'black')
        self.draw_hand(minute_angle, self.radius * 0.8, 4, 'blue')
        self.draw_hand(second_angle, self.radius * 0.9, 2, 'red')

        # Schedule the update function to be called after 1000 ms
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()