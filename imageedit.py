# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:57:17 2021

@author: NTayl
"""
from PIL import Image
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
img = Image.open('edit.png').convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W
np_img[np_img > 0] = 1

final = np_img.flatten()

x = np.array2string(final, separator=',')
print(final)

with open('test2.txt', 'a') as f:
    f.write(x)