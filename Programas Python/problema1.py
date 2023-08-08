

import random

jugadores=["Vidal","Gabo","Marta","Renato","Ele","Cristobal Cordova"]
equipo1=[]
equipo2=[]

i=0
while (i<=5):

    equipo1.append(random.choice(jugadores))
    equipo2.append(random.choice(jugadores))
    print(equipo1)
    print(equipo2)
    i=i+1



#print("Ingrese el var1")
#var1=int(input())
#print("su variable ingresada es",var1)

#print("Ingrese el var2")
#var2=int(input())
#print("su variable ingresada es",var2)

#var3=var1
#var1=var2
#var2=var3
#print("Var1 vale: ",var1,", var2 vale: ",var2)
