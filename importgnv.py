import Tkinter as tk
import math
import numpy as np
import Image
from scipy import misc
im_m = misc.imread('gnv.jpg')
arrsize = im_m.shape[0]*im_m.shape[1]
arr = bytearray(arrsize)
i = 0
for row in range(0,im_m.shape[0]):
    for col in range(0,im_m.shape[0]):
        arr[i] = 1 if (im_m[row][col][0])==0 else 0
        i+=1
fh = open('maps/dash.gnv', 'rb')
ba = bytearray(fh.read())[:32]
res = np.concatenate((ba, arr), axis=1)
fh = open('maps/exported.gnv', 'wb')
fh.write(res)
