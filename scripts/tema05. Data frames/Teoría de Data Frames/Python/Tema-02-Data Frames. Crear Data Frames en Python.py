
## CONSTRUIR DATA FRAMES EN PYTHON

import pandas as pd
import numpy as np 

#Para crear un Data Frame se usa la función pd.DataFrame()
#dentro de la función se inserta un diccionario donde las
#claves son el nombre de las columnas y los valores son los 
#parámetros de dichas columnas en la tabla del DF
#np.random.rand() genera número aleatorios
#NP.random.randn() genera número aleatorios normalizados
df = pd.DataFrame({
	"A":np.random.rand(10),
	"B":np.random.rand(10),
	"C":np.random.rand(10)
	})

#media por columnas
print(df.mean())
#media por columnas
print(df.mean(axis="columns"))

#Creamos otro data frame con sos columnas (key y values)
#El parámetro adicional columns permite poner el nombre de las columnas
df2 = pd.DataFrame({
    'key':['A', 'B', 'C', 'A', 'B', 'C'],
    'values':range(6)
}, columns = ['key', 'values'])

print(df2)
#Algo típico en analisis de datos cualitativos es 
#agrupar a todos aquellos que son de la misma naturaleza
#Se hace con data_frame.groupby()
df2.groupby("key") #Es objeto abastracto de python

print(df2.groupby("key").mean())

help(pd.DataFrame)