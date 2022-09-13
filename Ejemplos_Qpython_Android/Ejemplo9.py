import androidhelper
droid=androidhelper.Android()
dir="scripts3/"
archivo="robotica.txt"
with open(dir+archivo) as f:
    lin=f.readlines()
    print(lin)
    result=droid.ttsSpeak(str(lin))
