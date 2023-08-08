ent = open('datos.txt')
sal = open('final_datos.txt', 'w')
i = 0
lista1 = ent.readlines() #Lista completa, desordenada

def cad(lista1):
    for i in range(len(lista1)):
    
        cadena  = " ".join(lista1)
        cadena2 = cadena.replace(' ','-')
        return(cadena2)


def años(cadena2):
    año2013 = [] #Creamos listas vacías para cada año
    año2014 = []
    año2015 = []
    año2016 = []
    año2017 = []
    año2018 = []
    año2019 = []
    for i in range(0,len(cadena2)): #Recorremos la lista
        if cadena2 == '2013':
            año2013.append(cadena2)
        if cadena2 == '2014':
            año2014.append(cadena2)
        if cadena2 == '2015':
            año2015.append(cadena2)
        if cadena2 == '2016':
            año2016.append(cadena2)
        if cadena2 == '2017':
            año2017.append(cadena2)
        if cadena2 == '2018':
            año2018.append(cadena2)
        if cadena2 == '2019':
            año2019.append(cadena2)
        #Lo que hicimos, fue recorrer la lista en el subíndice 2 (año), para ver si era igual a un año en
        #concreto, si era así, a la lista vacía de ese año en concreto le asignamos los valores de los dolares
        #de ese año

        print(año2013)






    
ent.close()
sal.close()
    
    

    
        
    