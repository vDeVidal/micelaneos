from random import choice

def pos(list):  #Esta función genera la lista random impuesta por el pc
    
    lista_nul = []
    for i in range(5):
        lista_nul.append(choice(list))
    return lista_nul

if "__main__" == __name__:

    lista_pos = ["a","b","c","d","e","f","g","h","i","j"]
    lista_fi = str(pos(lista_pos))

    print("ingrese sus proposiciones: ")
    proposiciones=str(input())
    
    while proposiciones != lista_fi:
        famas = 0
        toques = 0
        for i in range(5):
            if lista_fi[i] == proposiciones[i]:
                famas+=1
            elif lista_fi[i] in proposiciones:
                toques+=1
    
    print(lista_fi)
    print(f"tu número tiene {famas} fama y {toques} toque")
    adivinado = input("Escribe otro número: ")
    
 
    print ("Felicitaciones! Adivinaste el código")