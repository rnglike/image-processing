## TUDO ISSO, pra deixar com menos contraste

import PIL
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def show_img(im,pb=False):
    if pb:
        plt.imshow(im,cmap='gray')
    else:
        plt.imshow(im)
    plt.axis('off')
    plt.show()

def show_hist(x,h):
    plt.bar(x,h)
    plt.show()
    
def get_acc(h):
    a = len(h) * [0]
    for i, y in enumerate(h):
        if i > 0:
            a[i] = a[i-1] + y;
    return a

# 1. Read the image
im = PIL.Image.open('images/f.jpg')
im = grey(im)
W,H = im.size

print(f"width: {W}")
print(f"height: {H}")
print(f"total: {W*H} px")


# 2. Get the histogram
x1 = get_range(256)
h1 = hist(im)


# 3. Get the normalized histogram
scales = len(x1)
h_sum = sum(h1)
h2 = [y/h_sum for y in h1]

    
# 4. Get the acc histogram (T(x))
h3 = get_acc(h2)


# 5. Get the inverse of the acc histogram (T^-1(x))
im2 = im.copy()
pixels = im.load()
for x in range(W):
    for y in range(H):
        output = h3[pixels[x,y]]
        scale = round(output * scales)
        pixels[x,y] = scale
h4 = hist(im)
        


show_hist(x1,h1) # original
show_hist(x1,h2) # normalizado
show_hist(x1,h3) # acumulado
show_hist(x1,h4)

show_img(im,pb=True)     # antes
show_img(im2,pb=True)    # depois























