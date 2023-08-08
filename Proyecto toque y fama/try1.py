#Intento para sacar la lista con las 10 letras aleatoria


import random




def pos(list):  #Esta función genera la lista random impuesta por el pc
    
    lista_nul = []
    for i in range(10):
        lista_nul.append(random.shuffle(list))
    return lista_nul

def largo_pos(list): #Esta función es para revisar la lista de proposiciones y verificar que cumplen con el rango

    i = 0  
    while i == 0:
        if (len(list)) != 10:
            
            print("Reingrese las 10 proposiciones")
            list = input()
        else:
            (len(list)) == 10
            
            return True
        i = i + 1
        
        

        
if __name__ == "__main__":
    
    lista_pos = ["a","b","c","d","e","f","g","h","i","j"]
    lista_fi = pos(lista_pos)

    print("Ingrese sus proposiciones")
    propsiciones = input() #sin ser una lista con caracteres separados

    lista_juego = propsiciones.split(" ")
    
    lista_revisada1 = largo_pos(lista_juego)
print(lista_fi)
    