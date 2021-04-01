# Estructura try/except

'''
Las excepciones son bloques de código que nos permiten continuar
con la ejecución de un programa pese a que ocurra un error.

Ejemplo:

*NO EJECUTAR*
print("Hola Mundo"

¿Para qué sirve manejar las excepciones en python?

Manejar los errores nos va  a permitir evitar que nuestro programa
deje de funcionar de golpe y nos va a dar la posibilidad
de mostrar un error personalizado al usuario
en vez de los clásicos errores del intérprete Python.

'''

'''
Bloques try - except

Para prevenir el fallo debemos poner el código propenso a errores
en un bloque try y luego encadenar un bloque except
para tratar la situación excepcional mostrando que ha ocurrido un fallo
'''

try:
  e = int(input("Ingresa una letra: "))
  print((e+2)**2)
except:
  print("Soy un ejemplo de except, Tienes un Error")

'''
Podemos aprovechar las excepciones para forzar al usuario
a introducir un número haciendo uso de un bucle while,
repitiendo la lectura hasta que lo haga correcto:
'''
print("Ahora con while")
while (True):
  try:
    e = int(input("Ingresa una letra: "))
    print((e+2)**2)
    break # Importante romper la iteración si todo ha salido bien
  except:
    print("Soy un ejemplo de except, Tienes un Error, [[ahora intenta con un Numero Entero]]")

#Bloque else
'''
Es posible encadenar un bloque else después del except para comprobar
el caso en que todo funcione correctamente (no se ejecuta la excepción).

El bloque else es un buen momento para romper la iteración con break
si todo funciona correctamente:
'''

print("----------------------------------------------------")
from math import sin, pi

while (True):
  try:
    for i in [2,3,4,6]:
      print(i)

    an = int(input("Ingresa uno de los anteriores numeros numeros: "))
    if an in [2,3,4,6]:
      angulo_no = sin(pi/an)
      print("El angulo notable {}, su Valor en seno es {}" .format(an, angulo_no))
    else:
      print("No ingresaste uno de los numeros deseados")
  except:
    print("Ingresa un numero entero")
  
  else:
    print("Ya no lo repitiras")
    break

# Bloque finally

'''
Por último es posible utilizar un bloque finally
que se ejecute al final del código,
ocurra o no ocurra un error:
'''

while (True):
  try:
    for i in [2,3,4,6]:
      print(i)

    an = int(input("Ingresa uno de los anteriores numeros numeros: "))
    if an in [2,3,4,6]:
      angulo_no = sin(pi/an)
      print("El angulo notable {}, su Valor en seno es {}" .format(an, angulo_no))
    else:
      print("No ingresaste uno de los numeros deseados")
  except:
    print("Ingresa un numero entero")
  
  else:
    print("Ya no lo repitiras")
    break
  
  finally:
    print("Fin") # Siempre se ejecuta
  
# Excepciones Multiples:
'''
En una misma pieza de código pueden ocurrir muchos errores distintos
y quizá nos interese actuar de forma diferente en cada caso.

Para esas situaciones algo que podemos hacer es asignar una excepción a una variable.

De esta forma es posible analizar el tipo de error que sucede gracias a su identificador:
'''
try:
  txt_not = int(input("Ingrese un numero entero:"))
  txt = txt_not.split()
except Exception as nt:
  print("Ha ocurrido un error ->", type(nt).__name__)

'''
Nota:
Cada error tiene un identificador único que curiosamente se corresponde con su tipo de dato.
'''

# print(type(nt))

'Es similar a conseguir el tipo (o clase) de cualquier otra variable o valor literal:'

print(type(12).__name__)
print(type(0.0003).__name__)
print(type({}).__name__)
print(type(()).__name__)
print(type([]).__name__)

'''
Gracias a los identificadores de errores podemos crear múltiples comprobaciones,
siempre que dejemos en último lugar la excepción por defecto Excepcion que engloba
cualquier tipo de error
(si la pusiéramos al principio las demás excepciones nunca se ejecutarían):
'''

try:
  txt_not = int(input("Ingrese un ¿numero entero?:"))
  txt = txt_not.split()
except TypeError:
  print("No se puede utilizar .split() en un numero entero")
except ValueError:
  print("Debes introducir un numero Entero")
except Exception as nt:
  print("Ha ocurrido un error no previsto->", type(nt).__name__)

# Invocación de excepciones:
'''
En algunas ocasiones quizá nos interesa llamar un error manualmente,
ya que un print() 'común' no es muy elegante:
'''

def f(x=None):
  if x == None:
    print("¡Error! No se permite un valor nulo (con un print)")

f()

# Instrucción raise:
'''
Gracias a raise podemos lanzar un error manual pasándole el identificador.
Luego simplemente podemos añadir un except para tratar esta excepción que hemos lanzado:
'''
def f(x=None):
  try:
    if x == None:
      raise ValueError("No se permite un valor nulo")
  except ValueError:
    print("No se permite un valor nulo (desde except)")
    
f()
