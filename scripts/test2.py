from utils import *

def add_padding(im):

    pixels = im.load()
    W, H = im.size

    new_pixels = np.zeros((W+1, H+1))
    
    for x in range(W):
        for y in range(H):
            new_pixels[x+1, y+1] = pixels[x, y]
            
    new_pixels = np.transpose(new_pixels) # fix orientation
    padded_im = PIL.Image.fromarray(new_pixels)

    return padded_im

# laplacian mask
lap_kernel = np.array([
                    0,  1,  0,
                    1, -4,  1,
                    0,  1,  0
                ])

im = PIL.Image.open('images/hole.jpg')
im = grey(im)
im = add_padding(im)

# kernel = erosion_mask(11, 'square')
im = kernel_apply(im, lap_kernel, 'filter')

show_img(im, pb=True)