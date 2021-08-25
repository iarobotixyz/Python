#https://iarobotxyz.blogspot.com
import serial
import time
ser = serial.Serial(
    port='/dev/cu.wchusbserial410',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
print("Conectado: " + ser.portstr)
seq = []
while True:
    for c in ser.read():
        seq.append(chr(c)) 
        joined_seq = ''.join(str(v) for v in seq)
        if chr(c) == '\n':
            print("Linea : " + joined_seq)
            seq = []
            break
ser.close()




