import PIL
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
from utils import *

def add_padding(pixels, W, H):

    new_pixels = np.zeros((W+1, H+1))
    for x in range(W):
        for y in range(H):
            new_pixels[x+1, y+1] = pixels[x, y]
            
    new_pixels = np.transpose(new_pixels)

    return new_pixels

im = PIL.Image.open('images/R.jpg')
im = grey(im)

W, H = im.size
pixels = im.load()

# laplacian mask
mask = np.array([
                    0,  1,  0,
                    1, -4,  1,
                    0,  1,  0
                ])

pixels = add_padding(pixels, W, H)
im = PIL.Image.fromarray(pixels)

pixels = im.load()
new_pixels = np.zeros((W+1, H+1))

for x in range(W):
    for y in range(H):

        if x+1 > W-1 or y+1 > H-1:
            break

        window = []
        for i in range(3):
            for j in range(3):
                    
                window.append(pixels[x+i, y+j])

        edge = np.sum(window * mask)

        # treat the edges
        if edge < 0:
            edge = 0
        
        new_pixels[x+1, y+1] = edge
        
new_pixels = np.transpose(new_pixels)
im = PIL.Image.fromarray(new_pixels)
show_img(im, pb=True)