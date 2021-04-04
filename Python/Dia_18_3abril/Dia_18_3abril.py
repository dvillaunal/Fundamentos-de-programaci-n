# Librería String y sus aplicaciones

'''
(realice al menos dos ejercicios que requieran leer archivos en formatos *.txt
y guarden las respuestas a los ejercicios en archivos *.txt independientes)
'''

'''
Las constantes en el módulo de cadena se pueden usar para especificar
categorías de caracteres como ascii_letters y dígitos.
'''
import string, random

for x in dir(string):
  print('----------')
  print(x)
  print('----------')

else:
  print('+++++++++++++++++++++++++++++++')
  print('                                 ')
  print('                                 ')

'''
La librería string viene por defecto (puede ser invocada sin necesidad de ser instalada)
en Python 3, permite acceder a atributos nuevos relacionados con los strings,
observe a continuación sus usos más comunes:
'''

# Guia del modulo String:

g = open('Guia_String.txt', 'w')
g.write('Guia del modulo String:')
g.write('\n')

list_dir = dir(string)
print(list_dir[0])
try:
  basestring
except NameError:
  basestring = str

for i in dir(string):
  if i.startswith("_"):
    continue
  x = getattr(string, i)
  if isinstance(x, basestring):
    print('%s=%s' % (i, repr(x)))
    print()
    v = repr(x)
    g.write(i)
    g.write('  =  ')
    g.write(v)
    g.write('\n')

g.close()


# .capwords() => Convierte la primera letra de cada palabra en texto
s = "No hay nadie que ame el dolor mismo, que lo busque, lo encuentre y lo quiera, simplemente porque es el dolor."

print(s)
print(string.capwords(s))

'''
Nota:
Los resultados son los mismos que si llamara split (),
pusiera en mayúscula las palabras en la lista resultante
y luego llamara a join () para combinar los resultados.
'''

# .translate() le doy valores numericos (algo como criptografia) a letras
'Repetimos valores, porque solo se le asignan digitos, no numeros'

x = 'Nutrición de las mayores puntuaciones. Profesionalismo.'

print(x)
x.translate(str.maketrans('aeiou', '12345'))


# Templates:
'''
Esta clase se usa para crear una plantilla de cadena
para sustituciones de cadena más simples:
'''
t = string.Template('La $orq funciona bajo el $umbrella de la "Schola" ($gener).')
txt = t.substitute(orq= 'orquesta', umbrella= 'paraguas', gener= 'Betholdiana')
print(txt)

## Ejercicios:

txt0 =  open('texto0.txt', 'r')
t0 = txt0.read()

def verifica(value): 
    for l in value:
      if l not in string.ascii_uppercase:
        return False
    return True

x = 0
for i in t0:
  if verifica(i) == False:
    x += 1
  else:
    print(verifica(i))

print("Se hallaron {} minusculas" .format(x))

r0 = open('resultado0.txt', 'w')
r0.write('Vamos a Codificar el Texto')

for i in t0:
  x = random.randint(0,9)
  sx = str(x)
  if i != ' ' or i != '  ':
    r0.write('VALOR:   ')
    r0.write(i)
    t0.translate(str.maketrans(i, sx))
    r0.write(' = ')
    r0.write(sx)
    r0.write('\n')
  elif i != '.' or  i != '. ':
    r0.write('VALOR:   ')
    r0.write(i)
    t0.translate(str.maketrans(i, sx))
    r0.write(' = ')
    r0.write(sx)
    r0.write('\n')
  else:
    None



r0.write('\n')
r0.write('\n')
r0.write(t0)
r0.close()

txt1 = open('texto1.txt', 'r')
t1= txt1.read()

def invertir_cadena(c):
    return c[::-1]

r1 = open('resultado1.txt', 'w')

T1 = t1.upper()
inv = invertir_cadena(T1)

r1.write('Mensaje Invertido')
r1.write('\n')
r1.write(inv)

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrado = ""
n = 8

for l in inv:
    if l in abc:
        pos_letra = abc.index(l)
        nueva_pos = (pos_letra + n) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        cifrado+= l

r1.write('\n')
r1.write('\n')
r1.write('Mensaje Cifrado')
r1.write('\n')
r1.write('\n')
r1.write(cifrado)
r1.close()
