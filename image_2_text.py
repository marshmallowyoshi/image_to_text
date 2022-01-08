from PIL import Image
import numpy as np
import sys

fn = input("filename(no extension, png only):")
ext = ".png"
full_fn = "%s%s" %(fn, ext)
np.set_printoptions(threshold=sys.maxsize)
img = Image.open(full_fn).convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W
np_img[np_img > 0] = 1

final = np_img.flatten()

x = np.array2string(final, separator=',')
print(final)

text_file = "%s.txt" %(fn)
with open(text_file, 'a') as f:
    f.write(x)