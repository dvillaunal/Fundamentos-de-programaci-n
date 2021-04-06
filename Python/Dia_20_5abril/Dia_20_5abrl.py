from datetime import datetime, date

# Fecha de nacimiento str a datetime:
e = open('EDAD.txt', 'r')
lista_e = e.readlines()
f_born_str = lista_e[1]

fborn_date = datetime.strptime(f_born_str, '%d/%m/%Y')

# Fecha actual str a datetime:
d = open('DIA.txt', 'r')
lista_d = d.readlines()
f_today_str = lista_d[1]
ftoday_date = datetime.strptime(f_today_str, '%d/%m/%Y')

# Archivo save:
r = open('Resultados.txt', 'w')

def date(d):
  """
  Calcula Tu Edad
  """
  # año:
  def cal_age():
    """
    Calcula, edad en años
    solo recibe:
    fn = <type: date>
    """
    t_a = ftoday_date.year - d.year
    t_a -= ((ftoday_date.month, ftoday_date.day) < (d.month, d.day))
    return t_a
  # mes:
  def cal_month():
    """
    Calcula, edad en meses
    """
    hoy = datetime.now()
    inicio = datetime.strptime(d.strftime('%d/%m/%Y'), '%d/%m/%Y')
    t_m = inicio.month- hoy.month
    return t_m
  # día:
  def cal_day():
    """
    Calcula, edad en días
    """
    today = datetime.now()
    inicio_d = datetime.strptime(d.strftime('%d/%m/%Y'), '%d/%m/%Y')
    t_d = inicio_d.day - today.day
    return t_d
  tu_edad = 'Tu edad es: {} años, {} meses, {} días\n'.format(cal_age(), cal_month(), cal_day())
  return tu_edad

r.write('EDAD:\n')

edad = date(fborn_date)
r.write(edad)

# Proximo cumpleaños:

#meses faltantes:
def falm_cum(fm):
  """
  Proximo cumpleaños en meses:
  formato fm = 'dd/mm/aaaa'
  """
  dia_cumple = datetime.strptime(fm, '%d/%m/%Y')
  today = datetime.now()
  delta = dia_cumple.month - today.month
  mf = 'Faltan {} meses para tu cumpleaños\n'.format(delta)
  return mf
meses_faltantes = falm_cum(f_born_str)

r.write(meses_faltantes)

# dias faltantes:
def fald_cum(fd):
  """
  Proximo cumpleaños en días:
  formato fd = 'dd/mm/aaaa'
  """
  dia_cumple = datetime.strptime(fd, '%d/%m/%Y')
  today = datetime.now()
  delta = dia_cumple.day - today.day
  df = 'Faltan {} días para tu cumpleaños\n'.format(delta)
  return df
dias_faltantes = fald_cum(f_born_str)

r.write(dias_faltantes)

# Resumen:
import datetime
r.write('Resumen #1\n')
def time(t):
  fecha_de_hoy = datetime.datetime.now()
  dif = fecha_de_hoy - t
  dias_vividos = dif.days
  segundos_vividos = dif.seconds
  horas_vividas, segundos_vividos = divmod(segundos_vividos, 3600)
  minutos_vividos, segundos_vividos = divmod(segundos_vividos, 60)
  dmhs = "{} día(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)\n".format(
			dias_vividos, horas_vividas, minutos_vividos, segundos_vividos)
  return dmhs

dmhs = time(fborn_date)
r.write(dmhs)


r.write('Resumen #2\n')
r.write('---Has Vivido---\n')

def dmaEdad(f):
    """
    Calcula meses y semanas vividas hasta la fecha
    f = fecha de nacimiento
    f = 'aaaa/mm/dd'
    """
    f = datetime.datetime.strptime(f, '%d/%m/%Y').date()
    hoy = datetime.date.today()
    aa = hoy.year - f.year
    aa -= 1
    dias = (hoy-f).days
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    milisegundos = segundos * 1000
    meses = ((hoy.year - f.year) *12) + (hoy.month - f.month)
    meses -= 1
    semanas = int(round(dias/7, 0))
    ms = '{} Años\n{} Meses\n{} Semanas\n{} Días\n{} Horas\n{} minutos\n{} Segundos\n{} Milisegundos'.format(aa,
                                                                               meses,
                                                                               semanas,
                                                                               dias,
                                                                               horas,
                                                                               minutos,
                                                                               segundos,
                                                                               milisegundos)
    return ms

ms = dmaEdad(f_born_str)
r.write(ms)

r.close()

'''
Si edad_persona <= 2:
  la edad en años caninos es = edad_persona * 10.5

SI edad_persona > 2:
  La edad en años caninos es = 21 + (edad_persona - 2) * 4
'''
from datetime import datetime, date

age_can = open('age_dog.txt', 'a')


def calcan(age):
  today = datetime.now()
  a= today.year - age.year
  a -= 1
  if a > 0:
    if a <= 2:
      c0 = (a * 10.5)
      ec0 = 'La edad en años caninos es {}'.format(c0)
      return ec0
    else:
      c1 = (21 + (a-2) * 4)
      ec1 = 'La edad en años caninos es {}'.format(c1)
      return ec1
  else:
    n = print("Su Fecha esta mal Digitada")
    return n

ec = calcan(fborn_date)

age_can.write(ec)
age_can.close()
ac = open('age_dog.txt', 'r')
ycan = ac.read()
ac.close()
print(ycan)
