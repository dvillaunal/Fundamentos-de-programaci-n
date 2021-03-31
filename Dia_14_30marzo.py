## Importar y usar librerías en Python

# Módulo en python
'''
En programación un módulo se define como la porción de un programa.

-> Según la web:
En programación, un módulo es una porción de un programa de ordenador.
De las varias tareas que debe realizar un programa para cumplir con su función u objetivos,
un módulo realizará, comúnmente, una de dichas tareas (o varias, en algún caso).
'''

# Libresía en python
'''
En programación una librería se define como un conjunto de implementaciones funcionales.

-> Según la web:
En informática, una biblioteca o, llamada por vicio del lenguaje librería (del inglés library)
es un conjunto de implementaciones funcionales, codificadas en un lenguaje de programación,
que ofrece una interfaz bien definida para la funcionalidad que se invoca.

Con esto podemos definir:
una librería como un conjunto de módulos cuya agrupación tiene una finalidad específica
y que también puede ser invocada, tal como un módulo. Pero no es un módulo,
sino un conjunto de ellos con una estructura determinada para lograr una finalidad.

teniendo esto en cuenta traemos librerias d ela siguiente manera:

Las incluimos en nuestro código con la instrucción 'import', seguida del nombre de la librería
'''

import math, random, datetime
r = int(input("Ingrese un numero entero: "))

raiz = math.sqrt(r) #Utilizamos la función sqrt del módulo math

print("La raiz cuadrada de {} es".format(r), raiz)

s = int(input("Ingrese el inicio del rango de numeros aletorios (numero entero): "))
e = int(input("Ingrese el final del rango de numeros aletorios (numero entero): "))
for i in range(20):
  print("Numeros aletorios en un rango dado")
  print(random.randint(s,e))

# From module import
'''
La orden from (module) import nos permitirá importar determinadas funciones de un módulo
y no el modulo completo. Aunque hay que tener cuidado con lo que importamos de cada módulo,
y pronto sabrás porque.
Primero veamos cómo haríamos para solo importar y utilizar esta función SQRT de Math.
Dejando todo el equipaje pesado de lado:
'''

from math import sqrt
r = int(input("Ingrese un numero entero: "))

raiz = sqrt(r) 

print("La raiz cuadrada de {} es".format(r), raiz)

'''
Nota:
Para saber todas las funciones de un módulo
podemos hacerlo mediante el siguiente código,
import (*library*)
print(dir((*library*)))
'''
print(dir(math))

print("EL directorio de funciones de random")
print(dir(random))

print("Numeros aletorios entre [0,1)")
for x in range(10):
  print(random.random())

from random import uniform, choice, sample

sf = float(s) + 0.1
ef = float(e) + 0.1
print("Numero aletorio entre {} y {}" .format(sf, ef))
uniform(sf, ef)

lista = ["Hola", True, 12, 32.45, "CLAVE MORSE"]

print("Escoge en tre los valores de la lista, un numero repetido de veces", lista)
for i in range(len(lista)):
  print(choice(lista))

print("k muestras sin recambio")
sample(lista, k = 2)

valores_sin = []
valores_cos = []

pi = math.pi

for i in [0, pi/6, pi/4, pi/3, pi/2, pi]:
  print(" ")
  print('el valor del Seno en {} es: ' .format(i))
  print(math.sin(i))
  print(" ")
  print('el valor del Coseno en {} es: ' .format(i))
  print(math.cos(i))
  valores_cos.append(math.cos(i))
  valores_sin.append(math.sin(i))

print("un valor del seno es: ", sample(valores_sin, k = 1))
print("un valor del coseno es: ", sample(valores_cos, k = 1))

