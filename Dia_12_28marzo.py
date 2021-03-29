"No encuentro en el código cómo se documenta una función ni cómo se accede a la documentación de la función."

# Documentación de funciones:
'''
Cada función escrita por un programador realiza una tarea específica.
Cuando la cantidad de funciones disponibles para ser utilizadas es grande,
puede ser difícil saber exactamente qué hace una función.
Es por eso que es extremadamente importante documentar en cada función cuál es la tarea que realiza,
cuáles son los parámetros que recibe y qué es lo que devuelve, para que a la hora de utilizarla sea lo pueda hacer correctamente.

La documentación de una función se coloca luego del encabezado de la función,
en un párrafo encerrado entre tres comillas dobles """.
Así, para la función vista en el ejemplo anterior:
'''

def area(r):
  """Calcula el Área de un circulo, ingresando un radio r"""
  pi = 3.14
  A = pi*(r**2)
  return print("Si el radio es {}, el área del circulo es {}" .format(r,A))

area(22)

# Acceso a la documentación de una función:

'''
Cuando una función definida está correctamente documentada,
es posible acceder a su documentación mediante la función help (Built-it):
'''

help(area)

'''
De esta forma no es necesario mirar el código de una función para saber lo que hace,
simplemente llamando a help es posible obtener esta información.
'''

# Funciones: pasar argumentos por valor y pasar argumentos por referencia:

'''
Dependiendo del tipo de dato que enviemos a la función, podemos diferenciar dos comportamientos:

-> Paso por valor:
  Se crea una copia local de la variable dentro de la función.

-> Paso por referencia:
  Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.

# Tradicionalmente:

-> Los tipos simples se pasan por valor:
  Enteros, flotantes, cadenas, lógicos...
-> Los tipos compuestos se pasan por referencia:
  Listas, diccionarios, conjuntos...
'''

# Paso por valor:

def meses_de_vida(age):
  """Calcula a groso modo los meses de vida, respecto a tu edad"""
  m = age*12

edad = 19
meses_de_vida(19)
print(edad)

# Paso por referencia:

lista_descuentos = [1000,30000,12000]

def des(c):
  for i in range(len(c)):
    i += 0.1
    lista_descuentos.append(i)

des(lista_descuentos)
print(lista_descuentos)


def meses_de_vida(age):
  """Calcula a groso modo los meses de vida, respecto a tu edad"""
  m = age*12
  return m
edad = 19
edad = meses_de_vida(19)
print(edad)

'Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:'

def sumar(num):
    for i,n in enumerate(num):
        num[i] += 13
    
    print(num)

n = []

for i in range(10):
  n.append(i)

sumar(n[:])  # Una copia de la lista usando [:]
print(n)
