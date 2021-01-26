
## EJERCICIOS DATA FRAME PYTHON


#Carga el CSV de la carpeta de datos del tema 
#llamado run.csv y responde a las siguientes preguntas.
import pandas as pd
df_run = pd.read_csv("../../../../data/run.csv")
print(df_run.head())
print(" ")

"""Preguntas de esta tarea"""

# 1.Indica cuantos estudiantes formaron parte del 
# estudio de deporte

print(df_run.shape[0])
print(len(df_run.index))
#Este estudio consta de 92 estudiantes
print(" ")

# 2.Indica cuantos individuos son hombres y cuantos 
# son mujeres

print(df_run.columns)
print(pd.unique(df_run["genero"]))

#Creo y data frame solo con los hombres
hombres=df_run[df_run["genero"]=="H"]
print(len(hombres.index))
#Hay 57 hombres.

#Creo y data frame solo con las mujeres
mujeres=df_run[df_run["genero"]=="M"]
print(len(mujeres.index))
#Hay 35 mujeres.

print(" ")

# 3.Calcula el porcentaje medio de variación del pulso 
# por minuto entre antes y después de hacer ejercicio 
# y compara el valor de los que hacen ejercicio 
# habitualmente y los que no. ¿Observas mucha diferencia?
# %variación = (pulso_despues - pulso _antes)/pulso_antes

#Añado nueva columna con el porcentaje de variación pedido
df_run ["Variacion_pulso"] = abs(((df_run["pulso.despues"]-df_run["pulso.antes"])/df_run["pulso.antes"])*100)
print(df_run.columns)

#Para comparar la variación del pulso hago la media de dicha variación para los que hacen y no hacen deporte
print(df_run.groupby("hace.deporte").aggregate({"Variacion_pulso":"mean"}))
#Se observa una variación del pulso mayor para los que hacen deporte
print(" ")


# 4.Calcula el porcentaje medio de variación del pulso 
# por minuto entre antes y después de hacer ejercicio  
# para los estudiantes que hacen ejercicio habitualmente 
# y compara el valor de los hombres con el de las mujeres. 
# ¿Observas mucha diferencia?

#Compruebo los valores posibles en la columna de hace deporte
print(pd.unique(df_run["hace.deporte"]))

#Primero filtro para que aparezca solo los estudiantes que hacen deporte
#Agrupo en base al genero masculino y femenino
#estipulo la media de la variación
print(df_run[df_run["hace.deporte"]=="si"].groupby("genero").aggregate({"Variacion_pulso":"mean"}))
#Se observa que la variación del pulso es mayor en las mujeres que en los hombres

print(" ")


# 5.Calcula el porcentaje medio de variación del pulso por 
# minuto entre antes y después de hacer ejercicio para 
# los estudiantes que no hacen ejercicio habitualmente y 
# compara el valor de los fumadores con los no fumadores. 
# ¿Observas mucha diferencia?


#Primero filtro para que aparezca solo los estudiantes que no hacen deporte
#Agrupo en base a si lso estudiantes fuman o no
#estipulo la media de la variación
print(df_run[df_run["hace.deporte"]=="no"].groupby("fuma").aggregate({"Variacion_pulso":"mean"}))
#No hay mucha diferencia, aunque la variación es ligeramente mayor en los fumadores

print(" ")


# 6. Calcula el porcentaje medio de variación del pulso 
# por minuto entre antes y después de hacer ejercicio de 
# todos los estudiantes según el tipo de actividad física 
# que realizan. ¿Observas alguna diferencia?

#Agrupo según el tipo de actividad
print(df_run.groupby("tipo.actividad").aggregate({"Variacion_pulso":"mean"}))
#Se observa que para actividades moderadas la variación es elevada

