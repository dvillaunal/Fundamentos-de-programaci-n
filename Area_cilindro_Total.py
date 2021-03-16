'''
**Área Total del Cilindro**
Cree un programa en Python 3 que le solicite al usuario la altura de un cilindro y el radio de su base,
y luego calcule el área del cilindro tapado.
El programa debe mostrar como resultado exclusivamente el área total del cilindro redondeada a dos cifras decimales,
no debe contener letras ni enunciados que lo acompañen.

Nota: usar pi como 3.14 (pi=3.14).

por ejemplo si el usuario ingresa una altura de  8 y un radio de la base de 3, el programa debe mostrar: 

207.24
'''

# Definimos PI según los parametros dados
pi = 3.14

#Funcion para Radio de la Esfera
def radio():
    rad = input("Por favor Ingresa El Radio para Calcular el Aréa: ")
    return rad
r = float(radio())

#Funcion para Radio de la Esfera
def altura():
    h = input("Por favor Ingresa la Altura para Calcular el Área: ")
    return h

H = float(altura())

# AREA LATERAL
AL = (2 * (pi * r) * (H))

# AREA DE LA BASE
AB = (pi * (r ** 2))

# AREA TOTAL
def areat():
  AT = ((2 * AB) + AL)
  return AT

At = areat()
print("El Área Total del Cilindro es:", "%.2f"% At)