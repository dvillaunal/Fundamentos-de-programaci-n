# Tuplas
"""
Las tuplas se utilizan para almacenar varios elementos en una sola variable.

Tupla es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos,

Los elementos de tupla están ordenados, no se pueden cambiar
(lo que significa que no podemos cambiar, agregar o eliminar elementos después de que se haya creado la tupla) 
y permiten valores duplicados.

Los elementos de tupla están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice, [1]etc.

Las tuplas se escriben entre paréntesis.
"""

utiles = ("borrador", "cuadernos", "regla", "lapiceros", "borrador")
print(utiles)

'como hemos visto con la función len() '
print(len(utiles))

## Tuplas de un solo elmento:

'''
Para crear una tupla con un solo elemento,
debe agregar una coma después del elemento;
de lo contrario, Python no lo reconocerá como una tupla.
'''
one_element = ('elemento',)
print("Veamos la clase de one_element", type(one_element))

'Esto no es una tupla:'
no_tupla = ('elemento')
print(type(no_tupla))


## Tipo de datos:
'''
Los elementos de tupla pueden ser de cadena, numeros (int y/o float) y booleanos

Una tupla puede contener diferentes tipos de datos:
'''

variedad = ("www", 12, True, False, "Hola", 23.4)

## Crear Tuplas:
'Con el construcctor tuple() podemos generar una tupla:'

crear = tuple(("objeto1", "objeto2", 'objeto3')) # Tenga en cuenta los parentesís dobles
print(crear)

## Acceso a las tuplas:
'Puede acceder a los elementos de tupla consultando el número de índice, entre corchetes:'
print("Utilizando el ejemplo anterior accedemos al elemento 0, este es {}." .format(crear[0]))
print(crear[0][0]) # 'w'

### Rango de índices:
'''
Puede especificar un rango de índices especificando dónde comenzar y dónde terminar el rango.

Nota: La búsqueda comenzará en el índice 2 (incluido) y terminará en el índice 4 (no incluido).
'''
frutas = ('mango', 'manzana', 'pera', 'fresa', 'banano', 'kiwi', 'naranja')
print(frutas)

'Al especificar un rango, el valor de retorno será una nueva tupla con los elementos especificados:'
print(frutas[2:4])

print(frutas[2:])
print(frutas[:4])


## Actualizar Tuplas:

'''
Las tuplas no se pueden cambiar, lo que significa que no puede cambiar,
agregar ni eliminar elementos una vez que se crea la tupla.

Pero existen algunas soluciones. Puede convertir la tupla en una lista,
cambiar la lista y convertir la lista nuevamente en una tupla.
'''
frutas1 = list(frutas)
frutas1.append('melon')
frutas = tuple(frutas1)
print(frutas)

'Para eliminar un elemento:'
frutas1.remove('melon') # Una lista
frutas = tuple(frutas1)
print(frutas, "Sin 'melon'")

'Eliminar una Tupla:'
frutas_copy = frutas
del frutas_copy
# print(frutas_copy), Sale error ya que la tupla no existe

## Desembalaje de una tupla:
'''
Cuando creamos una tupla, normalmente le asignamos valores.
Esto se llama "empaquetar" una tupla:
'''
(amarillo, rojiza, verde, rojo, pecoso, peludo, naranja) = frutas
print(amarillo)
print(pecoso)

'''
Nota: La cantidad de variables debe coincidir con la cantidad de valores en la tupla;
de lo contrario, debe usar un asterisco para recopilar los valores restantes como una lista.
'''
(amarillo, rojiza, *fruit) = frutas
print(fruit)

'''
Si el asterisco se agrega a otro nombre de variable que no sea el anterior,
Python asignará valores a la variable hasta que el número de valores restantes
coincida con el número de variables restantes.
'''
(amarillo, *others, citrico) = frutas
print(others)
print(citrico)

## Unir Tuplas:
'Para unir dos o más tuplas, puede utilizar el + operador:'
tupla_nueva = variedad + crear # de ejemplos anteriores
print(tupla_nueva)

'''
Si desea multiplicar el contenido de una tupla un número determinado de veces,
puede utilizar el * operador:
'''
tupla_mul = variedad * 3
print(tupla_mul)

## Metodos:

### .count():

'.count(n) Devuelve el número de veces que aparece el valor n en la tupla:'
c0 = tupla_mul.count(12) 
c1 = tupla_mul.count('www')
print(c0)
print(c1)

### .index():

'.index(n) Busque la primera aparición del valor n y devuelva su posición:'
b = tupla_mul.index(True)
print(b)

'Nota: genera una excepción si no se encuentra el valor:'

"""
e = tupla_mul.index('Felipe') #print(e), si se ejecuta => 'tuple.index(x): x not in tuple'
"""

'''
Ventajas de las tuplas sobre las listas
Dado que las tuplas son bastante similares a las listas, ambas se utilizan en situaciones similares.
Sin embargo, hay ciertas ventajas de implementar una tupla sobre una lista.
A continuación se enumeran algunas de las principales ventajas:

-> Generalmente utilizamos tuplas para tipos de datos heterogéneos (diferentes)
y listas para tipos de datos homogéneos (similares).

-> Dado que las tuplas son inmutables, iterar a través de una tupla es más rápido que con una lista.
Por lo tanto, hay un ligero aumento de rendimiento.

-> Las tuplas que contienen elementos inmutables pueden utilizarse como clave de un diccionario.
Con las listas, esto no es posible.

-> Si tienes datos que no cambian,
implementarlos como tupla garantizará que permanezcan protegidos contra escritura.

Texto sacado de [https://www.programiz.com/python-programming/tuple]
'''

