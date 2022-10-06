import subprocess
i=1 #intentos
ipdetectada=[]
for ping in range(64,254):
    print("___ Inicio de Ciclo___")
    address="192.168.1." + str(ping)
    res=subprocess.call(['ping', '-c', str(i), address])
    print("--- Comparativa ---")
    if res == 0:
        print( "Ping de la dirección: ",address, "--OK")
        print("Almacenamiento")
        ipdetectada.append(address)
    elif res == 2:
        print("No responde la dirección: ", address)
    else:
        print(address, "Ping Fallando!")
if ipdetectada:
    print ("Hizo Ping en: ")
    print (ipdetectada)
