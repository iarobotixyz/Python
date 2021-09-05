#https://iarobotxyz.blogspot.com
import serial
import time
import json
from mpl_toolkits.mplot3d import axes3d

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


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
                    
                fig = plt.figure(figsize=(7, 7))
                ax = fig.add_subplot(1, 1, 1, aspect=1)

                ax.set_xlim(-5, 15)
                ax.set_ylim(-5, 15)

                ax.tick_params(which='major', width=1.0)
                ax.tick_params(which='major', length=10)
                ax.tick_params(which='minor', width=1.0, labelsize=10)
                ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

                ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
             
                #ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
                ax.set_title('Temperatura: '+str(lista[9]), fontsize=20)
                ax.set_xlabel("X axis ")
                ax.set_ylabel("Y axis ")

                ax.legend()

                def circle(x, y, radius=0.25):
                    from matplotlib.patches import Circle
                    from matplotlib.patheffects import withStroke
                    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=2,
                                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                                    path_effects=[withStroke(linewidth=5, foreground='w')])
                    ax.add_artist(circle)


                def text(x, y, text):
                    ax.text(x, y, text, backgroundcolor="white",
                            ha='center', va='top', weight='bold', color='red')
                def text2(x, y, text):
                    ax.text(x, y, text, backgroundcolor="white",
                            ha='center', va='top', weight='bold', color='blue')

                # Z Label acelerometro
                circle(int(lista[3])/70, 5.27)
                text2(int(lista[3])/70, 5.45, "Z Acelerometro "+lista[3])
                
                # X Label acelerometro
                circle(int(lista[1])/70, 5.27)
                text2(int(lista[1])/70, 5.45, "X Acelerometro "+lista[1])

                # Y Label
                circle(0, int(lista[2])/15.8)
                text2(0, int(lista[2])/15.6, "Y Acelerometro "+lista[2])

                # XY Label
                circle(int(lista[1])/70, int(lista[2])/15.8)
                text2(int(lista[1])/70, int(lista[2])/15.6, "X+Y Acelerometro "+lista[1]+" , "+lista[2])


                # Z Label giro
                circle(int(lista[7])/70, 5.27)
                text(int(lista[7])/70, 5.45, "Z Giroscopio "+lista[7])
                
                # X Label giro
                circle(int(lista[5])/70, 5.27)
                text(int(lista[5])/70, 5.45, "X Giroscopio "+lista[5])

                # Y Label
                circle(0, int(lista[6])/15.8)
                text(0, int(lista[6])/15.6, "Y Giroscopio "+lista[6])

                # XY Label
                circle(int(lista[5])/70, int(lista[6])/15.8)
                text(int(lista[5])/70, int(lista[6])/15.6, "X+Y Giroscopio "+lista[5]+" , "+lista[6])

                # Mostramos el gráfico
                plt.show(block=False)
                plt.pause(0.001) # Pause for interval seconds.
                #input("hit[enter] to end.")
                plt.close('all') # all open plots are correctly closed after each run

                #plt.close(1)
            else:
                print("Cadena Incompleta")
            a = []
            break
ser.close()




