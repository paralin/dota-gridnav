import Tkinter as tk
import math
import numpy as np
fh = open('maps/dash.gnv', 'rb')
img = np.zeros((size,size,3),dtype="uint8")
fh.seek(32)
ba = np.fromfile(fh, dtype='uint8')
side = int(np.sqrt(len(ba)))
print ba
