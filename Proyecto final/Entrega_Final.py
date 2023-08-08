def limpieza(entrada):                                      # Función para limpiar(depurar) la información del archivo
    
    lista = entrada.readlines()
    for i in range (0,len(lista)):                          # Generación de listas y sublistas de todos los elementos del archivo
        lista[i] = lista[i].rstrip()
        lista[i] = lista[i].replace(' ','-')
        lista[i] = lista[i].replace(',','.')
        lista[i] = lista[i].split('-')
    return lista

def valorAños(lista):                                       # Función para separar separar todos los datos presentes en el archivo en su correspondiente año
    años2013 = []
    años2014 = []
    años2015 = []                                           # Creación de listas vacías para a posterior otorgarle contenido
    años2016 = []
    años2017 = []
    años2018 = []
    años2019 = []
    for i in range(0,len(lista)):
        if lista[i][2] == '2013':
            años2013.append(lista[i][3])
        if lista[i][2] == '2014':
            años2014.append(lista[i][3])
        if lista[i][2] == '2015':
            años2015.append(lista[i][3])                    # Con esta sucesión de 'if' dentro de un 'for' se separarán los datos para integrarlos en su respectiva lista vacía  
        if lista[i][2] == '2016':
            años2016.append(lista[i][3])
        if lista[i][2] == '2017':
            años2017.append(lista[i][3])
        if lista[i][2] == '2018':
            años2018.append(lista[i][3])
        if lista[i][2] == '2019':
            años2019.append(lista[i][3])

    promedio2013 = round(promedio(años2013),3)
    promedio2014 = round(promedio(años2014),3)
    promedio2015 = round(promedio(años2015),3)
    promedio2016 = round(promedio(años2016),3)              # Estipulamos variables correspondientes a los promedios de cada año
    promedio2017 = round(promedio(años2017),3)
    promedio2018 = round(promedio(años2018),3)
    promedio2019 = round(promedio(años2019),3)

    promedios = ['Promedio 2013: ',promedio2013],['Promedio 2014: ',promedio2014],['Promedio 2015: ',promedio2015],['Promedio 2016: ',promedio2016],['Promedio 2017: ',promedio2017],['Promedio 2018: ',promedio2018],['Promedios 2019',promedio2019]
    return promedios                                        # Con la variable "promedios", juntamos y ordenamos en una sola lista todos los promedios de todos los años
    
def promedio(totalAños):                                    # Función para calcular dichos promedios de la función anterior
    total = len(totalAños)
    suma = 0 
    for i in range(0,len(totalAños)):
        suma = suma + float(totalAños[i])
    promedio = (suma/total)

    
    return promedio


def miniyMaxi(lista):                                          # Función para buscar los valores minimos y maximos entre toda la lista de datos
    lminiyMaxi = []
    for x in range(0,len(lista)):
        lminiyMaxi.append(lista[x][3])
    mini = min(lminiyMaxi)
    maxi = max(lminiyMaxi)
    return mini, maxi

def fechaMiniyMaxi(lista):                                      # Función para determinar la fecha de dichos valores maximos y minimos de la función anterior
    for x in range(0,len(lista)):
        if lista[x][3] == miniyMaxi(lista)[0]:
            fechamini = lista[x]
    for x in range(0,len(lista)):
        if lista[x][3] == miniyMaxi(lista)[1]:
            fechamaxi = lista[x]
    return fechamini, fechamaxi

def valores(promedios2):                                        # Función para juntar los valores máximos y mínimos con sus respectivas fechas
    
    resultado1=('El mayor valor corresponde al día '+ fechaMiniyMaxi(lista)[1][0]+' del mes '+fechaMiniyMaxi(lista)[1][1]+' de '+fechaMiniyMaxi(lista)[1][2]+'\n')
    resultado2=('El menor valor corresponde al día '+ fechaMiniyMaxi(lista)[0][0]+' del mes '+fechaMiniyMaxi(lista)[0][1]+' de '+fechaMiniyMaxi(lista)[0][2])
    final.write(resultado1)
    final.write(resultado2)                                     
    final.close()
    return promedios2

if __name__ == '__main__':                                      # Con este "if __name__" hacemos que todos los valores dentro de condición se ejecuten de los primeros y asi cada variable toma su respectiva función
    entrada = open('datos.txt')
    lista = limpieza(entrada)
    promedios = valorAños(lista)
    valores = promedios
    linea = (promedios[0][0] + str(promedios[0][1]))

    promedios2 = str(valores)

    entrada.close()
    final = open('resumen.txt','w')
final.write(promedios2)                                         # Con este código generamos el archivo de salida y se escriben los datos salientes.



# El archivo de salida se generará solo al iniciar el programa