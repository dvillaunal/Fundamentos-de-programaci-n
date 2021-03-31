# Sets
'''
Set es uno de los 4 tipos de datos integrados en Python que se utilizan
para almacenar colecciones de datos, los otros 3 son List, Tuple y Dictionary,
todos con diferentes calidades y usos.

se utilizan para almacenar varios elementos en una sola variable.

Un conjunto es una colección desordenada y no indexada.

Nota: Los sets permiten verificar y eliminar elementos duplicados.

Los conjuntos se escriben con llaves.
'''

compras = {"Arroz", "Pasta", "Carne"}

print(compras)

'podemos crear sets con la función set()'
lista_a_conjunto = ["objeto1", "objeto2", "objeto3"]

print(type(lista_a_conjunto))

conjunto_de_lista = set(lista_a_conjunto)
print(type(conjunto_de_lista))

'Tamaño de los sets:'
print(len(conjunto_de_lista))

## Elementos para acceder a un Set
"""
No puede acceder a los elementos de un conjunto consultando un índice o una clave.

Pero puede recorrer los elementos del conjunto usando un for bucle,
o preguntar si un valor específico está presente en un conjunto, usando la inpalabra clave.
"""
### recorrer los elemntos dde un set
for i in compras:
    print(i)

### Averiguar si un elemento esta en un Set:
if "Arroz" in compras:
    print('el elemnto Arroz esta en el conjunto \"compras\"')

## Cambiar o Agregar elementos de un Set:

'''
Nota:
Una vez que se crea un conjunto,
no puede cambiar sus elementos,
pero puede agregar elementos nuevos.
'''
ar = input("Ingresa un articulo de aseo de tu canasta familiar: ")
compras.add(ar)
print(compras)


'Con el metodo update() podemos agregar elementos de otro conjunto al conjunto actual:'
compras.update(conjunto_de_lista)
print(compras)

"""
Pero este metodo no exige que necesariamente sea un conjunto,
puede ser cualquier objeto iterable (tuplas, listas, diccionares, etc.).
"""
opciones_almuerzo = ['sopa', 'seco', 'comida rapida']
compras.update(opciones_almuerzo)
print(compras)

## Eliminar elementos del conjunto:
'''
podemos utilzar por el momento dos metodos remove() y discard()
para eliminar elementos de los sets
'''

'Nota: si un elemento a eliminar no existe, remove() reporta un error'

compras.remove("objeto1")
print(compras)

'En cambio con discard() es completamente distinto ya que NO genera un error'
compras.discard("objeto2")
compras.discard("Banana")
print(compras, "Vemos que aunque \"Banana\" no esta en set -> \"compras\" no genera error")

"""
Tambien podremos utlizar pop() pero esta definido pra quitar el ultimo elemento.
Como los sets estan desorganizados, por lo que no sabra que elemento se quita

Nota: el valor de retorno del metodo pop() es el elemento eliminado
además el orden en el que vemos los objetos cambia
"""

elemento_eliminado = compras.pop()

print(elemento_eliminado)
print(compras)

'con elemento clear() vacia por completo el set'

conjunto_de_lista.clear()
print(conjunto_de_lista)


'con el comando del eliminara el conjunto por completo:'

del conjunto_de_lista
print("<print(conjunto_de_lista)> si ejecutan este codigo dara error, ya que 'conjunto_de_lista' no esta definido")

### Unir dos Conjuntos:

'''
El metodo union() devuelve un nuevo conjunto que contiene
a todos los elementos de ambos conjuntos.
'''


# Otros Metodos

### Metodo copy()
'el metodo copy() devuelve una copia del set seleccionado'
x = compras.copy()
print(x)

### Metodo difference():
'''
Devuelve un conjunto que contiene los elementos que solo
existen en el conjunto1 y no en el conjunto2:
'''
conjunto1 = {"mazda", "toyota", "BMW"}
conjunto2 = {"Ferrari", "toyota", "Renault"}

diferencia = conjunto1.difference(conjunto2)
print(diferencia)

'''
en cambio con el metedo difference_update() elimina todos los elementos que existen en ambos conjuntos
'''

conjunto1.difference_update(conjunto2)
print(conjunto1)

"""
Nota:
El método difference_update() es diferente del método difference(), porque el método difference()
devuelve un nuevo conjunto, sin los elementos no deseados, y el método difference_update()
elimina los elementos no deseados del conjunto original.
"""


"Intersection() -> Devuelve un conjunto que contiene los elementos que existen en ambos conjuntos => intersection(set1, set2,...,setn)"

interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

"Isdisjoint() -> Devuelve True si no hay elementos en el conjunto1 presentes en el conjunto2"

z = conjunto1.isdisjoint(conjunto2)
print(z)

"issubset() -> Devuelve True si todos los elementos establecidos conjunto1 están presentes en el conjunto2"

x = conjunto2.issubset(conjunto1)
print(x)

"issuperset() -> Devuelve True si todos los elementos establecidos en el conjunto1 están presentes en el conjunto2"

conjunto11 = conjunto1.copy()
y = conjunto1.issuperset(conjunto11)
print(y)

"Intersection_Update() -> Elimine los elementos que no están presentes en ambos conjuntos"

conjunto1.intersection_update(conjunto2)
print(conjunto1)

