#Procesamiento de imagen.
from cv2 import cv2
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img =plt.imread('Monstera.JPG') #Lee la imagen
plt.imshow(img) #Enseña la imagen
plt.show()

R,G,B=img[:,:,0],img[:,:,1], img[:,:,2] #Se declara una matriz RGB para la imagen
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B #Valores para la matriz 
plt.imshow(imgGray,cmap='gray') #Se muestra la imagen en escala de grises
plt.show()


