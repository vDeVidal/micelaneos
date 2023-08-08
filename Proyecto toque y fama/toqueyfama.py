#Benajmin Vidal (benjamin.vidal@alu.ucm.cl), Luciano Valenzuela(luciano.valenzuela.01@alu.ucm.cl)/seccion 1
from random import choice

def pos(list):  #Esta función genera la lista random impuesta por el pc
    
    lista_nul = []
    for i in range(5):
        lista_nul.append(choice(list))
    return lista_nul

  
if "__main__" == __name__:

    lista_pos = ["a","b","c","d","e","f","g","h","i","j"]   #con esta lista generamos la lista randomizada
    lista_fi = pos(lista_pos)

    print("¡Bienvenido al juego Toque y fama!")
    print("Este juego consta de adivinar una serie de 5 letras impuestas por el pc, desde la a hacia la j")
    print("Para ello debes ingresar sus propuestas de series de letras separadas por un espacio (a b c...")
    print("En este juego se le darán pistas para adivinar finalmente el codigo, a traves del sistema de FAMAS y TOQUES")
    print("En donde las FAMAS son las letras que van en el mismo lugar de la serie impuesta por el pc")
    print("y los toques son los aciertos de letras que van en la serie impuesta")

    print("Ingrese sus proposiciones")
    propsiciones = input()          

    lista_juego=propsiciones.split(" ")       #aqui pasamos la proposiciones ingresadas de un string a una lista para poder compararlo

    i=0

    while lista_juego!=lista_fi:

        famas = 0
        toques = 0

        for i in range(5):
            if lista_juego[i] == lista_fi[i]:
                famas = famas + 1                                           #con este bloque contamos cuantas famas y toques hay
            elif lista_juego[i] in lista_fi:
                toques = toques + 1
        print("Famas: ",famas,", Toques: ",toques)
        print("Ingresa otras letras")
        propsiciones = input()
        lista_juego = propsiciones.split(" ")


    print("Felicidades! hacertaste la serie de letras, has ganado!")
