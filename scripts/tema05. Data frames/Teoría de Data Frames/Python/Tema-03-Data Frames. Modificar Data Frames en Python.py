
## MODIFICAR Y AGREGAR DATOS AL DATA FRAME EN PYTHON

import pandas as pd
import numpy as np 

#Creamos un DF de ejemplo para esta clase
#np.random.randint(0, 100, 6) permite generar nºs aleatorios
#entre 0 y 100, indicando que queremos seis numeros
df = pd.DataFrame({
       'key' : ['A', 'B', 'C', 'A', 'B', 'C'],
       'value1': range(6),
       'value2': np.random.randint(0, 100, 6)
})


""" Función AGGREGATE() """

#aggregate() puede tomar un string, una función, o lista de
#operaciones para calcular los agregados indicados en el DF
a1 = df.groupby("key").aggregate(['min', np.median, np.mean, max])
#si es una función de python se puede pasar entre comillas
#se pueden pasar funciones de np
#también se pueden pasar palabras reservadas de python
print(a1)

#se le puede pasar un diccionario a aggregate() indicando
#la función que se le quiere aplicar a cada una de las 
#columnas del DF
a2 = df.groupby('key').aggregate({
    'value1': ['min',max],
    'value2': 'max'
})
print(a2)


""" Función FILTER() """

#df.filter()
#Se encarga de filtrar datos que queramos en función de una condición booleana, eliminando
#datos del DF original en función de una serie de 
#propiedades.
b1 = df.groupby("key").std()
print(b1)

#Se define una función de filtrado
def filter_std (DF):
	return DF["value2"].std() > 5
#Nos quedamos con los datos que cumplen la función
print(df.groupby("key").filter(filter_std))


""" Función TRANSFORM() """
#df.transform()
#vamos a recuperarlo a traves de una función lambda
#sirve para obtener una versión reducida de los datos
#pero sin combinar
#se conservar el tamaño de la tabla original
c1 = df.groupby('key').transform(lambda x: x - x.mean())
#La función toma la media de cada uno de las "key" y
#se lo resta al valor original
print(c1)


""" Función APPLY() """
#apply() permite aplicar cualquier función arbitraria
#al conjunto de los datos de un DF
#el parámetro debe ser un objeto DF y devuelve un objeto pandas
#que sera data frame, serie o un numero

#Queremos normalizar la primera columna de datos según
#los valores de la segunda
def norm_by_col2(x):
	#se divide value1 entre el sumatorio de value 2
    x['value1'] /= x['value2'].sum()
    return x

print(df.groupby('key').apply(norm_by_col2))

