import time
from androidhelper import Android
droid=Android()
droid.batteryStartMonitoring()
droid.makeToast('Informacion de la Batería')
droid.vibrate(1000)
while True:
    bdata=droid.readBatteryData()
    print(bdata.result)
    bstatus=droid.batteryGetStatus().result
    bhealth=droid.batteryGetHealth().result
    bplug=droid.batteryGetPlugType().result
    bcheck=droid.batteryCheckPresent().result
    blevel=droid.batteryGetLevel().result
    bvoltage=droid.batteryGetVoltage().result
    btemperature=droid.batteryGetTemperature().result
    btechnology=droid.batteryGetTechnology().result
    print("Estado: "+str(bstatus))
    print("Salud: "+str(bhealth))
    print("Conector: "+str(bplug))
    print("checkpresent: "+str(bcheck))
    print("Nivel: "+str(blevel))
    print("Voltaje: "+str(bvoltage))
    print("Temperatura: "+str(btemperature))
    print("Tecnología: "+str(btechnology))
    time.sleep(1)
droid.batteryStopMonitoring()
