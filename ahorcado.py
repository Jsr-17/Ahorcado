
def juego(palabra='palabra',acertada=False,palabraJuego='',array=[],arrayno=[]):


    print("Hola este es el juego del ahorcado tienes que adivinar una palabra")

    print("La palabra es la siguiente: ")
    
    for i in palabra:
        print("-",end=" ")
    while not acertada :
        esta=False
        letra=input("\nIntroduzca una letra:  ")

        for i in range(len(palabra)):
            if letra == palabra[i]:
                print("\nEsa palabra se encuentra")
                array.append(letra)
                esta=True
                break
        if not esta:
            arrayno.append(letra)

        print("\nLetras encontradas:\n")
        for i in range(len(array)):
                print(array[i],end=' ')
        print("\n \nLetras no  encontradas:\n")

        for i in range(len(arrayno)):
                print(arrayno[i],end=' ')
        

        palabraJuego=''
        for i in range(len(palabra)):
            if palabra[i] in array:

                palabraJuego+=palabra[i]

            else:
                palabraJuego+='-'

        print(palabraJuego)
        if palabraJuego==palabra:
            acertada=True

juego()