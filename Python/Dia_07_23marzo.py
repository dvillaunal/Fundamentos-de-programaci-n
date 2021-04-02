# Condicionales:
'''
Python admite las condiciones lógicas habituales de las matemáticas:

Es igual a: a == b
No es igual a: a! = B
Menor que: a <b
Menor o igual a: a <= b
Mayor que: a> b
Mayor o igual a: a> = b
Estas condiciones se pueden utilizar de varias formas, más comúnmente en "sentencias if" y bucles.

Una "instrucción if" se escribe utilizando la palabra clave if .
'''
## if, elif, else:
'La declaración if… elif… else se usa en Python para la toma de decisiones'

x = 'Hola'
h = input("Ingrese la palabra Hola: ")

if x == h:
  print("x es igual a h")

'podemos decirle que si no cumple la condición...'

x2 = 5
y3 = 3.4

if x2 == y3:
  print("Que raro no son iguales")

else:
  print("No son iguales x2 = {} y  y3 = {} ".format(x2,y3))

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


# Condicionales con iterables(diccionarios, listas, sets, tuplas, strings)

## Datos personales:
nombre = input("Ingresa tu nombre (sin apellido): ")
apellido = input("ingresa uno de tus dos (o 1) apellidos: ")
RH = input("Ingresa tu RH (tipo de sangre), las letras en mayusculas: ")
edad = int(input("Ingresa tu edad (Numero entero): "))
h = float(input("Ingresa tu altura en cm (Numero decimal): "))
kg = float(input("Ingresa tu peso en kg (Numero decimal): "))

datosp_tupla = (nombre, apellido, edad, RH, h, kg)
datosp_dic = {'Nombre': nombre, 'Apellido': apellido, 'Tipo de Sangre': RH, 'Edad': edad, 'Altura': h, 'Peso': kg}
print("Tus datos personales son: ", datosp_dic)

## Ejemplo...Outfit para Navidad:
print("**Ingrese el nombre de una prenda y su valor promedio (numero entero, sin decimales, sin puntos)**")

s0 = input("Ingrese nombre de la prenda: ")
d0 = int(input("Ingrese valor promedio de {} (numero entero, sin decimales, sin puntos): " .format(s0)))

s1 = input("Ingrese nombre de la prenda: ")
d1 = int(input("Ingrese valor promedio de {} (numero entero, sin decimales, sin puntos): " .format(s1)))

s2 = input("Ingrese nombre de la prenda: ")
d2 = int(input("Ingrese valor promedio de {} (numero entero, sin decimales, sin puntos): " .format(s2)))

s3 = input("Ingrese nombre de la prenda: ")
d3 = int(input("Ingrese valor promedio de {} (numero entero, sin decimales, sin puntos): " .format(s3)))

s4 = input("Ingrese nombre de la prenda: ")
d4 = int(input("Ingrese valor promedio de {} (numero entero, sin decimales, sin puntos): " .format(s4)))

print('--------------------------------------------------------------------------------------------------')
nom_prenda_set = {s0, s1, s2, s3, s4}
print("Tus 4 prendas de navidad son ", nom_prenda_set)

prendas_dic = {s0: d0, s1: d1, s2: d2, s3: d3, s4: d4}

val_prom = [d0, d1, d2, d3 , d4]
nom_prenda = [s0, s1, s2, s3, s4]

if 'A+' in RH:
  print("Tienes la misma sangre del programador")

elif 'O-' in RH:
  print("Tienes una sangre especial")

elif 'AB-':
  print("Tienes la sangre mas escasa del planeta")

else:
  print("Estas dentro del grupo de RH dado por (A-, AB+, 0+, B+, B-)")

if 'Villa' in apellido:
  print("Tienes el mismo apellido del programador")

if d0 >= 1000000 and d1 >= 1000000:
  print("Tus prendas {} y {} son costosas" . format(nom_prenda[0], nom_prenda[1]))

elif d2 < 100000:
  print("Tu prenda {} es relativamente barata" .format(nom_prenda[2]))

else:
  print("Me gustan las prendas que elegiste: ", prendas_dic)

for i in nom_prenda_set:
  print(i)

for x in val_prom:
  if x >= 10000 and x <= 100000:
    print("precios razonables")
  
  elif x > 1000000:
    print("¿QUE COMPRAS?")
  
  else:
    print("Ojo, lo Barato sale caro")

while edad >= 20:
  print(edad)
  edad += 1
  if edad == 81:
    print("Te quedan aprox. 60 años de vida")
    break 

RH_Tipos_list = ['A+', 'A-', 'AB+', 'AB-', 'O+', 'O-', 'B+', 'B-']

for i in RH_Tipos_list:
  print(i)
  if i in RH:
    print("Tu tipo de sangre es {}" .format(RH))
    break


   
