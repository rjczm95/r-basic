
## DATOS CUANTITATIVOS (ANÁLISIS DE RAUW DATA)

# Vamos a desarrollar un ejemplo con datos de planetas
# para obtenerlos utilizaremos la librería Seaborn
# El dataset que cargamos se llama planets

import seaborn as sns
planets = sns.load_dataset("planets")

#Vemos las dimensiones del dataset
print(planets.shape)
print ("Hay 1035 filas y 6 columnas")
print(" ")

# Vemos las primeras filas
print(planets.head())
print(" ")

# Eliminamos los "na" existentes en el DF y aplicamos describe
print(planets.dropna().describe())
print(" ")

# Sumatorio de la columna distance
print(planets.distance.sum())
print(" ")

# Productorio de la columna distanc
# Da infinito porque el resultado es muy grande
print(planets.distance.prod())
print(" ")

# Desviación media absoluta  de la columna distance
# Formula LaTeX: $$\frac{\sum_{i=1}^n |x_i -\bar{x}|}{n}$$
print(planets.distance.mad())
print(" ")

# Varianza muestral de la columna distance
print(planets.distance.var())
print(" ")

# Desviación estándar muestral de la columna distance
print(planets.distance.std())
print(" ")

#Esto agrupa por la columna "method"
planets.groupby('method')
#Agrupo por "method", selecciono la columna "orbital_period"
#aplico la mediana para la columna seleccionada
print(planets.groupby('method')["orbital_period"].median())
print(" ")

#Hago un bucle por el DF agrupado según "method"
#Imprimo el método vs la disposición (shape) del mismo sub-DF
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))
print(" ")

#Ver la información estadística para el conjunto de datos
#agrupados según los "method" para la variable de "year"
print(planets.groupby('method')['year'].describe())
print(" ")


#Agrupar los descrubimientos según el método y la decada
#del descubrimiento

#Con esto obtenemos la decada (1990, 2000, 2010...)
decada = 10 * (planets["year"]//10)
#Tansformo a string y le añado una "s" al final
decada = decada.astype(str) +'s'
print(decada)
print(" ")
# Le doy un nombre para poder incluirlo como columna adicional
# o para poder utilizarlo en un groupby
decada.name = "decade"

#Agrupo por dos columnas (method y decada)
#Selecciono como valor a tratar la columna number
#Aplico el sumatorio sum()
#Para desapilar los datos emplea unstack() (mejor formato)
#Aparecen muchos NaN endonde no hay valores
#para transformarlo a cero se emplea fillna(0)
print(planets.groupby(['method', decada])['number'].sum().unstack().fillna(0))


