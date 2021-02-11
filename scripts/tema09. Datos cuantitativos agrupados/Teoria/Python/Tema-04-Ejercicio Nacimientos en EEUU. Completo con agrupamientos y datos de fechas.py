
""" Análisis del nacimiento de bebés en EEUU """

# Vamos a trabajar con un nuevo tipo de datos: fechas.
# Ejemplo completo de análisis cuantitativo

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

births = pd.read_csv("../../../../data/us-births.csv")

#Explorar los datos
#Ver si están las filas y columnas
print(births.shape) # ~15.500 filas de datos
print("")
print(births.head(3))
print("")
print(births.tail(3))
print("")


#Realizar una tabla bidimensional con pivot_table
#Empleamos para agrupar los nacimientos los años y el genero
births_yg = births.pivot_table("births", index="year", columns="gender", aggfunc="sum")
print(births_yg)
print("")


#Vamos a agrupar los datos por décadas para mejorar su descripción
#Añadimos la columna "decade" al dataset
#Para añadir la "s" hay que transformar a string el tipo de columna
births["decade"] = (births["year"]//10)*10
births["decade"] = births["decade"].astype(str) +"s"

print(births.head(3))
print("")

births_dg = births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
print(births_dg)
print("")


#Para definir el estilo de colores del gráfico según seaborn
sns.set()
#Figura del nº de nacimientos por año en EEUU
births.pivot_table("births", index="year", columns="gender", aggfunc="sum").plot()
plt.ticklabel_format(useOffset=False, style='plain') #Desactivar notación científica
plt.ylabel("Total of births")
plt.xlabel("Year")
plt.title("Number of births by year in EEUU")
plt.show()
plt.close()


#Limpiar los datos que no interesan
#Calculo de cuartiles de variable "births"
quartiles = np.percentile(births["births"],[25,50,75])
#Mediana
median = quartiles[1]
#Rango intercuartilico
IQR = quartiles[2]-quartiles[0]
#Parámetro de desviación de los datos (no es el dato literal)
sigma = 0.75*IQR


#Filtrar los datos con query()
#Esta técnica se utiliza en machine learn cuando:
# -No se puede estimar la desciación gaussiana y la media literalmente
#@median y @sigma trasladan las variables definidas
#Va a eliminar factores extraños que distorsionan los datos
births = births.query("(births > @median - 5*@sigma) & (births < @median + 5*@sigma)")
print(births.shape) # ~14.500 filas de datos
print("")


#La columna "day" debería convertirse a nº entero
#Estaba en float y ahora está en formato int
#Lo emplearemos para elaborar las fechas
births['day'] = births['day'].astype(int)


#Las fechas son datos que se conocen como: SERIES TEMPORALES
#No se ven aquí, en su lugar creamos un: DATETIME
#Modificamos el índice del DF con pd.to_datetime()
#Le pasamos como parámetros a suma de años, meses y días
#empleando format="%Y%m%d"
#Obtenemos las fechas (year/month/day)
births.index = pd.to_datetime(10000*births.year+100*births.month+births.day, 
	format="%Y%m%d")
print(births.head(3))
print("")


#Creo nueva columna que se llame día de la semana a partir
#del índice generado anteriormente
#Empleo la función "dayofweek" 
#En "dayofweek" la semana empieza en 0 (lunes)
births['dayofweek'] = births.index.dayofweek
print(births.head(3))
print("")


#Calculo la media de nacimientos por decada y día de la semana
births_dwd = births.pivot_table('births', index='dayofweek', columns='decade', aggfunc="mean")
print(births_dwd)
print("")

#Representación anterior
births_dwd.plot()
plt.gca().set_xticklabels(['', 
	"L", "M", "X", "J", "V", "S", "D"])
plt.ylabel("Media de nacimientos")
plt.xlabel("Día de la semana")
plt.title("Mean of births per day of week")
plt.show()
plt.close()
print("")



#Obtenemos la media de nacimientos en función del
#mes y el día (function "month" y "day")
births_by_date = births.pivot_table('births', 
	index=[births.index.month, births.index.day], 
	aggfunc="mean")
print(births_by_date.head())
print("")

#Incorporo un index en formato DATETIME 
#Elijo un año bisiesto para que no falte un día (2020)
births_by_date.index = [pd.datetime(2020, month, day) 
                        for (month, day) in births_by_date.index]
print(births_by_date.head())
print("")

#Represento el gráfico anterior de la media de nacimientos
#por dia del mes
births_by_date.plot()
plt.show()
plt.close()