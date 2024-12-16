import PIL
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