from drawingpanel import *


def car(panel, x, y):
    panel.canvas.create_rectangle(x, y, x + 100, y + 50, fill="black")
    panel.canvas.create_oval(x + 10, y + 40, x + 30, y + 60, fill="red", outline="red")
    panel.canvas.create_oval(x + 70, y + 40, x + 90, y + 60, fill="red", outline="red")
    panel.canvas.create_rectangle(x + 70, y + 10, x + 100, y + 30, fill="cyan", outline="cyan")


# main

panel = DrawingPanel(500, 300)
panel.set_background("grey")

car(panel, 10, 70)
car(panel, 10, 140)
car(panel, 200, 30)
car(panel, 200, 140)
car(panel, 320, 30)
car(panel, 330, 100)
car(panel, 340, 200)
