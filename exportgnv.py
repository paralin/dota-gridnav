import Tkinter as tk
import math
import numpy as np
import Image
fh = open('maps/dash.gnv', 'rb')
fh.seek(32)
# read the binary data into unsigned 8-bit array
ba = np.fromfile(fh, dtype='uint8')
# calculate the side length of the square array and reshape ba accordingly
side = int(np.sqrt(len(ba)))
ba.reshape((side,side))
# toss everything else apart from the last bit of each pixel
ba &= 1
print len(ba)
img = np.dstack([255*ba]*3)
import Image
im = Image.fromarray(img)
im.save("gnv.jpg")
