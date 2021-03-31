
'''
En Python, el ciclo while se usa par ejecutar un número
de declaraciones hasta que la condición especificada sea verdadera.
Una vez que la condición sea falsa, el control saldra del ciclo

El ciclo while se construye así:

while [a condition is True]:
    [do something]

'''

a = 10

while a > 0:
    print("Valor de a es ", a)
    a -= 1
print("El ciclo esta completo")


x = int(input("Ingrese un valor menor a 10 (numero entero): "))

while x <= 15:
    x += 1
    if x%2 == 0:
        continue
    print(x)
print("imprime los numeros primos, despues del numero escogido, hasta el 15")

## Bucle while:
'Con el tiempo bucle podemos ejecutar un conjunto de instrucciones, siempre y cuando se cumpla una condición.'

while a <= 6:
  print("a es {}" .format(a))
  a += 1

'Con la sentencia break podemos detener el ciclo incluso si la condición while es verdadera:'

w = float(input("Ingrse un numero decimal menor a 5: "))

while w < 100:
  print("El valor actualizado de w es {}".format(w))
  if w == 90:
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

for i in range(100):
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
    
'''
Escriba un algoritmo que sume los números positivos ingresados por el usuario y cuando la suma sea superior a 100 deje de pedir números y muestre el total.
'''

s = 0
n = int(input("Ingrese un numero entero positivo: "))

while n > 0:
    s = s+n
    if s > 100:
        break
    n = int(input("Ingrese el otro valor entero a sumar: "))

print("El total es: ", s)

'''
Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
'''

s = input("¿Desea continuar el programa?: ")

while type(s) == str:
    if s != 'sí':
        s = input("¿Desea continuar el programa?: ")
    elif s == 'sí':
        print('¡Hasta la vista!')
        break

        
