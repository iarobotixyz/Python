import cv2
gray = cv2.imread('neurona.tif', cv2.IMREAD_GRAYSCALE)#abre imagen
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)#convierte imagen a binario
t, dsti = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)#convierte imagen a binario invertido
t, dti = cv2.threshold(gray, 170, 255, cv2.THRESH_TRUNC)#convierte imagen a diferencia de pixel

cv2.imshow('Original', gray)#Muestra Imagen
cv2.imwrite("Original.tif",gray)#Guarda Imagen
cv2.imshow('Binario', dst)#Muestra Imagen
cv2.imwrite("Binario.tif",dst)#Guarda Imagen
cv2.imshow('Binario_Invertido', dsti)#Muestra Imagen Binario Invertido
cv2.imwrite("Binario_Invertido.tif",dsti)#Guarda Imagen Binario Invertido
cv2.imshow('Binario_DPixel', dti)#Muestra Imagen Binario Invertido
cv2.imwrite("Binario_DPixel.tif",dti)#Guarda Imagen Binario Invertido

cv2.waitKey(0)