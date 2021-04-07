import calendar

'''
Python define un módulo incorporado
'calendar' que maneja las operaciones relacionadas con el calendario:

'module Calendar' permite la salida de calendarios como el programa
y proporciona funciones útiles adicionales relacionadas con el calendario.
Las funciones y clases definidas en el módulo Calendario utilizan un calendario idealizado,
el actual calendario gregoriano extendido indefinidamente en ambas direcciones.
De forma predeterminada, estos calendarios tienen el lunes como primer día de la semana
y el domingo como último (la convención europea).
'''

yy = int(input('Ingresa El Año [2000, =>] a Imprimir (Numero entero): '))
mm = int(input('Ingresa El Mes [1-12] a Imprimir (Numero entero): '))
dd = int(input('Ingresa un día [1-31] (Numero entero): '))

# Almanaque
a = open('ALMANAQUE.txt', 'w')
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2021,2, 1, 1, 2), file=a)
a.close()
print('Disfruta de tu Almanaque en el archivo "ALMANAQUE.txt"')

'''
<class calendar.Calendar>:

clase Calendario crea un objeto Calendario.
Un objeto Calendario proporciona varios métodos que se pueden utilizar
para preparar los datos del calendario para formatearlos.
Esta clase no se formatea por sí misma.
Este es el trabajo de las subclases.
La clase de calendario permite los cálculos para varias tareas
en función de la fecha, el mes y el año.
'''
print('-------------------------------')
# iterweekdays():
'''
Devuelve un iterador para los
números de días de la semana que
se utilizarán durante una semana.

Sintaxis: iterweekdays()
Parametro: None
Return: iterator for the week day numbers
'''

j = calendar.Calendar(firstweekday = 1)
  
for d in j.iterweekdays():
    print(d)

# .itermonthdates():
'''
itermonthdates() El método devuelve un iterador para el mes (1–12) del año.
Este iterador devolverá todos los días del mes
y todos los días antes del inicio del mes o después
del final del mes que se requieren para obtener una semana completa.

Sintaxis: itermonthdates (año, mes)

Parámetro:
  año: año del mes calendario
  :mes del calendario

Devuelve: un iterador para el mes.
'''

j = calendar.Calendar()
  
for d in j.itermonthdates(2020, 10):
    print(d)


# .monthdatescalendar()
'''
monthdatescalendar()
El método en Python se usa para obtener
una lista de las semanas del mes del año como semanas completas.

Sintaxis: monthdatescalendar (año, mes)

Parámetro:
  año: año del mes calendario
  :mes del calendario

Devoluciones: una lista de las semanas del mes.
'''
for i in j.monthdatescalendar(2021, 1):
    print(i)

# monthdays2calendar():
'''
monthdays2calendar():
El método en Python se usa para obtener
una lista de las semanas del mes del año como semanas completas.


Sintaxis: monthdays2calendar (año, mes)

Parámetro:  
  año: año del mes calendario
  :mes del calendario

Devoluciones: una lista de las semanas del mes.
'''
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(j.monthdays2calendar(yy, mm))

# yeardatescalendar():
'''
yeardatescalendar():
El método en Python se usa para obtener una lista de las semanas
del mes del año como semanas completas.
Las entradas en las listas de la semana son números de días.
Los números de días fuera de este mes son cero.

Sintaxis: yeardatescalendar (año, ancho)

Parámetro:
  año: año del calendario
  ancho:  [Predeterminado: 3] número de meses en cada fila.

Devuelve: una lista de filas de meses.
'''

print(j.yeardatescalendar(yy))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class calendar.TextCalendar:

La clase TextCalendar se puede utilizar para generar calendarios de texto sin formato.
La clase TextCalendar en Python le permite editar el calendario y usarlo según sus necesidades.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

'''
isleap(año):
Esta función comprueba si el año mencionado en el argumento es bisiesto o no .

Días bisiestos(año1, año2):
Esta función devuelve el número de días bisiestos entre los años especificados en argumentos.
'''

def bis(age):
  '''
  Indentificador de años bisiestos
  formato: age = 'Numero Entero (int)'
  '''
  if (calendar.isleap(age)):
    s = print ("El año es Bisiesto")
    return s
  else:
    n = print ("El año no es Bisiesto")
    return n

bis(yy)


'''
Vamos a Calcular Tu Horoscopo
'''
def horos(d, m):
  '''
  Calcula Tu Horoscopo.
  formato: d = dia (entero)
    m = mes (nuemro entero)
    imprime calendario de año dado anteriormente 
  '''
  if ((m == 3) and (d >= 21)) or ((m == 4) and (d <= 20)):
    signo = 'aries'
  signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
  fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
  m -= 1
  if d > fechas[m]:
    m += 1
  if m == 12:
    m = 0
  p = print("***Tu signo es: {}***" .format(signo[m]))
  c = print(calendar.month(yy, mm))
  return p, c

horos(dd, mm)

print('Disfruta de tu Almanaque en el archivo "ALMANAQUE.txt"')
