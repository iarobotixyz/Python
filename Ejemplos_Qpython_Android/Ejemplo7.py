#-*-coding:utf8;-*-
#qpy:console
import datetime
import feedparser
import androidhelper
droid=androidhelper.Android()
u0='http://www.banxico.org.mx/rsscb/rss?BMXC_canal'
u1=u0+'=pagos&BMXC_idioma=es'
u2=u0+'=fix&BMXC_idioma=es'
minutoAc=0
while True:
    ttmr=datetime.datetime.now().timetuple()
    if ttmr[4]!=minutoAc:
        uno=feedparser.parse(u1)
        dos=feedparser.parse(u2)
        if uno.bozo==0:
            su='<p>'
        if uno.bozo==1:
            for postu in uno.entries:
                su=(postu.title)
            su=su.replace ( "MX:" , "")
            su=su.replace ( "MXN" , ",")
            print ("Conectado a banxico\n", su)
        if dos.bozo==0:
            sd='<p>'
        if dos.bozo==1:
            for postd in dos.entries:
                sd=(postd.title)
            sd=sd.replace ( "MX:" , "")
            sd=sd.replace ( "MXN" , ",")
            print ("Conectado a banxico\n", sd)
        com='Compra:'+sd[0]+sd[1]+sd[2]+sd[3]+sd[4]+sd[5]
        print (com+sd[6]+sd[7])
        result=droid.ttsSpeak(com)
        ven='Venta:'+su[0]+su[1]+su[2]+su[3]+su[4]+su[5]
        print (ven+su[6]+su[7])
        result=droid.ttsSpeak(ven)
        minutoAc=ttmr[4]
