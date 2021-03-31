# Diccionarios

'''
-> Hoy Veremos el segundo tipo de datos de recopilación en Python.
Los diccionarios se utilizan para almacenar valores de datos en pares clave: valor.
Un diccionario es una colección ordenada *, modificable y que no admite duplicados.

Los diccionarios se escriben con llaves y tienen claves y valores:
diccionario = {'clave_1': valor_1, 'clave_2': valor_2,....,'clave_n': valor_n}
'''

## Ejemplo:

"Precios de objetos cotidianos"
dic = {'Reloj': 100, 'Camisa': 150, 'Gorra': 50}
print(dic)

"Podemos imprimir el valor de una clave:"
print(dic['Reloj'])

## Changeable:

'''
Los diccionarios se pueden cambiar, lo que significa que podemos cambiar,
agregar o eliminar elementos después de que se haya creado el diccionario.
'''

dic['Pantalón'] = 200 # Agrega un nuevo valor
dic['gafas'] = 32
dic['Gorra'] = 75

del(dic['gafas']) # Elimina la clave y el valor seleccionado

## No se permiten duplicados:
'Nota: Los diccionarios no pueden tener dos elementos con la misma clave'
'<carro = {"marca": mazda, "modelo": 2002, "año": 2002}>' # Si lo ejecutas sale error

## Acceder a elementos:

"podemos tomar el valor de una clave:"
x = dic['Gorra']
y  = dic.get('Gorra')

print(x)
print(y)

"Obtenga una lista de las claves:"
z = dic.keys()

print(z)

"Obtenga una lista de los valores:"
z = dic.values()

print(z)


## Diccionarios Anidados:

'''
algo muy curios de los diccionarios...es que se pueden anidar, esto es util
cuando tenemos mcuhos datos o muestras por grupos, en el caso mio siendo un estadista
ayuda a tener un orden logico sobre las muestras dadas, facilitando el trabajo de observación.
'''
n = input("ingresa tu nombre para anidarlo a un diccionario: ")
e = int(input("ingrese tu edad (numero entero) para anidarlo a un diccionario: "))
ns = int(input("ingresa tu semestre cursado actualmente (numero entero): "))

dic_ani = {
    "Muestra_1": {
        "nombre": "Daniel",
        "edad": 19,
        "N°_semestre": 4
    },
    "Muestra_2": {
        "nombre": "Sara",
        "edad": 17,
        "N°_semestre": 2
    },
    "Muestra_input": {
        "nombre": n,
        "edad": e,
        "N°_semestre": ns
    }
}

print(dic_ani, "Disfruta de tus datos anidados") 

## Metodos de Diccionario:

'''
A comparación de sus hermanos (Arrays), hasta ahora es el tipo de datos de recopilación
con tan pocos metodos...la verdad este es el Arrays que menos me ha confundido respecto a utilizarlos

'''

# Ejemplos:

"Utilizando los input() anteriores: "
'-> Semestres Faltantes => una suposición en la cual termine la carrera en 10 semestres'

ejemplo = {'Nombre': n, 'Edad': e, 'Semestres Faltantes': 10-ns}

print(ejemplo)

d = int(input("Dias de codigo hechos hasta ahora: "))

'Utilizando condicionales:'

if 'Nombre' in ejemplo:
  ejemplo.update({'Dias de Codigo': d})
  print("Los datos del Diccionario son de {}." .format(ejemplo['Nombre']))
  print(ejemplo)


