import PIL
from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt


imagem = PIL.Image.open('./af.jpeg').convert('L')

enhancer = ImageEnhance.Brightness(imagem)
img_mod = enhancer.enhance(2)

img_array = np.array(imagem)
img_mod_array = np.array(img_array)

img_mod_array = np.clip(img_mod_array * 2, 0, 255).astype(np.uint8)

img_mod = Image.fromarray(img_mod_array)

hist_original = np.array(imagem.histogram())
hist_mod = np.array(img_mod.histogram())

# img
plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap = 'gray')
plt.title("Imagem original")
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(img_mod, cmap = 'gray')
plt.title("Imagem modificada")
plt.axis('off')

plt.tight_layout()
plt.show()

# hist
plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.plot(hist_original, color = 'black')
plt.title("Hist da Imagem original")
plt.xlabel("Intensidade de Cinza")
plt.ylabel("Num de pixels")


plt.subplot(1, 2, 2)
plt.plot(hist_mod, color = 'red')
plt.title("Hist da Imagem modificada")
plt.xlabel("Intensidade de Cinza")
plt.ylabel("Num de pixels")

plt.tight_layout()
plt.show()