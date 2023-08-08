def depuracion(ent):
    lista = ent.readlines() #Generamos las lineas del documento a una lista
    for i in range(0,len(lista)): #Recorremos la lista que generamos con la variable "lista"
        lista[i] = lista[i].rstrip() #Quitamos saltos de lineas
        lista[i] = lista[i].replace(' ','-') #Reemplazamos los espacios por guiones
        lista[i] = lista[i].replace(',','.') #Reemplazamos las comas por puntos, para que no de problemas con el float
        lista[i] = lista[i].split('-') #Hacemos sublistas
    return lista

def años(lista):
    año2013 = [] #Creamos listas vacías para cada año
    año2014 = []
    año2015 = []
    año2016 = []
    año2017 = []
    año2018 = []
    año2019 = []
    for i in range(0,len(lista)): #Recorremos la lista
        if lista[i][2] == '2013':
            año2013.append(lista[i][3])
        if lista[i][2] == '2014':
            año2014.append(lista[i][3])
        if lista[i][2] == '2015':
            año2015.append(lista[i][3])
        if lista[i][2] == '2016':
            año2016.append(lista[i][3])
        if lista[i][2] == '2017':
            año2017.append(lista[i][3])
        if lista[i][2] == '2018':
            año2018.append(lista[i][3])
        if lista[i][2] == '2019':
            año2019.append(lista[i][3])
        #Lo que hicimos, fue recorrer la lista en el subíndice 2 (año), para ver si era igual a un año en
        #concreto, si era así, a la lista vacía de ese año en concreto le asignamos los valores de los dolares
        #de ese año
        

    promedio2013 = promedio(año2013) #Creamos una variable del promedio de cada año
    promedio2014 = promedio(año2014)
    promedio2015 = promedio(año2015)
    promedio2016 = promedio(año2016)
    promedio2017 = promedio(año2017)
    promedio2018 = promedio(año2018)
    promedio2019 = promedio(año2019)
    promedios = [['Promedio 2013: ',promedio2013],['Promedio 2014: ',promedio2014],['Promedio 2015: ',promedio2015],['Promedio 2016: ',promedio2016],['Promedio 2017: ',promedio2017],['Promedio 2018: ',promedio2018],['Promedio 2019: ',promedio2019]]
    #Creamos una variable "promedios", para asignarle la lista, de listas de todos los promedios calculados
    return promedios

def promedio(TotalAños):
    total = len(TotalAños) #Creamos la variable "total", para asignarle el largo del total del año a trabajar
    suma = 0 #Creamos una variable "suma" y le asignamos el valor 0
    for i in range(0,len(TotalAños)): #Recorremos la lista 
        suma = suma + float(TotalAños[i]) #Cambiamos la variable, para sumarle el total del año
    promedio = (suma/total) #Creamos la variable promedio para dividir la suma, por el total
    return promedio

def valor(lista):
    ent=open('datos.txt')
    sal=[]
    mayor=0
    for linea in ent:
        linea=linea.rstrip('\n')
        lista=linea.split('-')

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
            cadena10 = cadena5[1] #para dejar el valor del dolar por separado
            cadenaF = cadena9+'-'+cadena8+'-'+cadena7+'-'+cadena10

        if mayor < float(cadena10):
            mayor = float(cadena10)
            mayor1 = ''.join(mayor)
            mayor3 = float(mayor1)
            
            
    sal.append(mayor3)
    ent.close
    return sal






if __name__ == '__main__':
    ent = open('datos.txt') #Abrimos el archivo .txt
    lista = depuracion(ent) #Asignamos la depuracion a la variable "lista"
    promedios = años(lista) #Asignamos la función "años" a la variable promedios
    mayor3=valor(lista)
    print(promedios)
    print(mayor3)
    ent.close #Cerramos "datos.txt"

    
    