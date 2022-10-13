dir="scripts3/"
archivo="Robotica.txt"
with open(dir+archivo) as f:
    lin=f.readlines()
    lin=str(lin).replace ("\\n", "")
    lin=str(lin).replace ("'", "")
    lin=str(lin).replace ("[", "")
    lin=str(lin).replace ("]", "")
    print(lin)
cadPa =str(lin)
listPa = cadPa.split()
frePalab = []
orden=[]
for i in listPa:
    frePalab.append(listPa.count(i))
print("Cadena: \n" + cadPa +"\n")
print("Lista: \n" + str(listPa) + "\n")
print("Frecuencias: \n" + str(frePalab) + "\n")
print("Pares: \n")
orden=str(list(zip(listPa, frePalab)))
print(orden+"\n")
zipped = list(zip(listPa, frePalab))
res = sorted(zipped, key=lambda x: x[1], reverse=True) 
print("Lista Final: \n", str(res)) 
print("\nResultado Analisis txt Palabras:\n")
result = []
for item in res:
    if item not in result:
        result.append(item)
print(result)
