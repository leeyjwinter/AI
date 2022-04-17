from drawingpanel import *
from multiprocessing import Process

def car(panel, x, y,color,step):
    panel.canvas.create_rectangle(x * step, y, x * step + 100, y + 50, fill=color)
    panel.canvas.create_oval(x * step + 10, y + 40, x * step + 30, y + 60, fill="red", outline="red")
    panel.canvas.create_oval(x * step + 70, y + 40, x * step + 90, y + 60, fill="red", outline="red")
    panel.canvas.create_rectangle(x * step + 70, y + 10, x * step + 100, y + 30, fill="cyan", outline="cyan")

def moving_car(panel, x, y, color,step):
    for i in range(step):
        # car(panel, 10, 10, "black", 10)
        # car(panel, 10, 80, "blue", 20)
        # car(panel, 10, 150, "pink", 5)
        # car(panel, 10, 220, "brown", 3)
        panel.canvas.create_rectangle(0, 0, 500, 300, fill="grey")
        panel.canvas.create_rectangle(x*i, y, x*i + 100, y + 50, fill=color)
        panel.canvas.create_oval(x*i + 10, y + 40, x*i + 30, y + 60, fill="red", outline="red")
        panel.canvas.create_oval(x*i + 70, y + 40, x*i + 90, y + 60, fill="red", outline="red")
        panel.canvas.create_rectangle(x*i + 70, y + 10, x*i + 100, y + 30, fill="cyan", outline="cyan")
        panel.sleep(100)


    # panel.canvas.create_rectangle(x, y, x + 100, y + 50, fill=color)
    # panel.canvas.create_oval(x + 10, y + 40, x + 30, y + 60, fill="red", outline="red")
    # panel.canvas.create_oval(x + 70, y + 40, x + 90, y + 60, fill="red", outline="red")
    # panel.canvas.create_rectangle(x + 70, y + 10, x + 100, y + 30, fill="cyan",


# main

panel = DrawingPanel(500, 300)

#p1 = Process(target=moving_car(panel, 10, 10, "black",10))
#p2 = Process(target=moving_car(panel, 10, 80, "blue",20))
#p3 = Process(target=moving_car(panel, 10, 150, "pink",5))
#p4 = Process(target=moving_car(panel, 10, 220, "brown",3))

# p1.start()
# p2.start()
# p3.start()
# p4.start()


# p1.join()
# p2.join()
# p3.join()
# p4.join()
moving_car(panel, 10, 10, "black",10)
moving_car(panel, 10, 80, "blue",20)
moving_car(panel, 10, 150, "pink",5)
moving_car(panel, 10, 220, "brown",3)
car(panel, 320, 30)
car(panel, 330, 100)
car(panel, 340, 200)

