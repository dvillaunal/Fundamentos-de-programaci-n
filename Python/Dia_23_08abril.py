import numpy as np, random

#--------------------------------------------Librería NumPy--------------------------------------------#
'''
Comprender las funciones de NumPy antes de reinventar la rueda

¿Qué es NumPy?:

-> NumPy es una biblioteca Python numérica de código abierto.

-> NumPy contiene una matriz multidimensional y estructuras de datos matriciales.
-> Se puede utilizar para realizar una serie de operaciones matemáticas en matrices,
como rutinas trigonométricas, estadísticas y algebraicas.
Por lo tanto,
la biblioteca contiene una gran cantidad de funciones matemáticas,
algebraicas y de transformación.

-> NumPy es una extensión de Numeric y Numarray.

-> Numpy también contiene generadores de números aleatorios.

-> NumPy es un contenedor de una biblioteca implementada en C.

-> Los objetos Pandas dependen en gran medida de los objetos NumPy.
Esencialmente, Pandas extiende Numpy.
'''

# Matriz unidimensional:
'''
Para crear una matriz NumPy:
'''
a = np.array ([1,2,3])

'''
Para crear una matriz Python (Sin NumPy):
'''

# Una manera:
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(None)

print("numpy: ", a)
print("list:  ", matriz)

# Matriz multidimensional:
'Nota: Una matriz multidimensional tiene más de una columna'
a = np.array([1,2,32,1,2,3])
b = np.array ([1,2]) # 1D 
c= np.array ([[1,2], [10,20]]) # 2D

for i in [a,b,c]:
  print('----')
  print(i)
  print('----')

'''
Si desea crear una matriz 3-D:
Esto creará 3 matrices con 4 filas y 5 columnas
cada una con números enteros aleatorios.
'''
array_3D = np.random.randint(10, size=(3, 4, 5))
print(array_3D)

"Nota: Hay varias formas diferentes de crear una matriz:"

# matriz sin ningún elemento:

np.empty (2) # esto creará una matriz 1D de 2 elementos 
np.empty ([2,3]) # esto creará una matriz 2D (2 filas, 3 columnas cada una)

# matriz con ceros:

np.zeros(2) # creará una matriz 1D con 2 elementos, ambos 0 

# matriz con 1:

np.ones(2) # esto creará una matriz 1D con 2 elementos, ambos 1

'Si desea crear una matriz Numpy a partir de una secuencia de elementos, como de una lista'

np.asarray ([1,2])

# Adición / eliminación / clasificación de elementos:
'''
Podemos realizar una serie de operaciones rápidas en una matriz Numpy.
Esto hace que Numpy sea una biblioteca deseable para los usuarios de Python.
'''

# Para agregar elementos:
'''
Para agregar elementos NumPy:
'''
x = [0] 
np.append (x, [1,2])
print(x)

'''
Para agregar elementos Python (Sin NumPy):
un elemento a la vez.
'''
lista = [1]
lista.append(2)
lista.append(3)

# Para eliminar elementos:

'''
Para agregar elementos NumPy:
'''

a = np.delete ([0,1,2], 1)

'''
Para agregar elementos Python (Sin NumPy):
un elemento a la vez.

uno de los metodos.....
.pop()
'''

lista.pop()

print(a,'<= NumPy |Somos Diferentes| Default =>' ,lista)


# Funciones y atributos de la matriz NumPy:

'Un objeto ndarray tiene varios atributos, como:'

'''
shape = para encontrar las dimensiones
(números de columna / fila) de una matriz:
'''

a = np.array([[1,2],[3,4]])

print(a.shape)

'''
el método reshape ()
si desea cambiar la forma de una matriz sin copiar ningún dato:
'''

array = np.arange (10) # Esto devuelve una matriz 1D de 10 elementos 
array.reshape (2,5) # Esto devolverá una matriz de 2 filas, 5 columnas


'Nota: Si queremos encontrar el número de dimensiones de una matriz'

p = np.array([[1,2], [3,4]]) 
print (p.ndim)

'Si queremos encontrar la longitud de cada elemento de una matriz:'

p = np.array([0,1,2]).itemsize 
print (p)

# Funciones matemáticas:
'''
Numpy ofrece una gama de potentes funciones matemáticas.
Esta es una de las razones por las que la biblioteca es popular en los campos cuantitativos.
'''
## Sumar, Restar, Multiplicar, Dividir, Potencia, Mod:
'''
NumPy:
'''
a = [1,2] 
b = [3,4] 

suma = np.add(a, b) 
resta = np.subtract(a, b) 
mul = np.multiply(a, b) 
div = np.divide(a, b) 
p0 = np.power(a, b) 
p1 = np.power(a, 2) 
#para obtener el resto 
m = np.mod(a, b)

'Python (Default):'
a.extend(b)

'''
El restar listas (no esta predefinido)
'''

c = []

for x in a:
    for y in b:
        c.append(x*y)

print(c) #Listas multiplicadas, mucho codigo

'''
de aqui para adelante:
es mucho codigo y no es nada versatil
como podemos verlo, esta libreria facilita,
muchas cosas
'''

# Algebra:
'''
1. dot() #producto puntual de dos arreglos 
2. inner() #producto interno de dos arreglos
3. determinant() #determinante de un arreglo 
4. solve() #resuelve la ecuación de la matriz
5. inv() #inversa de la matriz
6. matmul()#matrix producto de dos matrices
'''
