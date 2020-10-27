import cv2
gray = cv2.imread('neurona.tif', cv2.IMREAD_GRAYSCALE)#abre imagen
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)#convierte imagen a binario
cv2.imshow('Original', gray)#Muestra Imagen
cv2.imwrite("Original.tif",gray)#Guarda Imagen
cv2.imshow('Binario', dst)#Muestra Imagen
cv2.imwrite("Binario.tif",dst)#Guarda Imagen
cv2.waitKey(0)