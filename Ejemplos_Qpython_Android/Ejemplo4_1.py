#https://iarobotxyz.blogspot.com/2022/06/introduccion-python-con-android-ejemplo_13.html
import androidhelper
import time
import qpy
droid = androidhelper.Android()
fecha=time.strftime("%e_%B_%Y_%H_%M_%S")
dir="scripts3/"
archivo="txt_"+str(fecha)+".txt"
print ("Nombre del Archivo: "+archivo)
while True:
    say=droid.recognizeSpeech(None,None,"test")
    with open(dir+archivo,"a") as obj:
        if say.result:
            obj.write("\n"+say.result)

        if say.result=='detener' or say.result=='salir':
            break
