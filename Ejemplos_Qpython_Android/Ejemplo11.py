dir="scripts3/"
archivo="python.txt"
vocales=('a','e','i','o','u')
def numero_vocales(frase):
    a=0
    e=0
    i=0
    o=0
    u=0
    for c in frase:
        if c=='a' or c=='A':
            a=a+1
        if c=='e' or c=='E':
            e=e+1
        if c=='i' or c=='I':
            i=i+1
        if c=='o' or c=='O':
            o=o+1
        if c=='u' or c=='U':
            u=u+1
    return a,e,i,o,u
with open(dir+archivo) as f:
    lin=f.readlines()
    print(lin)
    texto=(str(lin)).lower()
    print(vocales)
    print(numero_vocales(texto))
    for letra in vocales:
        texto=texto.replace(letra, "")
    print(texto)
