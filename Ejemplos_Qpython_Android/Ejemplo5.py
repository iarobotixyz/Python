#-*-coding:utf8;-*-
import androidhelper
import time
import json
from colorama import init
init()
from colorama import Fore, Back, Style
droid = androidhelper.Android()
droid.startSensingTimed(1, 250)
while True:
    rea=droid.sensorsReadAccelerometer().result
    li=droid.sensorsGetLight().result
    ac=droid.sensorsGetAccuracy().result
    sen=droid.readSensors().result
    res=json.dumps(rea, ensure_ascii=False)
    y=json.loads(res)
    print(Back.GREEN+'Cadena:'+str(sen))
    print(Style.RESET_ALL)
    print(Fore.RED+str(rea))
    print (Fore.RED+'Fuerza X: '+str(y[0]))
    print (Fore.RED+'Fuerza Y: '+str(y[1]))
    print (Fore.RED+'Fuerza Z: '+str(y[2]))
    print(Style.RESET_ALL)
    print(Fore.BLUE + ' Precisión: '+str(ac))
    print(Fore.YELLOW+' Sensor de Luz: '+str(li))
    time.sleep(0.5)
droid.stopSensing()
