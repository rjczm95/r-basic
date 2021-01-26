
# DATA FRAMES EN PYTHON

#Se utiliza la librería pandas para trabajar con data frames
import pandas as pd

#read_table() y read_csv son las funciones más usadas en pandas
#para abrir ficheros
#Los datos de bodyfat.txt vienen separados por espacios en blanco
#Para que se cree bien el data frame se pone delimiter=" "
df = pd.read_csv("../../../../data/bodyfat.txt", 
	delimiter=" ", decimal=".",
	encoding="utf-8") #Importante cuando da problemas y hace referencia a que está cargado según estándar internacional utf-8

#DF.head() devuelve los primero 5 elementos de la tabla
print(df.head(3))
print(df.tail(3)) #Para las ultimas filas

#Si se quiere acceder únicamente a una posición del DF
#es mejor utilizar la función DF.loc()
#funciona por el identificador del index
print(df.loc[[1]]) #Da fila con identificador 1


#Se emplea la función DF.iloc()
#cuando se quiere buscar en función de la localización
#del index ya que iloc es index location
#Los DF empezarán por 0
print(df.iloc[[0]]) #Este es el identificador 1
print(df.iloc[[5]])

#Para filtrar filas del DF se emplea la siguiente sintaxis
print(df[12:14])
print(df[10:30:5]) #Obtenemos las filas de la 10 a la 30 con saltos de 5 en 5

#Se extrae la variable Density (columna) y genera un vector columna
df.Density

#Obtener funciones para trabajar con la variable del DF
df.Density.sum()
df.Density.mean()
df.Density.median()

#la función describe() da el resumen estadístico del DF
df.Density.describe()
df.describe()
#Transponer la tabla del describe() para ver mejor la tabla
df.describe().transpose()

#shape() da un vector que es (nº filas, nº columnas)
df.shape

#Cargar un csv desde la url presente en la web
df2 = pd.read_csv("http://winterolympicsmedals.com/medals.csv")
df2.shape
df2.head(3)
#Se podría especificar el delimitador para ganar seguridad
pd.read_table("http://winterolympicsmedals.com/medals.csv", 
	delimiter=",")

