
## EJERCICIOS

# Vamos a hacer un repaso de todo lo aprendido a lo largo de esta sección

# 1. Dad la instrucción que defina la tabla de frecuencias absolutas de un 
# vector llamado "alumnos".

#import pandas as pd 
#pd.crosstab(index= alumnos, columns="count")


# 2. Con una sola instrucción, definid la tabla de frecuencias relativas de 
# un vector llamado "edades".

#import pandas as pd 
#(pd.crosstab(index= edades, columns="count"))/len(edades)



# 3. Con una sola instrucción, definid la tabla bidimensional conjunta de 
# frecuencias absolutas de dos vectores llamados "altura" y "peso", de 
# forma que las filas correspondan a "altura" y las columnas a "peso".

#import pandas as pd 
#pd.crosstab(index= altura, columns=peso)


# 4. Con una sola instrucción, definid la tabla bidimensional conjunta de 
# frecuencias relativas calculadas dentro del total, de dos vectores 
# llamados "edad" y "altura", de forma que las filas correspondan 
# a "altura" y las columnas a "edad".

#import pandas as pd 
#(pd.crosstab(index= altura, columns=edad, margins = True))/len(altura)


# 5. Con una sola instrucción, dibujad un diagrama de barras básico de 
# un vector llamado "edad".

#import pandas as pd 
#pd.crosstab(index= edad, columns="count").plot(kind="bar", title="Diagrama de Barras")


# 6. Con una sola instrucción, dibujad un diagrama circular básico de 
# un vector llamado "alumnos".

#import pandas as pd 
#pd.crosstab(index= alumnos, columns="count").plot(kind="pie", title="Diagrama de Circular")


# 7. La tabla "DNase" es uno de los data frames que tiene predefinidos R. 
# Dad la instrucción que dibuje un diagrama de barras básico de la 
# variable "density" de este mismo data frame
# url :  https://github.com/jamovi/r-datasets/blob/master/data/DNase.csv

import pandas as pd
import matplotlib.pyplot as plt

DNase = pd.read_csv("https://raw.githubusercontent.com/jamovi/r-datasets/master/data/DNase.csv")
print(DNase.head(3))
print(" ")
print(DNase.shape)
print(" ")
print(DNase["density"].dtypes)
print(pd.unique(DNase["density"]))

DNase["density"] = pd.Categorical(DNase["density"])

DNase_FG = pd.crosstab(index=DNase["density"], columns="count")

plt.bar(DNase_FG.index,DNase_FG["count"])
plt.xlabel("density")
plt.ylabel("count")
plt.xlim(-1,3)
plt.show()

