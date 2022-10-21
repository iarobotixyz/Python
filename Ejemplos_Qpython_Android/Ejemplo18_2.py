#https://iarobotxyz.blogspot.com/2022/10/contador-de-palabras-de-un-archivo-de.html
dir="scripts3/"
archivo="robotica.txt"
word_list1=["",'el','la','los','las','un','una','unos',
'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 
'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 
'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya',
 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 
 'son', 'solo', 'tengo', 'muy']
def stem_text(text):
    text = text.split()
    temp = [word_list1[0] if i in word_list1 else i for i in text]
    text = ' '.join(temp)
    return text
with open(dir+archivo) as f:
    lin=f.readlines()
    lin=str(lin).replace ("\\n", "")
    lin=str(lin).replace ("'", "")
    lin=str(lin).replace (",", "")
    lin=str(lin).replace (".", "")
    lin=str(lin).replace ("[", "")
    lin=str(lin).replace ("]", "")
    print(lin)
    lin=lin.lower()
    lin=stem_text(lin)
    print(lin)
cadPa =str(lin)
listPa = cadPa.split()
frePalab = []
orden=[]
for i in listPa:
    frePalab.append(listPa.count(i))
orden=str(list(zip(listPa, frePalab)))
zipped = list(zip(listPa, frePalab))
res = sorted(zipped, key=lambda x: x[1], reverse=True) 
print("\nResultado Analisis txt Palabras:\n")
result = []
for item in res:
    if item not in result:
        result.append(item)
print(result)
print("\nListado del arreglo: ")
for i in result:
    for j in i:
        print('  -',j, end="")
    print()
