# Strings

'''
Para trabajar con Strings primero debemos tener una definición clara de estas
por ende, tomare la definición del taller 2 (FdP):

Las variables de tipo string se utilizan para almacenar texto,
o cadenas de caracteres. Una string es un caso muy particular de una lista;
es una lista de caracteres de texto que no puede ser modificada.
Para evitarse la tarea de tener que escribir cada carácter individualmente como
lo haríamos normalmente para una lista, en los strings basta con escribir
el texto que se desee almacenar entre comillas y asignarle una variable.
'''

## 'p' = "p"

'''
en string son lo mismo:

'' = ""

para las multilines pasa lo mismo.

'''

### Ejemplos:
h1 = 'hola'
h2 = "Hola" 
print(h1, h2) # Resultado -> hola  Hola

## Strings como Matrices.....

a = "Navega dentro del String"

print(a[4]) # Resultado -> g
### utilizando las propedadesde las matrices

print(a[0:7])  # Resultado -> Navega 
print(a[:15])  # Resultado -> Navega dentro d
print(a[1:])   # Resultado -> avega dentro del String
'''
Se podria ver cada unas de las propedades, pero el punto esta claro,
podemos navegar entre los strings

hay más como bucles, mirar la longitud (funciones predefinidas),  pero en mi caso este
lo tengo mas que claro así poniendo solo los ejemplos
'''
### Ejemplos:
f = "Felipe"
for i in f:   # Resultado -> F e l i p e
  print(i)

print(len(f)) # Resultado -> 6

"""# Check String
unas de las cosas que más me llamaron la atención fue esta sección:

comprobar si una frase o caracter esta presente en un string, algo muy util
a la hora de filtrar una base de datos....sirve para hayar en textos complejos palabras
necesarias, es decir, sus utilidades son gigantes
"""

### Ejemplo:


frase = "Voy a comprobar si en este texto estara una W"

print("W" in frase, "comprobarr" in frase)  #Resultado -> True, False
"""
con in comprobamos si esta frase esta, pero existe un complemento not in,
sirve para comprobar si un elemento NO esta en el string
"""
print("z" not in frase, "hola" not in frase)  #Resultado -> True, True


# Moddificar Strings

'''
Esta sección tambien e llamo la atención, ya que sirve por ejemplo:

cuando se hace un encuesta por casualidades o una mala redacción en la base de datos
cuando se digitan nombres, que esten en mayuscula la 1ra letra de estas

Ejemplo:

DanIel FElIpE vIlla REngifo   ¿Como arreglamos esto?

Bueno....

aqui dejo las mas relevantes para mi:

upper() -> Convierte todo en mayusculas
lower() -> Convierte todo en minusculas
replace() -> Reemplaza unos caracteres o cadenas por otros
Split() -> Divide la cadena en subcadenas con un separador definido

{un parentesis....los strings se pueden concatenar entre ellos....es algo muy facil
como sumar variables}

'''

## Ejemplos:
"si lo desea escribalo con mayusculas en desorden"
nombre = input("ingrese su primer o unico nombre: ") # Intente con dAniEL

nombre_MAYUS = nombre.upper()
print("su nombre con todoas las letras en mayúscula: ", nombre_MAYUS)

nombre_min = nombre.lower()
print("su nombre en minuscula: ", nombre_min)

nombre_nm = nombre.replace(nombre[0], "F")
print("¿Su nombre cambio?...¿tiene sentido?: ", nombre_nm)

nombre_DIV = nombre_min.split("a")
print("dividi mi nombre: ", nombre_DIV)




# Veamos algunos errores y como corregirla:
PBM = 15
'''
x = "mi Puntaje Basico de Matricula es "
y = x + PBM
si lo pones fuera de las comillas dara un error
'''

## no se pueden combinar strings con varibles numericas
"para estos casos esta el metodo format()"

### Uso dde format(), Ejemplos:

y = "mi Puntaje Basico de Matricula es {}"
print(y.format(PBM))

'''
por defecto el toma en el orden dentro de los (), aplicandolos a los {}
para estos casos donde quisieramos cambiar el orden predeterminado de format:
'''
Nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
semestre = int(input("ingresa un numero entreo del semestre cursado actualmente: "))

txt = "mi nombre es {2}, estudio en la UNALMED con {0} años y estoy cursando actualmente el semestre N°{1}"
print(txt.format(edad, semestre, Nombre))

# Escape Characters:

'''
muchas veces queremos dejar unos espacios o algunas comillas para citar
pero en ocaciones nos salen errores ya que el programa puede malinterpretar
lo que queremos que haga....para estos casos esta:

\n -> hace una nueva linea
\" ó \' -> forma de citar dentro de las comillas
\t -> tab
\b -> dejar un espacio o Backspace
'''

# NOTA: Todos los metodos de String devuelven nuevos valores. NO cambian el String original

