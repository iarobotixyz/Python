#-*-coding:utf8;-*-
#qpy:console
import androidhelper
import time

droid=androidhelper.Android()

texto='hola,por favor ingresa tu nombre';
result=droid.ttsSpeak(texto)

n1=input("Ingresa tu Nombre: ");

print ("Bienvenido ",n1);
result=droid.ttsSpeak("Bienvenido "+n1)

time=time.strftime("%I %M %p, %Y")

print ("La hora es: ",time);
result=droid.ttsSpeak("La hora es"+time)

