##  Funciones Built-in
'''
Python tiene varias funciones que están disponibles para su uso.
Estas funciones se denominan funciones integradas.

Además, hoy fue mucha teoria para asimilar (por eso ejemplos simples)
'''
# abs():
'El método abs () devuelve el valor absoluto del número dado.'

lista = []
lista1 = []
for i in range(-10,10,1):
  lista1.append(i)
  lista.append(abs(i))

print(lista1)
print("Vemos que los valores desde el -10 al -1, ahora son positivos")
print(lista)


# all():
'''
La función  all() devuelve True si todos los elementos de un iterable son verdaderos;
de lo contrario, devuelve False.

Si el objeto iterable está vacío, la función all() también devuelve True.
'''

tupla = tuple(lista)
dic = {}
for i,n in enumerate(lista1):
  dic[i] = n

print(tupla, dic)
print(all(lista1))
'Nota: Cuando se usa en un diccionario, la función all () verifica si todas las claves son verdaderas, no los valores .'
print(all(dic))

# any():
'Retorna True si un elemento cualquiera del iterable es verdadero. Si el iterable está vacío, retorna False. Equivalente a:'
print(any(lista))
print(any(dic))

# ascii():
'La función ascii() devuelve una versión legible de cualquier objeto (cadenas, tuplas, listas, etc.).'
'La función ascii() reemplazará cualquier carácter no ASCII con caracteres de escape'

print(ascii("Capacitación"))
print(ascii('Pingüino'))

# bin():
'el codigo binario no le entido muy bien por ende lo dejare aparte'

# bool():
'Devuelve el valor booleano del objeto especificado.'

bool(lista)

# callable():
'La función callable() devuelve True si el objeto especificado es invocable; de ​​lo contrario, devuelve False:'

def inv():
  a = 'c'

def a():
  i = input()
  print(i)

z = 4

print(callable(inv))
print(callable(a))
print(callable(z))

# chr():
'La función chr() devuelve el carácter que representa el Unicode especificado.'

x = chr(87)
print(x)

y = chr(49)
print(y)

# compile():
'La función compile() devuelve la fuente especificada como un objeto de código, listo para ser ejecutado.'

comp = compile('input("funciono, escriba \'que bueno\' ")', 'text', 'eval')
'compile con exec(): '
exec(comp)

# complex():
'La función complex() devuelve un número complejo especificando un número real y un número imaginario.'

im = complex(2,13)
print(im)

# delattr():
'La función delattr() eliminará el atributo especificado del objeto especificado.'

class datos:
  RH = 'A+'
  peso = 43.2
  h = 155.45

delattr(datos, 'RH')

# dict():
'Devuelve un diccionario (Array)'

dic = dict(n_1 = 1, n_2 = 2, n_3 = 3)

print(dic)

# dir():
'''
La función dir() devuelve todas las propiedades y métodos del objeto especificado,
sin los valores.

Esta función devolverá todas las propiedades y métodos,
incluso las propiedades integradas que son predeterminadas para todos los objetos.
'''

print(dir(datos))

# divmod():
'''
La función divmod() devuelve una tupla que contiene el cociente 
y el resto cuando argumento1 (dividendo) se divide por argumento2 (divisor).
'''

divmod(10,2)

# enumerate():
'''
Toma una colección (por ejemplo, una tupla) y la devuelve como un objeto enumerado
'''
tupla0 = ('hola', 'hi', 'wii')
te = enumerate(tupla0)
print(te)

# eval():
'La eval()función evalúa la expresión especificada, si la expresión es una declaración de Python legal, se ejecutará.'

e = 'print("Hola")'
eval(e)

# exec():
'Ejecuta el código (u objeto) especificado, visto anteriormente'
comp = compile('input("funciono, escriba \'que bueno\' ")', 'text', 'eval')
exec(comp)

# filter():
'La función filter() devuelve un iterador donde los elementos se filtran a través de una función para probar si el elemento es aceptado o no.'

def cosa(x):
  if x <= 1:
    print(x)
  else:
    pass
  
nueva = filter(cosa, lista1)

for i in nueva:
  print(i)

# float():
'Devuelve un número decimal'

x = 5 
r = float(x)
print(x,"de entero a real ->", r)

# format():
'La función format() formatea un valor especificado en un formato especificado.'

'una de tantas opciones son el %'

x = format(0.01, '%')
print(x)

# frozenset():
'La función frozenset() devuelve un objeto frozenset inmutable (que es como un set, solo que no se puede cambiar).'
x = frozenset(lista1)
print(x)

# getattr():
'''
La getattr()función devuelve el valor del atributo especificado del objeto especificado.
'''
print('el peso del dato tomado es =>',getattr(datos,'peso'))

# globals():
'''
La función globals() devuelve la tabla de símbolos global como diccionario.

Una tabla de símbolos contiene la información necesaria sobre el programa actual.
'''

g = globals()
print(g)

# help():
'Ejecuta la función integrada para pedir ayuda al sistema'

help(print)
help(list)


'''
hay otras antes vistas:

list() # Retorna una lista

input() # Ingresa un valor dado por el usuario

int() # retorna un numero entero

len() # retorna el tamaño del algo

round() # redondea numeros dados

set() # retorna un set

tuple() # retorna una tupla

print() # imprime, str, int, float, valores dados por el usuarios

str() # Retorna un string

type() # Retorna el tipo de objeto a evaluar

....entre otras....
'''

