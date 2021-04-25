"Protocolo:
1. Daniel felipe villa Rengifo
2. Lenguaje Utilizado R
3. Tema: Escriba un programa de 'Hola Mundo'. Recuerde incluir los comentarios a las líneas de código
4. Fuentes utilizadas:
https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/print
"
"Lamentablemente R no maneja comentarios multilínea, hay un truco, que no se si es muy bueno que digamos y que pasa por escribir una cadena común multilínea"

# Con message evitaremos que el sistema los reconozca como lineas de cogigo impreso, algo mas parecido a un waring.

message("--------------------------------------")

message("Así como imprimimos en python\n(es decir, el mismo comando)\nprint(Valores a imprimir)")

message("--------------------------------------")

print('Mi primer reto con R')

message("--------------------------------------")

message("print imprime su argumento\ny lo devuelve de forma invisible (mediante invisible(x)).\nEs una función genérica,\nlo que significa que se pueden añadir fácilmente\nnuevos métodos de impresión para nuevas clases.")
message("--------------------------------------")

print('Hola Mundo')
