#https://iarobotxyz.blogspot.com/
import androidhelper
import time
droid=androidhelper.Android()
NombreAsistente='siri'
#NombreAsistente='alexa'
#NombreAsistente='jarvis'
n='RoboticaXYZ'
frasehora=' dame la hora'
result=droid.ttsSpeak(n+"Bienvenido al Asistente de Voz")
time.sleep(2)
while True:
    say=droid.recognizeSpeech(None,None,None)
    if say.result:
        lin=say.result.lower()
        if lin==str(NombreAsistente+frasehora):
            print("\n"+lin)
            time=time.strftime("%I %M %p, %Y")
            print ("La hora es: ",time);
            result=droid.ttsSpeak("La hora es"+time)
        if say.result=='detener' or say.result=='salir':
            break
