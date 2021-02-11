
### OTRAS ALTERNATIVAS PARA REPRESENTAR HISTOGRAMAS ###

## Histogramas con paquete Seaborn

import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Seaborn tiene un método que se llama:
#   - distplot()
# Se encarga de pintar, simultáneamente, el histograma 
# de frecuencias y la función de distribución estimada.
# Solo es posible emplearlo para 1 dimensión.


np.random.seed(2019)
#Generamos los datos como Series
size, scale = 1000, 10
data = pd.Series(np.random.gamma(scale, size=size))

#Dibujamos con sns.distplot()
sns.distplot(data)
plt.show()


#Otros datos del estudio ("x")
x = np.random.laplace(loc=10, scale=3, size=1000)

#sns.set_style() permite cambiar el estilo de los gráficos
sns.set_style("darkgrid")
sns.distplot(x)
plt.show()

#La función sns.distplot() tiene un parámetro que permite 
#indicar que función de distribución representar.
#Este parámetro es "fit"
#Para que no dibuje la distribución estimada se indica kde=False
sns.distplot(data, fit=stats.laplace, kde=False)
#A la hora de elegir una determinada distribución teórica 
#de laplace , elige la que mejor se ajusta a los datos.
#Esto se denomina estimación de parámetros, o también, en
#estadística inferencial se llama la bondad de ajuste.
#Es decir como de bien se ajustan unos datos a una distribución.
plt.show()


## PANDAS tiene la función "value_counts()"
# Se encarga de calcular el histograma de valores no
# nulos a partir de un objeto Series de PANDAS

#Nuevos datos a analizar creados por una distribución aleatoria
#Hacemos que la probabilidad (p) del 1º sea menor y vaya aumentando con el aumento de la unidad
data2 = np.random.choice(np.arange(10), size=10000, 
	p=np.linspace(1,11,10)/60)

# Transformo a Series el data 2 en PANDAS
s = pd.Series(data2)

#Cuenta la frecuencia absolutas de aparición del objeto "s"
print("")
print(s.value_counts())
print("")


#Se puede normalizar el resultado obteniendo las 
#frecuencias relativas de "s"
print(s.value_counts(normalize=True))
print("")

#Hacemos las dicisiones en intervalos arbitrarios
#variable de estudio definida
ages = pd.Series([1,1,3,5,6,8,9,10,12,15,18,18,18,20,25,30,40,51,52])
#extremos de intervalos definidos a mano
bins = (0,10,15,18,21,np.inf)
#Etiquetas de intervalos
labels = ("infancia","preadolescencia","adolescencia","universitario","adulto")

#Hacemos el agrupamiento de los datos con pd.cut()
groups = pd.cut(ages, bins=bins, labels=labels)

#Frec. Abs. (Histograma)
print(groups.value_counts())
print("")

#Frec. Rel. (Histograma)
print(groups.value_counts(normalize=True))
print("")

#Concateno los datos por filas y genero un DF (pd.concat())
#Renombramos las columnas con rename()
print(pd.concat((ages,groups), axis=1).rename(columns={0:"age",1:"group"}))
print("")









