import Tkinter as tk
import math
import numpy as np
fh = open('maps/dash.gnv', 'rb')
ba = bytearray(fh.read())[32:]
GRID_SIZE=int(math.sqrt(len(ba)))

def __flood_fill(image, x, y, value, cpoints):
    if not (x<len(image[0]) and y<len(image) and x>=0 and y>=0):
        return
    edge = [(x, y)]
    image[x][y] = 2
    while edge:
        newedge = []
        for (x, y) in edge:
            for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (s<len(image[0]) and t<len(image) and s>=0 and t>=0):
                    pix = image[s][t]
                    if not (pix in (0,1)):
                        continue
                    image[s][t] = 2
                    if pix!=value:
                        image[s][t]=3
                        cpoints.append((s,t))
                        continue
                    newedge.append((s, t))
        edge = newedge

def __flood_fill_edge(image, x, y, cpoints):
    if not (x<len(image[0]) and y<len(image) and x>=0 and y>=0):
        return
    pix = image[x][y]
    if pix !=3:
        return
    image[x][y] = 10
    cpoints.append((x*5,(GRID_SIZE*5)-y*5))
    print (x,y)
    for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)):
        __flood_fill_edge(image, s, t, cpoints)

floodx = 155
floody = 130
floodfill = []
cpoints = []
bas = np.reshape(ba, (GRID_SIZE, GRID_SIZE))
__flood_fill(bas, floodx, floody, 0, cpoints)
bas[floodx][floody] = 24
ba = np.hstack(bas)

anggrid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.int)

#Order the points
#Go over each edge point and get the direction to the white space
for pt in cpoints:
    x = pt[0]
    y = pt[1]
    dirs = []
    dir = 0
    for (s, t) in ((x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)):
        if bas[s][t]==2:
            dirs.append(dir)
        dir += 45
    anggrid[x][y] = np.mean(dirs)
    print (x, y), ": ", anggrid[x][y]

output = "["
y = 0
for row in anggrid:
    x = 0
    output += "["
    for col in row:
        output += str(anggrid[x][y])
        if x < GRID_SIZE-1:
            output += ","
        x+=1
    output += "]"
    if y < GRID_SIZE-1:
        output += ","
    y+=1
output += "]"
with open('anggrid.txt', 'w') as output_file:
    output_file.write(output)

class GNVVis(tk.Frame):
    def __init__(self, parent, rows=GRID_SIZE, columns=GRID_SIZE, size=15, color1="white", color2="blue"):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both")
        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        print "clicked at ", GRID_SIZE-(event.x/self.size), GRID_SIZE-(event.y/self.size)

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        i = len(ba)-1
        for row in range(self.rows):
            for col in range(self.columns):
                if ba[i]==3:
                    color = "orange"
                elif (ba[i]==2):
                    color = "red"
                elif (ba[i]==1):
                    color = "white"
                elif ba[i]==24:
                    color = "black"
                else:
                    color = "blue"
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                i-=1

        self.canvas.tag_lower("square")

if __name__ == "__main__":
    root = tk.Tk()
    board = GNVVis(root)
    board.pack(side="top", fill="both", expand="false")
    root.mainloop()
