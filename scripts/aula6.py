import PIL
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# Reading the image
im = PIL.Image.open('images/lgt.jpg')
im = grey(im)

def v_func(x, a=256):
    return np.abs(x-(a/2))          * 4 / np.pow(a,2)

def a_func(x, a=256):
    return (a/2 - np.abs(x-a/2))    * 4 /np.pow(a,2)

# Creating V n-histogram
hv = [v_func(i) for i in range(256)]
x = get_range(256)

# Getting equalized histogram
acc1 = get_acc(hv)      # accumulated map
fm1, im1 = apply_hist(im, acc1) # inverse map

# Getting original n-histogram
h2 = hist(im)
h2 = [i/sum(h2) for i in h2]

# Getting equalized histogram
acc2 = get_acc(h2)      # accumulated map
fm2, im2 = apply_hist(im, acc2) # inverse map




# --- LIST PLOTS ---


o_list = [round(float(x),4) for x in img_to_list(im)]
hv_list = [round(float(x),4) for x in hv]
acc_list = [round(float(x),4) for x in acc1]
fm_list = [round(float(x),4) for x in fm1]

amount = 20
print(f"x (0 to W*H) (showing {amount}):")
print(o_list[:amount])
print("T(x) (0 to 255):")
print(hv_list[:amount])
print("T(x) acc (o to 255):")
print(acc_list[:amount])
print("T(x)^-1 (o to W*H):")
print(fm_list[:amount])

# --- IMG PLOTS ---

fig, axs = plt.subplots(2,3)

# Original image plot

axs[0,0].imshow(im, cmap='gray')
axs[0,0].set_title('Original Image')

axs[1,0].bar(x, hist(im))
axs[1,0].set_title('Original Histogram')

# EQ. image plot

axs[0,1].imshow(im2, cmap='gray')
axs[0,1].set_title('Equalized Image')

axs[1,1].bar(x, hist(im2))
axs[1,1].set_title('EQ. Histogram')

# ESP image plot

axs[0,2].imshow(im1, cmap='gray')
axs[0,2].set_title('ESP Image')

axs[1,2].bar(x, hist(im1))
axs[1,2].set_title('ESP Histogram')

plt.show()

# --- HIST PLOTS ---

fig, axs = plt.subplots(1,4)

axs[0].bar(x, hv)
axs[0].set_title('V Histogram')

axs[1].bar(x, acc1)
axs[1].set_title('Acc Histogram')

axs[2].bar(x, hist(im))
axs[2].set_title('Original Histogram')

axs[3].bar(x, hist(im1))
axs[3].set_title('Equalized Histogram')

plt.show()