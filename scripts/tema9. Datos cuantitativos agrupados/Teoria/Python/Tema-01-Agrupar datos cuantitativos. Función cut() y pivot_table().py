
""" AGRUPAR DATOS CUANTITATIVOS """

## Función pd.cut() y df.pivot_table() en Python


# En esta clase vamos a centrarnos en dos apartados:
# - La función pd.cut()
# - La tabla de pivotaje (df.pivot_table())

# La tabla de pivotaje es una operación muy empleada en
# hojas de cálculo y otros programas que operan con datos
# tabulares



#SINTAXIS pivot_table()
#DataFrame.pivot_table(data, values=None, index=None, columns=None, aggfunc="mean", fill_value=None, margins=False, dropna=True, margins_name = "All")
#El parámetro "aggfunc" establece la función (por defecto es mean)
#El parámetro "fill_value" permite rellenar los NA
#El parámetro "margins" da las marginales (total por rows y por columns)
#El parámetro "dropna" permite que no tome los valores NA en las operaciones
#El parámetro "margins_name" para poner nombre a las filas o columnas que genera "margins"


# La tabla de pivotaje toma un conjunto de datos en forma
# de columna como entrada y hace agrupaciones de las 
# entradas en una tabla bidimensional que proporcione un
# resumen estadístico multidimensional de la información

# Suele confundise la groupby() con pivot_table() pero no
# es lo mismo

import numpy as np
import pandas as pd
import seaborn as sns

#Vamos a emplear el dataset titanic del paquete seaborn
#age es la edad de los pasajeros
#fare es el precio del billete
titanic = sns.load_dataset("titanic")
print(titanic.head(3))
print("")

#Agrupamos por género ("sex")
#Seleccionamos la columna de supervivientes ("survived")
#Aplicamos la función mean()
average_suv_s = titanic.groupby("sex")[["survived"]].mean()
print(average_suv_s)
print("")


#Agrupamos por genero ("sex") y clase ("pclass")
#Seleccionamos la columna de supervivientes ("survived")
#Aplico la media con aggregate("mean")
#Uso la función unstack() para desapilar la tabla
average_suv_sp = titanic.groupby(["sex","pclass"])[["survived"]].aggregate("mean").unstack()
print(average_suv_sp)
print("")


#El código anterior empleado es bastante complicado de leer
#El equivalente a todo ese código anterior es el empleo
#de la tabla de pivotaje (df.pivot_table())
#El primer parámetro es la columna a la que aplicamos las medidas estadísticas
#index="" indica la agrupación en las filas
#columns="" indica la agrupación en las columnas
pt1 = titanic.pivot_table("survived", index="sex", columns="pclass")
print(pt1)
print("")


#Función pd.cut() para agrupar datos
#Se selecciona la variable del DF a agrupar (columna)
#El parámetro "bins=list" dqa lugar a los intervalos
#Para incluir el extremo izquierdo del primer intervalo se usa "include_lowest=True"
#Se establece la precisión de la variable con "precision=1"
#"right=False" hace que los extremos izdos estén cerrados y los dchos abiertos
age = pd.cut(titanic["age"], bins=[0,18,25,35,50,65,100],
	include_lowest=True, precision=1,
	right=False)
print(age)
print("")


#Empleamos la variable age para agrupar con un pivot_table()
average_suv_spa = titanic.pivot_table("survived", index=["sex",age], columns="class")
print(average_suv_spa)
print("")


#La función pd.qcut() permite establecer intervalos de clase
#según los cuantiles
#"fare" son las tasas
#Se indica primero la variable (columna) de trabajo
#Luego se indica el nº de cuantiles para establecer la división
#Trae también parámetros
fare = pd.qcut(titanic["fare"], 4, labels=["Q1","Q2","Q3","Q4"])
print(fare)
print("")


#pivot table con más variables y agrupaciones
pt_extra = titanic.pivot_table("survived", index=["sex",age], columns=[fare,"pclass"])
print(pt_extra)
print("")


#EJEMPLO COMPLETO

#Se agrega un diccionario a aggfunc para relacionar los datos que queremos a una función determinada
X1 = titanic.pivot_table(index = "sex", columns="class", 
	aggfunc = {"survived":sum, "fare":"mean"})
print(X1)
print("")


#Se calculan los marginales por filas y columnas
X2 = titanic.pivot_table('survived', index="sex", columns="class", 
	margins=True, margins_name="Total")
print(X2)
print("")
