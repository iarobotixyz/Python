#https://iarobotxyz.blogspot.com/2020/10/proyecto-analisis-neuronal.html
import numpy as np
import cv2

img = cv2.imread('Binario_Invertido.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, bin_img = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)

minLineLength = 100
maxLineGap = 100
lines = cv2.HoughLinesP(bin_img, 2, np.pi/180,70,minLineLength,maxLineGap)

lines = [x.flatten() for x in lines]

# dibuja lineas
for line in lines:
    x1,y1,x2,y2 = line
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite("Binario_Linea2_INV_1.tif",img)