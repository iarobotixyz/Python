#-*-coding:utf8;-*-
import datetime
import feedparser
import androidhelper
droid=androidhelper.Android()
minutoAc=0
sismoinicial=0
url='http://www.ssn.unam.mx/rss/ultimos-sismos.xml'
s='RoboticaXYZ'
while True:
    ttmr=datetime.datetime.now().timetuple()
    dtNow=datetime.datetime.now()
    if ttmr[4]!=minutoAc:
        print ("Minuto: ", dtNow)
        rss = feedparser.parse(url)
        if rss.bozo==1:#Error de Conexión SSN
            s="<p>"
        if rss.bozo==0:#Conectado a SSN
            s = rss.entries[0]['description']
        s = s.replace ( "Preliminar: M" , "")
        s = s.replace ( "<p>" , "")
        s = s.replace ( "Fecha:" , "")
        s = s.replace ( "Profundidad:" , "")
        s = s.replace ( "<br />" , "")
        s = s.replace ( "Lat/Lon:" , "")
        s = s.replace ( "</p>" , "")
        s = s.replace ( " " , ",")
        s = s.replace ( "/" , ",")
        array = s.split(',')
        if array[0]==str(dtNow)[0:10]:
            if sismoinicial!=rss.entries[0]['title']:
                n='Nuevo Sismo Registrado'
                arr=rss.entries[0]['title'].split(',')
                print(n+"\nFecha", array[0]+" "+array[1])
                print ("Latitud: ", array[5])
                print ("Longitud: ", array[6])
                sismoinicial=rss.entries[0]['title']
                q=n+' a las '+array[1]
                t=' en el Estado de'+arr[2]+' con p'
                u='rofundidad de '+array[7]+' kilometro'
                v='s en la Dirección '+arr[1]+' y una m'
                w='agnitud de '+arr[0]+' grados Richter'
                result=droid.ttsSpeak(q+t+u+v+w)
                print(q+t+u+v+w)
            if array[1][0:5]==str(dtNow)[11:16]:
                x='Misma Hora del Sismo '
                y=rss.entries[0]['title']
                z='No corro, No grito, No empujo, Salir'
                print(x+y+z)
                result=droid.ttsSpeak(x+y+z)
        minutoAc=ttmr[4]
