#Intento para sacar la lista con las 10 letras aleatoria


from random import choice
from unicodedata import name




def pos(list):  #Esta función genera la lista random impuesta por el pc
    lista_nul = []
    for i in range(10):
        lista_nul.append(choice(list))
    return lista_nul
def menu(list):
    print("Reingrese las 10 proposiciones")
    list = input().split(" ")
    return list

def largo_pos(list,a): #Esta función es para revisar la lista de proposiciones y verificar que cumplen con el rango

    i=1
    while i<a:
        list=menu(list)
        #yu(list)
        if len(list)!=10:

            if i<1:
                i==0
            else:
                i=i-1
        else:
            i=i+1
        print('largo :',len(list),i)






if __name__ == "__main__":

    lista_pos = ["a","b","c","d","e","f","g","h","i","j"]
    lista_fi = pos(lista_pos)

    print("Ingrese sus proposiciones")
    propsiciones = input() #sin ser una lista con caracteres separados

    lista_juego = propsiciones.split(" ")
    i=0
    while i<len(lista_juego):

        if lista_juego[i]=='0' or lista_juego[i]=="1" or lista_juego[i]=="2"or lista_juego[i]=="3"or lista_juego[i]=="4"or lista_juego[i]=="5"or lista_juego[i]=="6"or lista_juego[i]=="7"or lista_juego[i]=="8"or lista_juego[i]=="9":
            print('es un numero:', i)
        else:
            print(lista_juego[i])
        i=i+1
    #fama=10

    lista_revisada1 = largo_pos(lista_juego)



    #print(lista_revisada1)

print(__name__)

"""Falta: - que se detecten las famas y los toques
          - que cada proposicion recorra la lista
          - Intrucciones
          - mensaje de que ganó
          - enviarlo
          - Maldecir al Hugo
          - Que nos pague la Terapia"""