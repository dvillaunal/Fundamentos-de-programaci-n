## Bucle for:

from random import choice, randint, uniform
import random

'''
Un bucle for se utiliza para iterar sobre una secuencia
(que es una lista, una tupla, un diccionario, un conjunto o una cadena).
'''

for i in range(7):
  for x in range(i):
    print(i, end=" ")
  print(" ")


for i in range(10):
  for x in range(5,i-1,-1):
    print("*", end=" ")
  print(" ")

lista = ["fruta", 'vegetal', 'harina']

for i in lista:
  print(i)

for i in lista:
  i += " cosas"
  print(i)

name = input("Ingresa tu 1er o uníco nombre: ")

list = []

for x in name:
  list += x

print(list)

'Con la instrucción break podemos detener el ciclo antes de que haya pasado por todos los elementos'

for i in lista:
  print(i)
  if i == 'vegetal':
    break

'''
Nota: Para recorrer un conjunto de código un número específico de veces, podemos usar la función range () ,
La función range() devuelve una secuencia de números, comenzando desde 0 de forma predeterminada,
se incrementa en 1 (de forma predeterminada) y termina en un número especificado.
'''

for i in range(6):
  print(i)
else:
  print("Los numeros van del 0 al 5, sin tomar el valor introducido dentro de range()")

e0 = random.randint(1,20)
e1 = random.randint(1,20)
e2 = random.randint(1,20)

f0 = random.uniform(1,10)
f1 = random.uniform(1,10)
f2 = random.uniform(1,10)

s0 = random.choice(["HOLA", 'mundo', '100dias'])
s1 = random.choice(["Programar", 'python', 'ciencia de datos'])
s2 = random.choice(["colaboratory", 'telegram', 'github'])

lista = [e0, f0, s0, True, e1, f1, s1, False, e2, f2, s2, True]

lista_int = []
lista_float = []
lista_str = []
lista_bool = []

for i in lista:
  if type(i) == int:
    lista_int.append(i)
  
  elif type(i) == float:
    lista_float.append(i)
  
  elif type(i) == str:
    lista_str.append(i)
  
  else:
    lista_bool.append(i)
  continue

print(lista_int)
print(lista_float)
print(lista_str)
print(lista_bool)

lista_de_nombres = ['Miguel', 'Bruma', 'Jose', 'Lorena', 'Natalia', 'Paola', 'Sara', 'Liliana']
edades = {'Miguel': 22, 'Daniel': 25, 'Bruma': 9,'Jose': 23, 'Lorena': 17, 'Natalia': 18, 'Paola': 22, 'Sara': 29, 'Liliana': 56}

# Recorer un dicionario con el ciclo for.

for i in edades:
  print(i)

# Imprimimo las edades correspomdientes a cada nombre usando un ciclo for.


for i in lista_de_nombres:
  print(edades[i])
  

# usamos el ciclo for para recorrer un diccionario que tiene los datos de una persona

datos_basicos = {"apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

# keys()  nos da las llaves o claves de diccionario
clave = datos_basicos.keys()

# values() nos da los valores del diccionario
valor = datos_basicos.values()
#  me devuelve una lista de tuplas, donde cada tupla tiene su clave y su valor.
cantidad_datos = datos_basicos.items()


for clave, valor in cantidad_datos:
    print (clave + ": " + valor)

for i in range(0, 101, 1):
  if i < 30:
    print("Hello")
  elif i < 85 :
    print("*", end=" ")
  else:
    break


for n in range(3, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, "igual", x, "*", n/x)
      break
  else:
    print(n, "es un número primo")

  
#otro ejemplo con break 


for i in range(100000):
  print(i)
  if i == 3:
    break


'Con la instrucción else podemos ejecutar un bloque de código una vez cuando la condición ya no es verdadera:'

palabra = "amo python"


# Pirmer ejemplo con continue. 

palabra = "amo python"


for i in palabra:
  if i == "a":
    continue
  print("Letra actual : " + i) 


# Segundo ejemplo con continue.

for i in range(10):
  if i ==2:
    continue
  print(i)
