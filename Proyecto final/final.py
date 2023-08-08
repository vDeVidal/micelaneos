def depuracion(entrada):
    #creamos listas y sublistas de los elementos del archivo
    lista = entrada.readlines()
    for i in range (0,len(lista)):
        lista[i] = lista[i].rstrip()
        lista[i] = lista[i].replace(' ','-')
        lista[i] = lista[i].replace(',','.')
        lista[i] = lista[i].split('-')
    return lista

def años(lista):
    #creamos listas vacias para cada año
    años2013 = []
    años2014 = []
    años2015 = []
    años2016 = []
    años2017 = []
    años2018 = []
    años2019 = []
    for i in range(0,len(lista)):
        #tomamos solo los valores del dolar en cada fecha
        if lista[i][2] == '2013':
            años2013.append(lista[i][3])
        if lista[i][2] == '2014':
            años2014.append(lista[i][3])
        if lista[i][2] == '2015':
            años2015.append(lista[i][3])
        if lista[i][2] == '2016':
            años2016.append(lista[i][3])
        if lista[i][2] == '2017':
            años2017.append(lista[i][3])
        if lista[i][2] == '2018':
            años2018.append(lista[i][3])
        if lista[i][2] == '2019':
            años2019.append(lista[i][3])
    #Creamos una variable del promedio de cada año

    promedio2013 = round(promedio(años2013),3)
    promedio2014 = round(promedio(años2014),3)
    promedio2015 = round(promedio(años2015),3)
    promedio2016 = round(promedio(años2016),3)
    promedio2017 = round(promedio(años2017),3)
    promedio2018 = round(promedio(años2018),3)
    promedio2019 = round(promedio(años2019),3)

    promedios = ['Promedio 2013: ',promedio2013],['Promedio 2014: ',promedio2014],['Promedio 2015: ',promedio2015],['Promedio 2016: ',promedio2016],['Promedio 2017: ',promedio2017],['Promedio 2018: ',promedio2018],['Promedios 2019',promedio2019]
    return promedios
    #Creamos una variable "promedios", para asignarle la lista de todos los promedios calculados
def promedio(totalAños):
    #Función para calcular el promedio de los valores
    total = len(totalAños)
    suma = 0 
    for i in range(0,len(totalAños)):
        suma = suma + float(totalAños[i])
    promedio = (suma/total)

    
    return promedio

#Función para calcular máximo y minimo
def minymax(lista):
    lminymax = []
    for x in range(0,len(lista)):
        lminymax.append(lista[x][3])
    lmin = min(lminymax)
    lmax = max(lminymax)
    return lmin, lmax

#Función para definir la fecha de el valor máximo y minimo
def fminmax(lista):
    for x in range(0,len(lista)):
        if lista[x][3] == minymax(lista)[0]:
            fechamin = lista[x]
    for x in range(0,len(lista)):
        if lista[x][3] == minymax(lista)[1]:
            fechamax = lista[x]
    return fechamin, fechamax

def valores(promedios2):
    
    resultado1=('El mayor valor corresponde al día '+ fminmax(lista)[1][0]+' del mes '+fminmax(lista)[1][1]+' de '+fminmax(lista)[1][2]+'\n')
    resultado2=('El menor valor corresponde al día '+ fminmax(lista)[0][0]+' del mes '+fminmax(lista)[0][1]+' de '+fminmax(lista)[0][2])
    final.write(resultado1)
    final.write(resultado2)
    final.close()
    return promedios2

if __name__ == '__main__':
    entrada = open('datos.txt')
    lista = depuracion(entrada)
    promedios = años(lista)
    valores = promedios
    linea = (promedios[0][0] + str(promedios[0][1]))
    
    promedios2 = str(valores)

    entrada.close()
    final = open('resumen.txt','w')
final.write(promedios2)




''''final.write(promedios[0][0]+str(promedios[0][1]+'\n'))
    final.write(promedios[1][0]+str(promedios[1][1]+'\n'))
    final.write(promedios[2][0]+str(promedios[2][1]+'\n'))
    final.write(promedios[3][0]+str(promedios[3][1]+'\n'))
    final.write(promedios[4][0]+str(promedios[4][1]+'\n'))
    final.write(promedios[5][0]+str(promedios[5][1]+'\n'))
    final.write(promedios[6][0]+str(promedios[6][1]+'\n'))
    '''