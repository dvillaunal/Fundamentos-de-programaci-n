import pandas as pd
import xlrd
import warnings
import numpy as np
from numpy import random

# ejecutar un bloque de código y capturar las advertencias:
with warnings.catch_warnings():
	# ignorar todos los avisos de captura:
	warnings.filterwarnings("ignore")
	# ejecutar código que generará advertencias
print('intente hacer try y except para suprimir el error y no me dio')

# Ejercicio 1:
'''
Base de datos tomada de:
http://superalumnos.net/base-de-datos-de-ejemplo-inmobiliaria
tomando solo los primeros 100 archivos

los datos tomados corresponde a la venta de inmuebles (terrenos)
con el nombre de vendedores correspondiente
tomando a 'NA = no se sabe'

> Los Items son:

-> TIPO DE INMUEBLE
-> VENTA O ALQUILER
-> LUGAR O PROVINCIA
-> TAMAÑO DEL TERRENO (m^2)
-> Precio de venta en miles de pesos $
-> Nombre del vendedor
'''

base = pd.ExcelFile('Inmueble.xls')

df = base.parse('Hoja1')

dic = df.to_dict()
# Haciendo diccionarios con cada Item:

s_tipo = pd.Series(dic['Tipo'])
s_oper = pd.Series(dic['Operación'])
s_lugar = pd.Series(dic['Provincia'])
s_nom = pd.Series(dic['Vendedor'])

# Haciendo un conteo de cada item:
c_tipo = s_tipo.value_counts()
c_oper = s_oper.value_counts()
c_lugar = s_lugar.value_counts()
c_nom = s_nom.value_counts()

c_lugar.to_excel('Conteo_Provincias.xls')
c_oper.to_excel('Conteo_Operaciones.xls')
c_nom.to_excel('Conteo_Nombres.xls')
c_tipo.to_excel('Conteo_Tipo.xls')

des = df.describe()
des.to_excel('Estadisticas_Basicas_Super_Precio.xls')

print('intente hacer try y except para suprimir el error y no me dio')

# Ejercio 2:
# Observar de cada xls creado , generar apartir de la medio y desviación estandar:
'''
Generar un tabla con numeros pseudoaletorios
primero empezamos con un array, despues a data frame y por ultimo guardarlo en xls
una tabla para Superfice y otr para precio de venta.
'''
print(des)
nomr_su = random.normal(loc = 162.848485, scale=80.843306, size=(10,10))
nomr_pre = random.normal(loc = 1.179969e+06, scale=6.542468e+05, size=(10,10))

dnomr_su = pd.DataFrame(nomr_su)
print(dnomr_su)

dnomr_pre = pd.DataFrame(nomr_pre)
print(dnomr_pre)

dnomr_su.to_excel('Distr_Normal_PseudoAletorio_Superfice.xls')
dnomr_pre.to_excel('Distr_Normal_PseudoAletorio_Precio.xls')
