from samsungtvws import SamsungTVWS
import os
import androidhelper
droid = androidhelper.Android()
dir=os.path.realpath(__file__)
token_file=os.path.dirname(str(dir))+'/token_tv.txt'
hostTV='192.168.1.94'
tv=SamsungTVWS(hostTV, port=8002, token_file=token_file)
while True:
    say=droid.recognizeSpeech(None,None,None)
    if say.result=='Apagar' or say.result=='encender':
        tv.shortcuts().power()
    if say.result=='enter' or say.result=='entrar':
        tv.shortcuts().enter()
    if say.result=='ver' or say.result=='observar':
        tv.shortcuts().enter()
    if say.result=='inicio' or say.result=='home':
        tv.shortcuts().home()
    if say.result=='regresar' or say.result=='atrás':
        tv.shortcuts().back()
    if say.result=='Subir volumen':
        tv.shortcuts().volume_up()
    if say.result=='bajar volumen':
        tv.shortcuts().volume_down()
    if say.result=='arriba':
        tv.shortcuts().up()
    if say.result=='abajo':
        tv.shortcuts().down()
    if say.result=='izquierda':
        tv.shortcuts().left()
    if say.result=='derecha':
        tv.shortcuts().right()
    if say.result=='informacion':
        tv.shortcuts().info()
    if say.result=='guía':
        tv.shortcuts().guide()
    if say.result=='menú':
        tv.shortcuts().menu()
    if say.result=='herramientas':
        tv.shortcuts().tools()
    if say.result=='canal arriba':
        tv.shortcuts().channel_up()
    if say.result=='canal abajo':
        tv.shortcuts().channel_down()
    if say.result=='silencio' or say.result=='mute':
        tv.shortcuts().mute()
    if say.result=='fuente' or say.result=='origen':
        tv.shortcuts().source()
    if say.result == 'salir' or say.result=='detener':
        break
