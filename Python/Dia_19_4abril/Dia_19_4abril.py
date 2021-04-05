import datetime, calendar
from datetime import date, time, timedelta


f = open('CALENDAR.txt', 'w')

ahora = datetime.datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora, file = f)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow(), file = f)  # Muestra fecha/hora UTC
print("Día:",ahora.day, file = f)  # Muestra día
print("Mes:",ahora.month, file = f)  # Muestra mes
print("Año:",ahora.year, file = f)  # Muestra año
print("Hora):", ahora.hour, file = f)  # Muestra hora
print("Minutos:",ahora.minute, file = f)  # Muestra minuto
print("Segundos:", ahora.second, file = f)  # Muestra segundo
print("Microsegundos:",ahora.microsecond, file = f)  # Muestra microsegundo

print("\nHoras:\n", file = f)
hora1 = time(21, 19, 12)  # Asigna 21h 19m 12s
print("\n\tHora1:\n", hora1, file = f)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\n\tHora2:\n", hora2, file = f)

print("\tHora1 < Hora2:", hora1 < hora2, file = f)

print("\nFechas:\n", file = f)
f1 = date.today()  # Asigna fecha actual
print("\n\tfecha1:\n", f1, file = f)


f2 = date.today() + timedelta(days=2)
print("\n\tFecha2:\n", f2, file = f)

print("\n\tf1 > Fecha2:", f1 > f2, file = f)

day_week = datetime.datetime.isoweekday(f1)
t_dayweek= ("Lun", "Mar", "Mié", "Jue","Vie", "Sáb","Dom")

st_daywekk = str(t_dayweek)

f.write(st_daywekk)

print('\n', file=f)

print('Fecha aaaa-mm-dd: ',f1,'# Día de la Semana',"->",day_week,"->", 'Nombre, día de la semana: ',t_dayweek[day_week-1], file=f)

#calendario
print('\n', file=f)
print('------------Calendario del mes de abril 2021------------', file=f)
print('\n', file=f)


age = date.today().year 
mes = date.today().month
calendario_mes = calendar.month(age, mes)
print(calendario_mes, file=f)

f.close()

# Almanaque
a = open('ALMANAQUE.txt', 'w')
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2021,2, 1, 1, 2), file=a)
a.close()


f = open('CALENDAR.txt', 'w')

ahora = datetime.datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora, file = f)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow(), file = f)  # Muestra fecha/hora UTC
print("Día:",ahora.day, file = f)  # Muestra día
print("Mes:",ahora.month, file = f)  # Muestra mes
print("Año:",ahora.year, file = f)  # Muestra año
print("Hora):", ahora.hour, file = f)  # Muestra hora
print("Minutos:",ahora.minute, file = f)  # Muestra minuto
print("Segundos:", ahora.second, file = f)  # Muestra segundo
print("Microsegundos:",ahora.microsecond, file = f)  # Muestra microsegundo

print("\nHoras:\n", file = f)
hora1 = time(21, 19, 12)  # Asigna 21h 19m 12s
print("\n\tHora1:\n", hora1, file = f)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\n\tHora2:\n", hora2, file = f)

print("\tHora1 < Hora2:", hora1 < hora2, file = f)

print("\nFechas:\n", file = f)
f1 = date.today()  # Asigna fecha actual
print("\n\tfecha1:\n", f1, file = f)


f2 = date.today() + timedelta(days=2)
print("\n\tFecha2:\n", f2, file = f)

print("\n\tf1 > Fecha2:", f1 > f2, file = f)

day_week = datetime.datetime.isoweekday(f1)
t_dayweek= ("Lun", "Mar", "Mié", "Jue","Vie", "Sáb","Dom")

st_daywekk = str(t_dayweek)

f.write(st_daywekk)

print('\n', file=f)

print('Fecha aaaa-mm-dd: ',f1,'# Día de la Semana',"->",day_week,"->", 'Nombre, día de la semana: ',t_dayweek[day_week-1], file=f)

#calendario
print('\n', file=f)
print('------------Calendario del mes de abril 2021------------', file=f)
print('\n', file=f)


age = date.today().year 
mes = date.today().month
calendario_mes = calendar.month(age, mes)
print(calendario_mes, file=f)

f.close()

# Almanaque
a = open('ALMANAQUE.txt', 'w')
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2021,2, 1, 1, 2), file=a)
a.close()
