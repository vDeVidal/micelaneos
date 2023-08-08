lista = ['a', 'b', '1', 'hola', 'hola mundo', 'hol4', 'HOLA', 'Luis']
for elemento in lista:
    print(
        f"¿'{elemento}' contiene únicamente letras del alfabeto? {elemento.isalpha()}")