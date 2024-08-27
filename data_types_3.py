# Tupla
# Es una colección de elementos distintos ordenados entre ( ) y separados por comas.

tupla = (3, 2, 'ocho')
print('la tupla:', tupla, 'es de tipo:', type(tupla))

# como característica principal de las tuplas, cuando tenemos una tupla con 1 elemento
tupla = (5) # Forma incorrecta de expresarlo
print('la tupla de 1 elemento es:', tupla, 'es de tipo:', type(tupla))

tupla = ('5',) # Forma correcta
print('la tupla de 1 elemento es:', tupla, 'es de tipo:', type(tupla))
print('Su cantidad de elementos es:', len(tupla))

tupla = (3, 6, 'ocho', 'lobo', 'chocolate', 'tierra', [9.2], 'cosa')
print('tupla:', tupla)
print('aplicando slicing:', tupla[4]) # slicing de un elemento
print('aplicando slicing con números negativos:', tupla[-4:-1]) # slicing de más elementos

# Mutabilidad
# tupla[3] = 'cachorro'
# print('Tupla mutable', tupla) # No se puede, porque no tienen la capacidad de reemplazar sus valores ya predeterminados como si fueran listas
    # Las tuplas son no mutables -> TypeError: 'tuple' object does not support item assignment

# Suma de tuplas
tupla1, tupla2 = (1, 2, 3), ('cosa', 'casa', 'ronquido')
print('suma de tuplas:', tupla1 + tupla2)
print('aplicando la función len:', len(tupla1+tupla2))
print('multiplicando tuplas por un entero:', tupla1*4)

# convertir tuplas a listas
print('convirtiendo tupla a lista:', list(tupla1), 'tiene tipo:', type(list(tupla1)))

# Convertir listas a tuplas
print('convirtiendo lista a tupla:', tuple(['azul', 'oso']), 'tiene tipo:', type(tuple(['azul', 'oso'])))

# A manera de resumen: mutabilidad, operaciones con tuplas: suma, producto por un entero, slicing, conversión de tuplas a listas y viceversa.

# RANGOS
# Sucesión de números enteros
# La función range() retorna una sucesión de números en un rango, range(start, stop, step)

rango1 = range(5) # Definición por default para un rango sin necesidad de elementos
print('ejemplo de rango 1:', rango1, 'rango1 es de tipo:', type(rango1))

# Conversión de range a lista
print('convirtiendo el rango a la lista:', list(rango1))

rango2 = range(3, 104, 3) # (inicio,  final, saltos)
print('convirtiendo el rango a lista:', list(rango2)) # Los pasamos a listas para verlos como queremos

print('aplicando slicing al rango con 1 elemento:', rango2[0], 'con múltiples elementos:', rango2[2:5])

# TAREA 2
# Crear un archivo .py para determinar si cumplen con mutabilidad, suma y producto por un entero

# DICCIONARIO
# Tipos de datos boleanos representan uno de dos posibles valores: True o False

valor1 = True # TRUE
valor2 = False
print('tipos de valores boleanos:', valor1, valor2)
print('usando type:', type(valor1), type(valor2))

print('usando and:', valor1 and valor2)
print('usando or:', valor1 or valor2)

# Conversión a valores boleanos
print('entero 0 a boleano', bool(0))
print('entero 1 a boleano', bool(1))
print('entero 5 a boleano', bool(5))
print('entero -7.5 a boleano', bool(-7.5)) # Número flotante
# Todos los números que no sean 0 serán verdaderos incluso los flotantes
# Es una sobresimplificación de las cosas

if (5+3-8):
    print('otra vez print') # No lo va a imprimir porque el valor de la suma es 0 y cero equivale a falso

else:
    print('ya ven')

if (5+3-8*6):
    print('otra vez print')

else:
    print('ya ven')

# Conversiones a boleano de strings
print("str '' a boleano", bool('')) # Cadena nula: no hay ningun caracter
print("str ' ' a boleano", bool(' ')) # Tiene un espacio
print("str 'a' boleano", bool('a'))
# Las cadenas nulas serán consideradas como falsas, todo lo demás (incluso los espacios) son considerados como verdaderos

print('lista vacía [] a boleano', bool([]))
print('tupla vacía () a boleano', bool(()))
print('diccionario vacío {} a boleano', bool({}))

# DICCIONARIO {}
# fORMATO COMPLEJO para almacenar información y su estructura es en pares; su símbolo son las llaves {}; key: value
diccionario1 = dict()
print('ej de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))

diccionario1 = {'llave1': 'lobo', 'llave2': -82.654, 34: 'cosa', 'llave4': [2, 3, 4]}
print('diccionario1', diccionario1)

# slicing a diccionario
print('para el slicing uso la llave')
print(diccionario1['llave2'])
print(diccionario1['llave4'])
print(diccionario1[34])

print('usando Len, el diccionario tiene:', len(diccionario1), 'elementos')

# Sets
# Colección de valores no ordenados ue no admiten duplicados entre {} y separados por comas
set1 = {3, 6, 'azul'}
print('ej de conjunto:', set1, 'de tipo:', type(set1))
# Se imprime con un orden aleatorio pero respetando los elementos que haya

set1 = {3, 'jaja', 8, 12, 8, 'jaja', 'jeje', 3, 12}
print('ej de conjunto:', set1)
# Solo pone los elementos diferentes SIN sus repeticiones

# Los sets no se pueden indexar, ni sumar

