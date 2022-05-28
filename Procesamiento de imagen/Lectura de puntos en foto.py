import cv2
import numpy as np

circles = np.zeros([2,2], dtype = int)  # Declarar una matriz de 2x2 para guardar ambas coordenadas
counter = 0

 
def mousePoints(event,x,y,flags,params):       #Define una clase con parametros
    global counter                                          # Variable global
    if event == cv2.EVENT_LBUTTONDOWN: #If click con el izq
        circles[counter] = x,y                             #Guarda la coordenada en el primer espacio de la matriz
        counter = counter + 1                            # Aumenta 1, para poder guardar en el segundo espacio de la matriz
        if counter==2:    
            print(circles)
            pt1=(circles[0,0], circles[0,1]) #Saca los valores de la matriz
            pt2=(circles[1,0], circles[1,1])   #Saca los valores de la matriz
            img_mod=cv2.line(img, (pt1), (pt2), (0,0,255), 2)
            #(imagen, (coordenada 1), (Coordenada 2), (RGB de la linea), (Grosor))
            cv2.imshow("Line",img_mod)
            
img=cv2.imread('Monstera.jpg') #Llamar la imagen
cv2.imshow('Test',img) # Mostrar la imagen
cv2.setMouseCallback('Test', mousePoints)


#Trazar la linea que conecte a los dos puntos
#Sacar las escalas dentro de esa linea 

cv2.waitKey(0)
        
