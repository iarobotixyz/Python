#-*-coding:utf8;-*-
#qpy:console
import androidhelper
import time
import qpy
droid = androidhelper.Android()
fecha=time.strftime("%A_%e_%B_%Y")
dir="scripts3/"
archivo="texto_"+str(fecha)+".txt"
print ("Nombre del Archivo: "+archivo)
while True:
    say=droid.recognizeSpeech(None,None,"test")
    with open(dir+archivo,"a") as obj:
        if say.result:
            obj.write("\n"+say.result)

        if say.result == 'detener':
            break
