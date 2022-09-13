import androidhelper
import qpy
import time
fecha=time.strftime("%A_%e_%B_%Y")
droid=androidhelper.Android()
ruta=qpy.tmp+"/Video_"+str(fecha)+".mp4"
droid.recorderCaptureVideo(ruta,5,True)
droid.recorderStop()
