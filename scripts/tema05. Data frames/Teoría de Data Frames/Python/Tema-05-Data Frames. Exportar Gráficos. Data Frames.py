## PÁRAMETROS DE GROUPBY() PARA DATA FRAME EN PYTHON

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#Vamos a crear un DF a mano e importarlo con matplotlib
#en forma de archivo png, representado gráficos 

#Distribución de años entre 1900 hasta 2020
years = [year for year in range(1900, 2020)]
#Muertes para cada uno de los años de la lista years
deads = [(y + np.random.uniform(0,100) - 1850) for y in years]

#Construyo DF con las listas years y deads, asignándoles una clave
df = pd.DataFrame({
    "year": years,
    "deads": deads})

print(df.head())


#en el eje de las x se pinta la columna year
#en el eje de las y se pinta la columna deads
#el tipo de gráfico es scatter (gráfico de dispersión de ptos)
df.plot(kind = "scatter", x="year", y = "deads", 
	figsize = (10, 8))
plt.show()
plt.close()

#Gráficos de líneas
my_plot = df.plot(x="year", y = "deads", 
	figsize = (10, 8))
plt.show()
plt.close()

#La instrucción get_figure() permite generar la figura entera
#del plot creado
my_fig = my_plot.get_figure()

#savefig("path") permite exportar el gráfico
my_fig.savefig("Tema-05-Plot Data Frame.png")
