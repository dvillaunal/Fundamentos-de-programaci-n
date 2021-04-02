# LISTS

'''
Las listas se utilizan para almacenar múltiples elementos en una sola variable.

Las listas son uno de los 4 tipos de datos incorporados en Python que se utilizan
para almacenar colecciones de datos, los otros 3 son Tuple, Set y Dictionary,
todos con diferentes cualidades y usos.

-> Nota: las listas siempre tienen el primer indice [0]

-> Nota2: Cuando decimos que las listas están ordenadas,
significa que los artículos tienen un orden definido y ese orden no cambiará.
Si agrega nuevos elementos a una lista,
los nuevos elementos se colocarán al final de la lista.

-Hay algunos métodos de lista que cambiarán el orden, pero en general:
el orden de los elementos no cambiará.

-> Nota3: Dado que las listas están indexadas,
las listas pueden tener elementos con el mismo valor:

'''
## Ejemplo de Lista basica:
'como vemos esta lista podemos tener variedad de tipos de datos => bool, int, float,...,etc'
lista = ["lista", 1, "lista", 12, True]
print(lista) # ["lista", 1, "lista", 12]

"tenemos funciones como len(), que determina cuantos elementos tiene una lista"

print(len(lista)) # 5 elementos

"una vez más tenemos una función predefinida y esta nos ayuda a crear listas de maneras diferentes"
lista_f = list(("lista", 1, "lista", 12, True))
print(lista_f)

# Acceso a los elemntos de una lista:

print(lista[0])
print(lista_f[0:4])

'''
dentro de este tema... estan la indexación negativa,
entre otras cosas que estan explicadas en el anterior repl

-> otra cosa que podemos acer es acceder a las listas y cambiar el valor de ellas
'''

lista[0] = 45
lista_f[1:3] = ["Hola", False, 21]
lista[2] = lista_f[1]
print(lista) # [45, 1, 'Hola', 12, True]
print(lista_f) # ['lista', 'Hola', False, 21, 12, True]
'''
Nota: La longitud de la lista cambiará cuando el número de elementos insertados
no coincida con el número de elementos reemplazados.

algo util  para las lista es el metodo .apppend() => sirve para agregar nuevos
elementos a una lista

otro más especifico en donde agregar elementos es .insert(# a donde quiere que vaya el elemnto, elemnto a ingresar)
'''

x = int(input("ingresa un numero entero para agregar a la lista: ")) # numero ingresado: 132
lista.append(x)
print(lista) # [45, 1, 'Hola', 12, True, 132] => vemos que se agrego el valor de x

lista_f.insert(0, x)
print(lista_f) #[132, 'lista', 'Hola', False, 21, 12, True]

"algo basico de las listas es que podemos sumarlas entre ellas (ojo solo sumarlas, es igual a .extend()"

lista_new = lista + lista_f
print(lista_new)

"podemos eliminar elentos de una lista"

lista_f.remove(132)
print(lista_f) # vemos que elimino el 132 que tenia, no discrimina por indexación

lista_new.pop(4) #aquie vemos que solo eliminara el elemento N°4 de la lista indicada
print(lista_new)


# Orden dentreo de las listas

'''
algo que me llamo mucho la antención fue el hecho que con los siguientes comando podemos organizar las listas:

> .sort() orden alfabéticamente  o numéricamente
> .sort(reverse = True) oreden descendente respecto al alfabeto o numeros

sort() no discrimina entre mayusculas y minusculas

> .reverse() invierte el orden de clasificación actual e los elementos

'''

# Ejemplo:

x1 = input("ingrese su primer nombre: ")
x2 = input("ingrese apellido: ")
y1 = int(input("ingrese edad en años: "))
y2 = float(input("ingrese estatura en cm: "))
peso = float(input("ingrese su peso en Kg: "))

lista = [x1, x2, y1, y2]

print(lista)

lista.append(peso)
print(lista)

lista_txt = lista[0:2]
lista_txt.sort(reverse= True)
print(lista_txt)

lista_num = lista[3:5]
lista_num.sort()
print(lista_num)
lista.reverse() # invertir el orden dado
print(lista)
