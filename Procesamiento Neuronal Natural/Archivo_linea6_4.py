#https://iarobotxyz.blogspot.com/2020/11/procesamiento-neuronal-natural.html
import cv2
import numpy as np
import time
import datetime

img = cv2.imread('neurites.tif', cv2.IMREAD_COLOR)
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
f = open("Neurona_CompaXYZ-"+str(st)+".txt",'a')
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s = str(st)+" - \n"
f.write(s)
s = "Coordenadas\n x1,y1 - x2,y2 \n"
f.write(s)
# Dibuja lineas
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 200), 1)#Azul Verde Rojo 4Ancho
    if x1==x2:
    	cv2.circle(img,(x2, y2), 6, (255,255,0), 2)#Circulo azulverde
    if y1==y2:
    	cv2.circle(img,(x2, y2), 6, (250,0,250), 2)#Circulo rosa
    cv2.circle(img,(x2, y2), 5, (255,0,0), 1)#Circulo Azul
    cv2.circle(img,(x1, y1), 5, (0,200,0), 1)#Circulo verde    
    s = str(x1)+","+str(y1)+" - "+str(x2)+","+str(y2)+" \n"
    f.write(s)
f.close()

# Muestra Resultado
#img = cv2.resize(img, dsize=(1080, 700)) #Ajuste de pantalla
cv2.imshow("Resultado Neurona", img)
cv2.imwrite("DenNeuronaNodosCompa34.tif",img)#Guarda Imagen Binario Invertido


#Tecla Espacio para terminar el programa
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()