import Tkinter as tk
import math
fh = open('maps/dash.gnv', 'rb')
ba = bytearray(fh.read())[32:]
GRID_SIZE=int(math.sqrt(len(ba)))
i = 0
class GNVVis(tk.Frame):
    def __init__(self, parent, rows=GRID_SIZE, columns=GRID_SIZE, size=15, color1="white", color2="blue"):
        print rows
        print columns
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

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        i = len(ba)-1
        for row in range(self.rows):
            for col in range(self.columns):
                color = self.color1 if (ba[i]&1)==1 else self.color2
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
