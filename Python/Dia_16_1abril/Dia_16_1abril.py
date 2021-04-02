# Manejo de archivos de texto en Python
'''
Crear archivos en python usando With

Esta cláusula establece automáticamente un contexto para la ejecución segura
debido a que crea un punto de partida de configuraciones iniciales y al finalizar recupera los valores anteriores.
Y en el caso de la apertura de un archivo este automáticamente ha de cerrarlo
una vez terminada la función que lo involucre,
así como también se realiza una limpieza de la memoria utilizada.

Por esto creo que la forma correcta de manipular archivos es utilizando
la cláusula with aunque veo muchos tutoriales y cursos donde se enseña
a abrir y crear ficheros solo utilizando
el método open (lo que no está mal pero tampoco es lo mas optimo)
'''
from io import open

# Forma clasica de crear un archivo:

txt = open("Ejemplo0.txt", 'w') # Ruta donde crearemos el fichero, w indica escritura (puntero al principio)

txt.write('Esto es un Ejemplo\nOtra linea de texto') # Escribimos el Texto

txt.close() # Cerramos el fichero

# Lectura:
'Nota: Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)'
txt = open("Ejemplo0.txt", 'r')

'Lectura completa'
t = txt.read()

'Cerramos el fichero'
txt.close()

print(t)

'Nota: Podemos usar el método readlines() del fichero para generar una lista con las líneas:'

txt = open("Ejemplo0.txt", 'r')

list_t = txt.readlines()

txt.close()

print(list_t)

# Extensión:
'Este modo nos permite añadir datos al final de un fichero:'

'''
Nota:
Ruta donde leeremos el fichero,
"a" indica extensión (puntero al final)
'''

txt = open("Ejemplo0.txt", 'a')

txt.write('\nSoy una extensión, es decir, Estoy al final')

txt.close()

'''
NOTA:
La variante "a+" permite crear el fichero si no existe

# txt0 = open('Ejemplo1.txt', 'a+')
'''
# Manejando el puntero:
'''
Es posible posicioar el puntero en el fichero manualmente usando el método seek
e indicando un número de caracteres para luego
leer una cantidad de caracteres con el método read:
'''
txt = open("Ejemplo0.txt", 'r')

txt.seek(5)

txt.read(13)

'''
Para posicionar el puntero justo al inicio de la segunda línea,
podríamos ponerlo justo en la longitud de la primera:
'''

txt = open("Ejemplo0.txt", 'r')

txt.seek(0)

'Nota: Leemos la primera línea y situamos el puntero al principio de la segunda'
txt.seek(len(txt.readline()))

t = txt.read()
txt.close()
print(t)

print('----------------------------------------------------------------------------')

# Modificar una línea:

'''
Para lograr este fin lo mejor es leer todas las líneas en una lista,
modificar la línea en la lista,
posicionar el puntero al principio y
reescribir de nuevo todas las líneas:
'''

txt = open("Ejemplo0.txt", 'r+')
list_t = txt.readlines()

'Modificamos la línea que queramos a partir del índice'

list_t[0] = 'Hola Mundo\n'

'Volvemos a ponter el puntero al inicio y reescribimos'

txt.seek(0)
txt.writelines(list_t)
txt.close()

with open("Ejemplo0.txt", 'r') as txt:
  print(txt.read())

print('----------------------------------------------------------------------------')

#Utilizando with as:

with open("fichero.txt", 'w') as fichero: #Creamos el archivo
  fichero.write("Creando archivo de texto en python usando with as")
  fichero.close()

'''
> Método Seek(byte):

Este método se corresponde al puntero que te mencionaba y junto al método tell()
nos permitirá ubicarnos al final o al principio de los archivos.
Pero el método seek() fue diseñado para archivos binarios, no para archivos de texto.

Este método moverá el puntero hacia el byte indicado como argumento.

> Método Tell():

El método tell() devuelve el puntero a una posición en un momento dado.
Junto con seek() nos permitirán posicionarnos al principio o al final.

Tell() nos devuelve un entero que indica la posición del puntero.
'''


# Ejercicio:

dir_acordes = 'Dios_me_Ama.txt'
while (True):
  try:
    with open(dir_acordes, 'r+') as acordes:
      contenido = acordes.read()
      print(contenido)
      break
  except:
    print("Error al intentar abrir: ", dir_acordes)
    print('**COPIE LO SIGUIENTE (tal cual esta ahí):** ')
    print('ACORDES/Dios_me_Ama.txt')
    print('---------------------------')
    dir_acordes = input("Especifique su ubicación: ")
