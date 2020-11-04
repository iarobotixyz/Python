#https://iarobotxyz.blogspot.com/2020/11/procesamiento-neuronal-natural.html
import cv2
import numpy as np
import time
import datetime

img = cv2.imread('Original.tif', cv2.IMREAD_COLOR)
# Convierte la imagen escala gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
# Detecta 
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=300)
#lines = cv2.HoughLinesP(edges,rho = 1,theta = 1*np.pi/180,threshold = 100,minLineLength = 100,maxLineGap = 50) 
#lines = cv2.HoughLinesP(gray, rho=1, theta=np.pi/360, threshold=10, minLineLength=10, maxLineGap=20)#Muchas Lineas
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=10, minLineLength=10, maxLineGap=20)

#lines = cv2.HoughLinesP(edges,rho = 1,theta = 1*np.pi/180,threshold = 100,minLineLength = 100,maxLineGap = 50) 

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
f = open("Neurona_InfoXYZ-"+str(st)+".txt",'a')
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s = str(st)+" - \n"+str(lines)+"\n"
f.write(s)
f.close()

# Dibuja lineas
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)#Azul Verde Rojo 5Ancho

# Muestra Resultado
#img = cv2.resize(img, dsize=(1080, 700)) #Ajuste de pantalla
cv2.imshow("Resultado Neurona", img)
cv2.imwrite("LineaNeuronaArchivoOriginal.tif",img)#Guarda Imagen Binario Invertido


#Tecla Espacio para terminar el programa
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()