from random import choice


def pos(list):  #Esta función genera la lista random impuesta por el pc
    
    lista_nul = []
    for i in range(5):
        lista_nul.append(choice(list))
    return lista_nul

def contador(list):
    famas=0
    toques=0
    for i in range(5):
        if lista_fi[i] == list[i]:
            famas= famas + 1
        elif lista_fi[i] in list:
            toques= toques + 1
        numfam=famas
        numtoq=toques
        numfamytoq = numfam,numtoq
        
    return numfamytoq

    
if "__main__" == __name__:

    lista_pos = ["a","b","c","d","e","f","g","h","i","j"]
    lista_fi = pos(lista_pos)

    print("Ingrese sus proposiciones")
    propsiciones = input()          #sin ser una lista con caracteres separados (str)

    lista_juego=propsiciones.split(" ")

    i=0

    while lista_juego!=lista_fi:
        print(lista_fi)
        hugo=contador(lista_juego)
        #print(hugo)
        print("famas: ",hugo[0],"toques: ",hugo[1])
        if hugo[0]!=5:
            print("reingrese las proposiciones: ")
            lista_juego=input()        
        else:
            i=i+1
    
    print("ganaste")
