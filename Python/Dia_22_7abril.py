# Diferencias de tiempos (timedelta):
'''
La función .timedelta() de Python está presente en la biblioteca de fecha y hora,
que generalmente se usa para calcular diferencias en las fechas y
también se puede usar para manipulaciones de fechas en Python.
Es una de las formas más sencillas de realizar manipulaciones de fechas.

Sintaxis:
  datetime.timedelta(días = 0,
                      segundos = 0,
                      microsegundos = 0,
                      milisegundos = 0,
                      minutos = 0,
                      horas = 0,
                      semanas = 0)

Return:
  Fecha
'''
from datetime import datetime, timedelta

# Un ejemplo de datedelta:

e = open('Example.txt', 'w')

print("Microseconds = ", timedelta(microseconds = 1), file=e)
print("Milliseconds = ", timedelta(milliseconds = 1), file=e)
print("Seconds      = ", timedelta(seconds = 1), file=e)
print("Minutes      = ", timedelta(minutes = 1), file=e)
print("Hours        = ", timedelta(hours = 1), file=e)
print("Days         = ", timedelta(days = 1), file=e)
print("Weeks        = ", timedelta(weeks = 1), file=e)

print('--------------------timedelta attributes--------------------', file=e)
# timedelta attributes:
'''
atributos timedelta El objeto datetime timedelta tiene tres atributos especiales

min, max, resolution

para devolver la diferencia:
más negativa,
más positiva y
más pequeña
entre dos objetos timedelta no iguales.
'''
print("Minimum = ", timedelta.min, file=e)
print("Maximum = ", timedelta.max, file=e)
print("Resoultion = ", timedelta.resolution, file=e)

e.close()

# Leer un archivo precargado:

fa = open('Fecha_Actual.txt', 'r')

fecha_str = fa.readlines()

fa.close()

list_t = []

for i in fecha_str:
  list_t.append(i)

frm = list_t[1]
t = list_t[0]

'''
Python proporciona el método .strptime(),
en su clase datetime, para convertir una representación
de cadena de la date/time en un objeto date
'''
t_date = datetime.strptime(t, frm)

r0 = open('Resultado0.txt', 'a')

print('Clase de t_date = {}'. format(str(type(t_date))), file=r0)
print('{} <= Este es diferente a este => {}\n'. format(str(t_date),str(t_date)), file = r0)

# Calculando futuros datos para dos años
Futura_Fecha_despues_2years = t_date + timedelta(days = 730)
  
Futura_Fecha_despues_2dias = t_date + timedelta(days = 2)

print('Futura_Fecha_despues_2dias: {}\n'.format(Futura_Fecha_despues_2dias), file=r0)
print('Futura_Fecha_despues_2years: {}\n'.format(Futura_Fecha_despues_2years), file=r0)
r0.close()

# Restar una cantidad específica de días, de segundos a un objeto de tipo datetime con timedelta:
r1 = open('Resultado1.txt', 'w')
days = 1000

today = datetime.now()

otra_d = today - timedelta(days, 0)
otra_s = today - timedelta(0, 30)

print('Dias Restados Con timedelta = \n{}'.format(otra_d), file=r1)
print('Segundos Restados Con timedelta = \n{}'.format(otra_s), file=r1)

print('------Substraer 10 días a la fecha actual------', file=r1)

r = today - timedelta(10)

print('Fecha actual:', today, file=r1)
print('10 días antes de la fecha actual:', r, file=r1)

yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)
print('-----Obtener la fecha de ayer, hoy y mañana-----', file=r1)
print('AYER = {}, HOY = {}, MAÑANA = {}'.format(str(yesterday), str(today), str(tomorrow)), file=r1)

r1.close()

r2 = open('Resultados2.txt', 'w')

print('Horas: 00 hasta las 23')
print('Minutos: 00 hasta las 60')
print('Segundos: 00 hasta las 60')
print('Formato = %H:%M:%S')

s1 = input('Ingrese una "date" con el formato dado: ')

s2 = input('Ingrese una "date" con el formato dado (el que se va restar): ')

FMT = '%H:%M:%S'

print(s1, file=r2)
print(s2, file=r2)
print(FMT, file=r2)


tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

print('Diferencia entre: s1 = {} y s2 = {}'.format(s1,s2), file=r2)
print('Resultado = {}'.format(tdelta), file=r2)

if tdelta.days < 0:
    tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    print('s1 es menor que s2 por dias',file=r2)


r2.close()

r2 = open('Resultados2.txt', 'r')
resultado2 = r2.read()
print('------Resultados2.txt---------')
print(resultado2)
r2.close()
