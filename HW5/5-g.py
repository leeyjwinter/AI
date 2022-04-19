from drawingpanel import *

def car(panel, x, y, color):
    panel.canvas.create_rectangle(x,y, x+100, y+50, fill=color)
    panel.canvas.create_oval(x+10, y+40, x+30, y+60, fill="red", outline="red")
    panel.canvas.create_oval(x+70, y+40, x+90, y+60, fill="red", outline="red")
    panel.canvas.create_rectangle(x+70, y+10, x+100, y+30, fill="cyan", outline="cyan")

#main
panel=DrawingPanel(500, 300)
panel.set_background("grey")

car(panel, 10, 10, "black")
car(panel, 10, 80, "blue")
car(panel, 10, 150, "pink")
car(panel, 10, 220, "yellow")

for i in range(50):
    panel.canvas.create_rectangle(0,0,500,300,outline="grey", fill="grey")
    car(panel, 10*i, 10, "black")
    car(panel, 20*i, 80, "blue")
    car(panel, 16*i, 150, "pink")
    car(panel, 40*i, 220, "yellow")
    panel.sleep(100)