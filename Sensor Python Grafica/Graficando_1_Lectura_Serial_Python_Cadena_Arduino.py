#https://iarobotxyz.blogspot.com
import serial
import time
import json

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



ser = serial.Serial(
    port='/dev/cu.wchusbserial410',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
print("Conectado: " + ser.portstr)
a = []
lista = [0,0,1,0,0,1,0,1,0]
time.sleep(1)
while True:
    for c in ser.read():
        a.append(chr(c)) 
        joined_seq = ''.join(str(b) for b in a)
        if chr(c) == '\n':
            data = json.dumps(joined_seq)
            cad = json.loads(data)
            #{"AceleracionXYZ",964,-78,178,"GiroscopioXYZ":-309,222,107,"TempC",22.48}
            formato = "{}".format(cad)
            lista = formato.split(",")
            print("Numero de elementos en la cadena Arduino: ", len(lista))
            if len(lista)==10:
                print(formato)
                print ("---- Ciclo----")
                print(lista[0])#AceleracionXYZ
                print(" X - "+lista[1])
                print(" Y - "+lista[2])
                print(" Z - "+lista[3])
                print(lista[4])#GiroscopioXYZ
                print(" X - "+lista[5])
                print(" Y - "+lista[6])
                print(" Z - "+lista[7])
                print(lista[8])#Temperatura
                print(" C - "+lista[9])
                

               ##Dibujar Piso
                fig = plt.figure()
                #fig = plt.figure(figsize=(7, 7))
                ax1 = fig.add_subplot(111, projection='3d')
                ax1.set_title('Temperatura: '+lista[9])
                # Definimos los datos
                x3 = [10,9,8,7,6,5,7,8,9,1]
                y3 = [10,9,7,8,2,5,6,3,7,2]
                z3 = [10,9,7,8,2,5,6,3,7,2]

                dx = [1,6,7,8,2,5,6,3,7,2]
                dy = [1,6,7,8,2,5,6,3,7,2]
                dz = [1,2,3,4,5,6,2,3,4,1]

                ax1.bar3d(int(lista[5])+500, dy, dz, x3, y3, z3, shade=True)
                
###############################################
                # fake data
                _x = np.arange(int(lista[5])+500)
                _y = np.arange(7)
                _xx, _yy = np.meshgrid(_x, _y)
                x, y = _xx.ravel(), _yy.ravel()
                top = x + y
                #top = int(lista[3])
                bottom = np.zeros_like(top)
                width = depth = 1
                ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
  ###########################################################              
               
                plt.show(block=False)
                plt.pause(0.001) # Pause for interval seconds.
                #input("hit[enter] to end.")
                plt.close('all') 
            else:
                print("Cadena Incompleta")
            a = []

            break
ser.close()




