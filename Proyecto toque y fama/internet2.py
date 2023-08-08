import random
adivinar = ""
for i in range(4):
    posible = ["a","b","c","d","e","f","g","h","i","j"]
    posible= random.choice
    while str(posible) in adivinar:
        posible= random.choice
    adivinar+=str(posible)
adivinado =input("Ingrese el número que desea encontrar: ")
intentos = 1
while adivinado != adivinar:
    intentos+=1
    fama = 0
    toque = 0
    for i in range(4):
        if adivinar[i] == adivinado[i]:
            fama+=1
        elif adivinar[i] in adivinado:
            toque+=1
    print(adivinar)
    print("tu número tiene ", fama, "fama y",toque, "toque")
    adivinado = input("Escribe otro número: ")
    
 
print ("Felicitaciones! Adivinaste el código en ",intentos, "intentos")
