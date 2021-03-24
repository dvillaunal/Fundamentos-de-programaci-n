# Expresiones Lógicas
'''
Los operadores se utilizan para realizar operaciones sobre variables y valores.

Los operadores son símbolos especiales en Python que realizan cálculos aritméticos o lógicos.
El valor sobre el que opera el operador se llama operando.

Python divide los operadores en los siguientes grupos:

-> Operadores aritméticos
-> Operadores de Asignación
-> Operadores de comparación
-> Operadores logicos
-> Operadores de identidad
-> Operadores de membresía
-> Operadores bit a bit
'''
## Operadores Aritméticos:
'''
Los operadores aritméticos se utilizan con valores numéricos
para realizar operaciones matemáticas comunes:
'''
x1 = float(input("Ingresa un numero decimal entre 1 y 10: "))
x2 = int(input("Ingresa un numero entero entre 1 y 10: "))

y1 = x1 + x2 #Suma
y2 = x1 - x2 #Resta
y3 = x1 * x2 #Multiplicación
y4 = x1 / x2 #División
y5 = x1 % x2 #Modulo
y6 = x1 ** x2 #Potencias
y7 = x1 // x2 #la división piso // redondea el resultado al número entero más cercano

print(y1)
print(y2)
print(y3)
print(y4)
print(y5)
print(y6)
print(y7)

## Operadores de Asignación:
'Los operadores de asignación se utilizan para asignar valores a las variables:'

print("x1 es un ejemplo de asignar valores a una variable, es decir, x1 es {}" .format(x1))

x1 += 2 # x1 = x1 + 2
x2 -= x1 # x2 = x2 = x2 - x1
y5 *= 12 # x2 = x2 * 12
y1 /= x1 # y1 = y1 / x1
y7 %= y2 # y7 = y7 % y2
y4 //= y3 # y4 = y4 // y3
y6 **= 2 # y6 = y6 ** 23

print(x1)
print(x2)
print(y5)
print(y1)
print(y7)
print(y4)
print(y6)

## Opereaciones de Comparación:
'Esto nos devolvera un valor True si cumple la condición y False para lo contrario'
print(x1 == y2) # Igual
print(y5 != 23.32) # No es igual
print(y7 > y3) # Mayor que
print(y1 < y6) # Menor que
print(x1 >= x2) # Mayor o igual que
print(y4 <= (y5 + y4)) # Menor o igual que

## Operadores Logicos:
'Los operadores lógicos se utilizan para combinar declaraciones condicionales:'

print(x1 == y5 and y3 > y4) # Retorna True si cumple con las condiciones
print(x2 >= x1 or y7 < 12) # Retorna True si cumple con al menos una de las condicones
print(not(y4 > 23 and 34 >= y4)) # Invierte el resultado, devuelve False si el resultado es verdadero

## Operadores de Identidad:
'''
Los operadores de identidad se utilizan para comparar los objetos, no si son iguales,
sino si en realidad son el mismo objeto, con la misma ubicación de memoria:
'''
txt1 = input("Ingrese una palabra: ")
txt2 = input("Ingrese una palabra diferente a {} : " . format(txt1))
txt1_1 = txt1

print(txt1 is txt1_1) #Devuelve True si ambas variables son el mismo objeto
print(txt1 is txt2)
print(txt1 is not txt1_1) #Devuelve True si ambas variables no son el mismo objeto
print(txt1_1 is not txt2)

## Operadores de membresia:
'Los operadores de pertenencia se utilizan para probar si se presenta una secuencia en un objeto:'

im = input("Ingrese la frase 'Hola mundo': ")
h = 'Hola'

print('ya que h es Hola, entonces im contienea h', h in im) # Devuelve True si una secuencia con el valor especificado está presente en el objeto
print(im not in txt1) # Devuelve True si una secuencia con el valor especificado no está presente en el objeto

'-------------------------------------------------------------------------------------------------------------------------------------------'
# Condicionales:
'''
Los operadores condicionales consisten en un operador externo que evalúa una expresión lógica y,
según el valor de ésta, ejecuta un bloque específico de instrucciones mientras que ignora otro(s).

-> if, elif, else
-> bucle for
-> Bucle While
-> break, continue, pass
'''
## if, elif, else:
'La declaración if… elif… else se usa en Python para la toma de decisiones'

x = 'Hola'
if x == h:
  print("x es igual a h")

'podemos decirle que si no cumple la condición...'

if x2 == y3:
  print("Que raro no son iguales")

else: print("No son iguales x2 = {} y  y3 = {} ".format(x2,y3))

'''
Nota: La palabra clave elif es la forma que tiene Python de decir
"si las condiciones anteriores no eran verdaderas, pruebe esta condición".
'''

p = int(input("Ingrese un numero entre el 10 y el 30: "))

if p >= 10 and p <= 30:
  print("Bien hecho, estas dentro del rango")

elif p <= 10:
  print('ingresaste un numero menor a 10')

else:
  print('Practica más tu obediencia')

'Podemos anidarlos...'
a = int(input("Ingresa numero entero entre 0 y 10: "))
b = int(input("Ingresa numero entero entre 0 y 10: "))
c = int(input("Ingresa numero entero entre 0 y 10: "))

if p >= 10 and p <= 30:
  print(a) if b > c else print("b es mayor que c") # Expresiones condicionales

if a > b or a > c:
  if b < 10:
    print("b es menor que 10")
  else: 
    print("b es 10")


'''
Nota: Las declaraciones if no pueden estar vacías, 
pero si por alguna razón tiene una declaración sin contenido,
introduce pass para evitar errores.
'''

if a < 9:
  pass

else:
  print("a puede ser 9 o 10")

lista = ["fruta", 'vegetal', 'harina']

if 'vegetal' in lista:
  print("lista esta completa")

'-------------------------------------------------------------------------------------------------------------------------------------------' 
## Bucle for:
'''
Un bucle for se utiliza para iterar sobre una secuencia
(que es una lista, una tupla, un diccionario, un conjunto o una cadena).
'''

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

## Bucle while:
'Con el tiempo bucle podemos ejecutar un conjunto de instrucciones, siempre y cuando se cumpla una condición.'

while a <= 6:
  print("a es {}" .format(a))
  a += 1

'Con la sentencia break podemos detener el ciclo incluso si la condición while es verdadera:'

w = 12

while w < 24:
  print(w)
  if w == 23:
    break
  w += 1

'Con la declaración continue podemos detener la iteración actual y continuar con la siguiente:'

x = 0
while x < 2:
  x += 1
  if x == 4:
    continue
  print(x)

'Con la instrucción else podemos ejecutar un bloque de código una vez cuando la condición ya no es verdadera:'

t = 10

while t <= 31:
  print(t)
  t += 3
else:
  print("t es menor a 31")

num = []

for i in range(50):
  num.append(i)

for i in num:
  if i < 40:
    while i < 20:
      print("sigue intentando,  i debe ser menor a 20",'i =', i)
      i += 1
  elif i > 40 and i < 45:
    for i in range(40, 46):
      print(i)
  else:
    break
