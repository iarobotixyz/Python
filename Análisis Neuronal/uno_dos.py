import cv2
gray = cv2.imread('neurona.tif', cv2.IMREAD_GRAYSCALE)#abre imagen
cv2.imshow('Original', gray)#Muestra Imagen
cv2.imwrite("Original.tif",gray)#Guarda Imagen
cv2.waitKey(0)