print("Ingrese el nombre y valor (respectivamente de un elemento de la canasta familiar")

canasta_fam = {}
lista_val = []
lista_clave = []

for x in range(5):
  x+=1
  print("Elemento N°", x)
  clave = input("Ingrese el nombre del producto: ")
  valor = int(input("Ingrse el valor del producto (numero entero): "))
  canasta_fam.update({clave: valor})
  lista_val.append(valor)
  lista_clave.append(clave)


print("Tabla de productos y sus precios")
for a,b in canasta_fam.items():
  print(a,"->", b)


'Si todos los productos de la tienda, por cuestión de aniversario les restan el 30% del valor total'
canasta_des = {}

y = len(lista_val)
y = y-1
print(y)
for x in range(y):
  lista_val[x] = lista_val[x] - (lista_val[x]*(0.3))
  canasta_des.update({lista_clave[x]: lista_val[x]})

print("Productos con el 30% de descuento")
for a,b in canasta_des.items():
  print(a,"->", b)

for i in canasta_des.values():
  i = round(i,2)
  for x in range(4):
    canasta_des.update({lista_clave[x]: i})

print("Productos redondeados")
for a,b in canasta_des.items():
  print(a,"->", b)

'''
Como la tienda no puede perer ha decido,
subir, regresarle el 10% del valor redondeado hasta que cumpla con los precios establecidos,
(sin sobrepasarlos) 
'''

for x in canasta_des.values():
  while x <= 1000:
    x = x + (x*(0.1))
    for i in range(4):
      canasta_des.update({lista_clave[i]: x})
    x += 1
  else:
    continue
  

print("Productos Arreglados")
for a,b in canasta_des.items():
  print(a,"->", b)

for i in canasta_des.values():
  i = round(i,2)
  for x in range(4):
    canasta_des.update({lista_clave[x]: i})

print('Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.')

s = "Anita lava la tina"
print("Frase del ejercicio: ", s)
dic ={}

for i in s:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for key, val in dic.items():
  print(key, "->", val)

s = input("Ahora intentalo tu!: ")

while len(s) < 18:
  s = input("Intenta de nuevo, esta vez con una frase de 18 letras: ")

dic ={}

for i in s:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for key, val in dic.items():
  print(key, "->", val)
