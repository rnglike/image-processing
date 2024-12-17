import PIL
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

# Return black and white image
def grey(img):
    return img.convert('L') # TODO: Convert manually

# Returns a histogram representing the occurencies of the pixel of an image
def hist(img):
    
    hist = 256 * [0]
    px = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            hist[px[i,j]] += 1
            
    return hist
            
# Returns a range of ints, from 0 to r
def get_range(r):
    x = r * [0]
    for i in range(r):
        x[i] = i
    return x

# 
def hist_multichannel(img):
    
    r, g, b = img.split()

    x = get_range(256)

    hr_label = "Red Channel"
    hg_label = "Green Channel"
    hb_label = "Blue Channel"

    hr = hist(r)
    hg = hist(g)
    hb = hist(b)

    hs = [hr, hg, hb]
    hs_label = [hr_label, hg_label, hb_label]

    fig, axs = plt.subplots(2,2)
    
    axs[0,0].imshow(img)
    axs[0,0].set_title('Image')
    
    for h, label in zip(hs, hs_label):
        
        # TODO: divide the channels in each plot
        
        axs[0,1].bar(x, h)
        axs[0,1].set_title(label)
    
    plt.show()

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
        if i == 0:
            a[i] = y
        else:
            a[i] = a[i-1] + y
    return a

def apply_hist(im, h3):

    W,H = im.size
    x1 = get_range(256)

    scales = len(x1)

    # 5. Get the inverse of the acc histogram (T^-1(x))
    im2 = im.copy()
    pixels = im2.load()
    final_map = []
    for x in range(W):
        for y in range(H):
            output = h3[pixels[x,y]]
            scale = round(output * (scales-1))
            pixels[x,y] = scale
            final_map.append(scale)

    return final_map, im2

def img_to_list(im):

    W,H = im.size
    pixels = im.load()
    map = []
    for x in range(W):
        for y in range(H):
            map.append(pixels[x,y])
    return map

def kernel_apply(im, kernel, operation):

    pixels = im.load()
    W, H = im.size
    kernel_size = kernel.shape[0]
    new_pixels = np.zeros((W, H))

    if kernel_size//2 == kernel_size/2:
        raise ValueError('Kernel size must be odd')

    for x in range(W):
        for y in range(H):

            offset = kernel_size//2
            mx = x + offset
            my = y + offset

            if mx > (W-1) - offset or my > (H-1) - offset:
                break

            window = np.zeros((kernel_size, kernel_size))
            for i in range(kernel_size):
                for j in range(kernel_size):
                        
                    wx = x + i
                    wy = y + j
                    window[i, j] = pixels[wx, wy]

            px = pixels[mx, my]

            match operation:
                case 'filter':

                    px = np.sum(window * kernel)
                    px = np.max([0, np.min([255, px])]) # thresholding

                case 'morphological':

                    # check if kernel is binary
                    if not np.all((kernel == 0) | (kernel == 1)):
                        raise ValueError('Kernel must be binary')

                    # check if smallest window value is 0 or largest is 255
                    if np.min(window) < 0 or np.max(window) > 255:
                        raise ValueError('Window must be binary')

                    px = 0
                    # check if window is a match
                    if np.all(window*kernel == kernel*255):
                        px = 255
    
            new_pixels[mx, my] = px
            
    new_pixels = np.transpose(new_pixels)
    im = PIL.Image.fromarray(new_pixels)
    return im

def erosion_mask(size, format='square'):
    
    match format:

        case 'square':
            mask = np.ones((size, size))
        case 'cross':
            mask = np.zeros((size, size))
            for i in range(size):
                mask[i, size//2] = 1
                mask[size//2, i] = 1
        case 'circle':
            mask = np.zeros((size, size))
            for i in range(size):
                for j in range(size):
                    if (i-size//2)**2 + (j-size//2)**2 <= (size//2)**2:
                        mask[i, j] = 1
                        
    return mask