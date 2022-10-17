#https://iarobotxyz.blogspot.com/2022/10/juego-el-ahorcado-en-python-con.html?m=1
import random
import os
import androidhelper
droid=androidhelper.Android()
palabras = 'juego python robot robotica'.split()
palabras += 'arduino microcontrolador pic '.split()
AHORCADO = ['''
      +___+
      |   |
          |
          |
          |
    _________
    =========''', '''
      +___+
      |   |
      O   |
          |
          |
    _________
    =========''', '''
      +___+
      |   |
      O   |
      |   |
          |
    _________
    =========''', '''
      +___+
      |   |
      O   |
     /|   |
          |
    _________
    =========''', '''
      +___+
      |   |
      O   |
     /|\  |
          |
    _________
    =========''', '''
      +___+
      |   |
      O   |
     /|\  |
     /    |
    _________
    =========''', '''
      +___+
      |   |
      O   |
     /|\  |
     / \  |
    _________
    =========''']
 
def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]
 
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print (' Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (" "+letra, fin)
    print ("___________________")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: 
        print (" "+letra, fin)
    print ("")
 
def elijeLetra(algunaLetra):
    while True:
        adiv=' Adivina una letra: '
        print(adiv)
        result=droid.ttsSpeak(adiv)
        letra = input()
        say=droid.recognizeSpeech(None,None,None)
        if say.result:
            letra=str(say.result)
        print(letra)
        letra = letra.lower()
        if len(letra) != 1:
            intro='Introduce una sola letra.'
            print (intro) 
            result=droid.ttsSpeak(intro)
        elif letra in algunaLetra:
            print ('\nYa has elegido esa letra')
            print ('¿Intenta con otra?\n')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    new='Deseas jugar nuevamente? (Si o No)'
    print(new)
    result=droid.ttsSpeak(new)
    return input().lower().startswith('s')

print (' J U E G O - A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    letra=elijeLetra(letraIncorrecta + letraCorrecta)
    os.system('clear')
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            excel=' ¡Excelente!\nLa palabra secreta es "'
            excel+= palabraSecreta + '"!\n¡Has ganado!'
            print(excel)
            result=droid.ttsSpeak(excel)
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            fail='¡Ups.. Se ha quedado sin letras!\n'
            print(fail)
            print('Despues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            result=droid.ttsSpeak(fail)
            finJuego = True
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break
    