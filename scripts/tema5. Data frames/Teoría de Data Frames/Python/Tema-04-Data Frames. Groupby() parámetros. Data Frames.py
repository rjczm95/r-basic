
## PÁRAMETROS DE GROUPBY() PARA DATA FRAME EN PYTHON

import pandas as pd
import numpy as np 

#Párametros de la función groupby()

df = pd.DataFrame({
       'key' : ['A', 'B', 'C', 'A', 'B', 'C'],
       'value1': range(6),
       'value2': np.random.randint(0, 100, 6)
})
print(df)

#Creamos una lista para utilizarla en groupby()
#Cada posición de L se corresponde con una fila del DF
#Las posiciones que tienen el mismo parámetro pertenecerán
#a la misma fila del sub-DF obtenido por groupby
L = [0,1,0,1,2,0]

#se suma los valores de las filas 0,2,5 por un lado
#se suma los valores de las filas 1,3 por otro lado
#la fila 4 se queda tal cual estaba
one = df.groupby(L).sum()
#El nombre de la fila se asigna según el parámetro de L
print (one)

#El ejemplo clásico es agrupar por una columna no numérica
#El nombre de la fila se asigna según la columna "key"
print(df.groupby('key').sum())

#El resultado es el mismo que el anterior pero
#aquí se le asigna un vector obtenido del DF
print(df.groupby(df['key']).sum())

#set_index() permite configurar el indice de las filas del DF
#según el parámetro dado (en este caso la columna key)
#será A, B o C.
df2 = df.set_index('key')
print(df2)

#Creo un diccionario
#Transformo las categorias A, B y C
#en dos que son vowel y consonant
mapping = {
    'A': 'vowel',
    'B': 'consonant',
    'C': 'consonant'
}

#Le paso el dicionario al DT a través de groupby
#El indice de las filas se agrupara con vowel y consonant
#El groupby en sí mismo no devuelve ninguna función
print(df.groupby(mapping))
print(df2.groupby(mapping).sum())

#Se le pueden pasar a groupby() una función entera de python
#str.lower pasa a minuscula los index de las filas
print(df2.groupby(str.lower).mean())

#se pueden combinar modos de agrupación generando
#dos claves para el index de las filas
print(df2.groupby([str.lower, mapping]).mean())

