from random import choice as rd

jugadores=["Vidal","Gabo","Marta","Renato","Ele","Cristobal Cordova"]
equipo1=[]
equipo2=[]

i=0
while (i<=5):

    equipo1.append(rd(jugadores))
    equipo2.append(rd(jugadores))
    print(equipo1)
    print(equipo2)
    i=i+1
