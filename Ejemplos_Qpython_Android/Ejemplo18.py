dir="scripts3/"
archivo="robotica.txt"
with open(dir+archivo) as f:
    lin=f.readlines()
    lin=str(lin).replace ("\\n", "")
    lin=str(lin).replace ("'", "")
    print(lin)
cadPa =str(lin)
listPa = cadPa.split()
frePalab = []
for i in listPa:
    frePalab.append(listPa.count(i))
print("Cadena: \n" + cadPa +"\n")
print("Lista: \n" + str(listPa) + "\n")
print("Frecuencias: \n" + str(frePalab) + "\n")
print("Pares: \n")
print(str(list(zip(listPa, frePalab))))
