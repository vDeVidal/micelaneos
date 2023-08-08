
ent = open('datos.txt')
lista = ent.readlines()
i = len(lista)
for i in range (0,len(lista)):
    cadena = ''.join(lista[i])
    cadena2 = cadena.split('-')
    cadena3 = ''.join(cadena2)
    cadena4 = cadena3.rstrip('\n')
    cadena5 = cadena4.split(' ')

    cadena6 = cadena5[0]
    cadena7 = cadena6[5::1] #para dejar el año por separado
    cadena8 = cadena6[2:5:1] #para dejar el mes por separado
    cadena9 = cadena6[0:2:1] #para dejar el día por separado
    cadena10 = cadena5[1]#para dejar el valor del dolar por separado

    cadenaF = cadena9+'-'+cadena8+'-'+cadena7+'-'+cadena10
    
    for i in len(cadenaF):
        años2013 = []
        años2014 = []
        años2015 = []
        años2016 = []
        años2017 = []
        años2018 = []
        años2019 = []
        if cadenaF[12:17] == '2013':
            años2013 = años2013.append(cadenaF[12:17])
            print(años2013)