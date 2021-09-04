#https://iarobotxyz.blogspot.com
import serial
import time
import json
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
            else:
                print("Cadena Incompleta")
            a = []
            break
ser.close()




