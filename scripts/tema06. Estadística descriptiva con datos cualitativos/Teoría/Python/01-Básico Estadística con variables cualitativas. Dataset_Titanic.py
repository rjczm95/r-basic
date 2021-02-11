
## ANALISIS ESTADÍSTICO DE VARIABLES CUALITATIVAS

#Dataset titanic
#Recoge datos de la tragedia del titanic
#Para más información visita kaggle

#Este dataset se carga en Python utilizando un paquete
#que se llama "Seaborn" cuyo uso común es sns

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


#Cargo el dataset titanic en el parámetro titanic
titanic = sns.load_dataset("titanic")
print(titanic.shape) #nº filas (personas) y columnas (observaciones)
print(" ")
print(titanic.head())
print(" ")

#La columna survived es claramento un factor de 2 niveles (0 == no & 1 == si)
#Para convertirla a factor se emplea la instrucción de pandas
#pd.Categorical("varaible_cualitativa")
titanic["survived"] = pd.Categorical (titanic["survived"])
titanic["pclass"] = pd.Categorical (titanic["pclass"])
titanic["sex"] = pd.Categorical (titanic["sex"])
titanic["sibsp"] = pd.Categorical (titanic["sibsp"])
titanic["parch"] = pd.Categorical (titanic["parch"])
titanic["embarked"] = pd.Categorical (titanic["embarked"])
titanic["class"] = pd.Categorical (titanic["class"])
titanic["who"] = pd.Categorical (titanic["who"])
titanic["adult_male"] = pd.Categorical (titanic["adult_male"])
titanic["alive"] = pd.Categorical (titanic["alive"])
titanic["alone"] = pd.Categorical (titanic["alone"])
titanic["deck"] = pd.Categorical (titanic["deck"])



""" TABLAS DE CONTINGENCIA DE UNA VARIABLE """

## TABLAS DE FRECUECNIAS ABSOLUTAS

#Para crear una tabla de frecuencias se emplea pandas
#La función se llama pd.crosstab
tab = pd.crosstab(index = titanic["survived"],
	columns ="pasajeros")
print(tab) #Tabla de contingencia para nº supervivientes vs no supervivientes
print(" ")
print(type(tab)) #es un Dat Frame
print(" ")
tab.plot(kind="bar")
plt.show()
print(" ")

#Tabla de contingencia para las clases de los pasajeros
print(pd.crosstab(index=titanic["pclass"],
	columns="pasajeros"))
print(" ")


#Tabla de contingencia para el género de los pasajeros
print(pd.crosstab(index=titanic["sex"],
	columns="pasajeros"))
print(" ")

#"deck" se refiere a la división de cubiertas del titanic
#Tabla de contingencia para las cubiertas en las que se alojaban los pasajeros
tab_c = pd.crosstab(index = titanic['deck'],
           columns = "count")
#No aparecen contados los NaN (not a number) para la tabla de frecuencias
print(tab_c)
print(" ")

#Para conocer la cantidad de cabinas conocidas en las que se alojaban personas
#se aplica df.sum()
print(tab_c.sum())
print(" ")
print(tab_c.shape) #conocer las dimensiones de la tabla
print(" ")


#Para extraer un dato de la tabla de contigencia
#se utiliza la instrucciín iloc[], index location
print(tab_c.iloc[2:5])
print(" ")


##TABLA DE FRECUENCIAS RELATIVAS

#Se emplea el sum() calculado con anterioridad
print(tab_c/tab_c.sum()) #FREC. REL. ABS.
print(" ")

print (tab/tab.sum())
print(" ")

type_class = pd.crosstab(index=titanic["pclass"],
	columns="pasajeros")
print(type_class/type_class.sum())
print(" ")

gender =pd.crosstab(index=titanic["sex"],
	columns="pasajeros")
print(gender/gender.sum())
print(" ")



""" TABLAS DE CONTINGENCIA DE DOS VARIABLE """

##FRECUENCIAS ABSOLUTAS

#También se emplea la función pd.crosstab()
#supervivientes por generos
survived_sex = pd.crosstab(index=titanic["survived"],
	columns=titanic["sex"])
#Para cambiar el nombre de las filas se emplea:
survived_sex.index = ["died","survived"]

print(survived_sex)
print(" ")

#supervivientes por clases de pasajeros
survived_class = pd.crosstab(index=titanic["survived"],
							 columns=titanic["pclass"])
survived_class.index = ["died","survived"]
survived_class.columns = ["first","second","third"]
print(survived_class)
print(" ")

#El parámetro "margins=TRUE" permite discernir el total de cada variable
#Hemos de añadir una fila y una columna
survived_class = pd.crosstab(index = titanic['survived'], 
                            columns = titanic['pclass'],
                            margins = True)

survived_class.index = ["murio", "sobrevivio", "total_clase"]
survived_class.columns = ["primera", "segunda", "tercera", "total_superv"]
print(survived_class)
print(" ")


## FRECUENCIAS RELATIVAS GLOBALES

#Se requiere calcular la proporción de conteos con respecto
#al total de la tabla

#Es mejor hacerlo en dos fases:
# 1. Calcula la tabla de las frecuencias cruzadas
# 2. Dividir por el total de inidviduos representados

#Teniendo ya calculado "survived_class" sería:
#Se uriliza loc para acceder a los nombres. iloc solo sirve para la posición (0,1,2...)
frec_glob = survived_class/survived_class.loc["total_clase","total_superv"]
#se obtienen las FREC. REL. GLOBALES 
print(frec_glob)
print(" ")

## FRECUENCIAS RELATIVAS MARGINALES

#Por columnas
#Se divide por la suma de las columnas
column_survived = survived_class/survived_class.loc["total_clase"]

print(" ")


#Por filas
#Se divide por la suma de las filas
#!!CUIDADO!! Se hace de modo diferente
#Se puede emplear la transpuesta de la tabla global
#emplear para ello df.T
row_class = survived_class.T/survived_class["total_superv"]
print(row_class)
print(" ")

#No obstante, es más sencillo usar la función df.div()
#permite dividir por filas
#El parámetro "axis = 0" es fundamental
row_class2 = survived_class.div(survived_class["total_superv"], 
	axis = 0)
print(row_class2)
print(" ")

#También se puede emplear esta instrucción para la 
#relativa marginal por columnas
column_survived2 = survived_class.div(survived_class.loc["total_clase"],
	axis=1)
print(column_survived2)
print(" ")


## TABLAS MULTIDIMENSIONALES

#Habría que indicar a la función pd.crosstab() que va a
#haber más de dos categorías/variables

#Las tablas multidimensionale sson dificiles de leer

#En el index se indica una categorías y en las columnas
#se indica un array o lista con las otras dos categorías
#Para las marginales poner el parámetro "margins = True"
surv_sex_class = pd.crosstab(index = titanic["survived"],
	columns = [titanic["sex"],titanic["pclass"]],
	margins=True)
print(surv_sex_class)
print(" ")

#para quedarme unicamente con la subtabla de las mujeres
#se hace lo siguiente
print(surv_sex_class["female"])
print(" ")

#para las mujeres de primera clase se haría:
print(surv_sex_class["female"][1])
print(" ")


#Para obtener la FREC. RELAT. GLOBAL
FRG =round(surv_sex_class/surv_sex_class["All"]["All"],3)
print(FRG)
print(" ")

#Para obtener la FREC. RELAT. MARGINAL POR COLUMNAS
FRM_column = round(surv_sex_class/surv_sex_class.loc["All"],3)
print(FRM_column)
print(" ")

#Para obtener la FREC. RELAT. MARGINAL POR FILAS
FRM_filas = round(surv_sex_class.div(surv_sex_class["All"],
	axis=0),3)
print(FRM_filas)






