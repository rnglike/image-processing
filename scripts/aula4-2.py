from PIL import Image
import matplotlib.pyplot as plt

imagem = Image.open('./af.jpeg').convert('L')

pixels = imagem.load()

largura, altura = imagem.size

img_neg = Image.new('L', (largura, altura))
pixels_neg = img_neg.load()

for i in range(largura):
    for j in range (altura):
        valor_pixel = pixels[i, j]
        pixels_neg[i, j] = 255 - valor_pixel
        
hist_original = [0] * 256
hist_neg = [0] * 256

for i in range(largura):
    for j in range (altura):
        hist_original[pixels[i, j]] += 1
        hist_neg[pixels_neg[i, j]] += 1

# img
plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap = 'gray')
plt.title("Imagem original")
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(img_neg, cmap = 'gray')
plt.title("Imagem neg")
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
plt.plot(hist_neg, color = 'red')
plt.title("Hist da Imagem modificada")
plt.xlabel("Intensidade de Cinza")
plt.ylabel("Num de pixels")

plt.tight_layout()
plt.show()