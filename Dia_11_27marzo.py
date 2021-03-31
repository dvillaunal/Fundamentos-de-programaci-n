# Funciones

'''
Una función es un bloque de código que solo se ejecuta cuando se llama.

Puede pasar datos, conocidos como parámetros, a una función.

Una función puede devolver datos como resultado.
'''
# Funciones "estériles"

'Las funciones "estériles" son líneas de código que ejecutan acciones pero no devuelven nada al cuerpo del programa'

# Crear una función

'''
En Python, una función se define usando la palabra clave def :
'''

def imprima():
  print("Esto es una Función")


"Llame a un función con el nombre de la misma y al final con dos parentesís:"

imprima()

# Argumentos:

"""
La información se puede pasar a funciones como argumentos.

Los argumentos se especifican después del nombre de la función, entre paréntesis.
Puede agregar tantos argumentos como desee, solo sepárelos con una coma.
"""

'Ecuación pitagoras'
print("digite el valor de dos catetos e imprimo su Hipotenusa")
def hipo(ca, co):
  h = (ca**2) + (co**2)
  print("%.2f" % h)

'''
Nota:
De forma predeterminada, se debe llamar a una función con el número correcto de argumentos.
Lo que significa que si su función espera 2 argumentos,
debe llamar a la función con 2 argumentos, ni más ni menos.
'''

# Argumentos arbitrarios, * argumentos

'''
Si no sabe cuántos argumentos se pasarán a su función, 
agregue un * antes del nombre del parámetro en la definición de la función.

De esta forma, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
'''

def nombres(*n):
  print("el nombre del invitado es " + n[3])

nombres("Roberto", "Samuel", "Jonas", "Jesús")

# Argumentos de palabras clave
"""
También puede enviar argumentos con la sintaxis clave = valor .
De esta forma no importa el orden de los argumentos.
"""

def nombre(nom1, nom2, nom0):
  print("deletra el nombre del invitado" + nom0)
  for i in nom0:
    print(i)

nombre(nom1= "Roberto", nom0= "Daniel Felipe Villa Rengifo", nom2= "Jonas")

# Argumentos de palabras clave arbitrarias, ** kwargs
'''
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos:
** antes del nombre del parámetro en la definición de la función.

De esta forma, la función recibirá un diccionario de argumentos y
podrá acceder a los elementos en consecuencia:
'''

def comida(**c):
  print("cual es tu comida favorita: " + c['ham'])

comida(ham = "Hamburgesa", dog = "Hot Dog", tacos = "Tacos", pollo = "Pollo frito")

# Valor de parámetro predeterminado:
'''
El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.

Si llamamos a la función sin argumento, usa el valor predeterminado:
'''

def musica(m = "La que tenga buena letra"):
  print("Mi genero favorito es " + m)

musica("reggaeton")
musica("Trap")
musica("Salsa")
musica()

# Clases definidas por el Usuario:
'''
-> Funciones definidas por el usuario
    -> Funciones Fertiles
    -> Funciones Inferitles
-> Funciones incorporadas (buil-in) 
'''

print("Esto es una funcíon predeterminada")

'''
abs() devuelve el valor absoluto de un numero
len() devuelve ña longitud de un objeto
help() Ejecuta el sistema de ayuda integrado.
list() Devuelve una lista
round() Redondea un número
set() Devuelve un nuevo objeto de conjunto
input() Permitir la entrada del usuario
eval() Evalúa y ejecuta una expresión.
entre otras..........
.........
........
'''

rango = []

def numbers():
    for i in range(int(input('Hasta donde quieres llegar?: '))+1):
        print(i)
        rango.append(i)

numbers()
print(rango)
a = sum(rango)
print("La suma de la lista impresa da {}" .format(a))

# Funciones "fértiles"

'Las funciones "fértiles" son líneas de código que ejecutan acciones y luego devuelven "un valor" al cuerpo del programa'

def date():
  own0 = ["Nombre", "Apellido", "Rh", "Edad"]
  own1 = []
  for i in own0:
    print("Ingrese el sigueinte dato: ", i)
    o = input()
    own1.append(o)
    if len(own1) == 4:
      break
  return print('tus datos personales son: ' ,own1)

date()

# Librerías
'''
Existen librerías que han sido creadas para Python. Contienen las definiciones
e instrucciones para funciones específicas que no son utilizadas en todos los casos.
Las incluimos en nuestro código con la instrucción import, seguida del nombre de la librería.

Algunos ejemplos comunes:

math: incluye una gran variedad de funciones matemáticas como seno, coseno, raiz cuadrada, entre muchas otras.
datetime: incluye los tipos de datos y funciones necesarias para tratar fechas dentro de Python.
random: incluye las funciones necesarias para generar números aleatorios dentro de Python.
openpyxl: incluye los tipos de datos y funciones necesarias para manipular hojas de calculo de Excel.

**Info sacada de "Taller 04", Fundamentos de Programación**
'''

# Ejercicios:

'Escriba un programa que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo'

def dibujo():
  print('digite ancho , altura y figura para imprimir cuadrado')
  ancho = int(input("Anchura del rectángulo: "))
  h = int(input("Altura del rectángulo: "))
  c = input("Caracter a utilizar: ")
  for x in range(h):
    for x in range(ancho):
      print(c, end = ' ')
    print()
  def area():
    ar  = ancho * h
    return print("el area de la figura es: ", ar)
  area()


dibujo()

