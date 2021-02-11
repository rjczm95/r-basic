
### FUNCIÓN DE DENSIDAD Y PROBABILIDAD EN PYTHON ###

# Dado un conjunto de datos, discretos o continuo, se asume:
#  - Provienen de una población más grande (es una muestra de la misma)
#  - Siguen una distribución descrita por una serie de parámetros

# La función de densidad o probabilidad de la variable
# aleatoria subyacente es una forma ideal de finalizar
# un análisis descriptivo

# Vamos a usar PANDAS para crear capas por encima del
# gráfico utilizando una de estas funciones:
#  · plot.kde (kernel density estimate)
#  · plot.pdf (probability density function)

# Para estimar la densidad con plot.kde, Python emplea
# la librería SciPy que recoge la función:
#   - gaussian_kde (gkde)

# La distribución generada es una aproximación más real

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


#Vamos a generar dos distribuciones normales de 
#distinta media (mu) y distinta sigma (sigma)
mu = 10, 20
sigma = 5, 2


np.random.seed(2019)
#Generamos un DataFrame con 2 columnas, una para 
#cada distribución
dist = pd.DataFrame(np.random.normal(loc=mu, 
	scale=sigma, size = (1000,2)),columns=["x1","x2"])

#Sacamos los estadísticos de resumen del DF creado
#para ello empleamos la función aggregate()
print(dist.aggregate(["min","max","mean","std"]).round(decimals=2))
print("")


#Creamos la figura (fig) y los ejes o gráficas (subplots) de la misma
fig, ax = plt.subplots()

#Creamos la función de densidad para cada columna del DF
dist.plot.kde(ax=ax, legend=False, 
	title="Histograma de dos distribuciones normales")

#Creamos el histograma para cada columna del DF
# density=True permite tener las frecuencias relativas
#en lugar de las absolutas
dist.plot.hist(density=True, ax=ax)

ax.set_ylabel("Probabilidad")
ax.set_xlabel("Datos de las variables")
ax.grid(axis="y", alpha=0.5)
#Poner color de fondo
ax.set_facecolor("#d5d5d5")

plt.show()
plt.close()


## Vamos a emplear de la librería "scipy" el módulo "state"
from scipy import stats

# En "statss" tenemos la fórmula analítica de la 
# distribución normal

#Determinamos la distribución teórica con stats.norm()
#Distr. Norm. Teórica [N(0,1) - exp((-x**2)/2)/sqrt(2*pi)]
dist2 = stats.norm() 

#A partir de la distribución generada (dist2) se puede
#construir un muestreo de datos para aproximar la
#distribución normal a esos datos (sample)
#Para obtener los datos se emplea rvs() sobre stats.norm()
sample = dist2.rvs(size=1000) #Muestra de datos de la distribución
print(sample[:4])

#Para evaluar la función analítica y la estimada,
#necesitamos el array de los cuantiles (eje x)
# "x" es la generación de cuantiles desde 
# el 0.01 hasta el 0.99 (función stats.norm.ppf())
#Calculamos cuantos datos de la distribución son
#menores o iguales a cada uno de los percentiles empleados
x = np.linspace(start=stats.norm.ppf(0.01), #stats.norm.ppf(0.01) es la inversa del percentil de la normal del 1%
	stop=stats.norm.ppf(0.99), num=250)

# La distribución normal estumida partiendo de una
# muestra de datos (sample) se estima con:
#  - stats.gaussian_kde(dataset=sample)
gkde = stats.gaussian_kde(dataset=sample)


fig2, ax2 = plt.subplots()

#TEÓRICA
#Empleo para las "y" dist2 generado con stats.norm()
ax2.plot(x, dist2.pdf(x), linestyle="solid", color="red",
	lw=3, alpha=0.8,label="Distribución normal teórica")

#ESTIMADA
#Empleo para las "y" gkde generado con stats.gaussian_kde()
ax2.plot(x, gkde.evaluate(x),linestyle="dashed",
	color="green",lw=2,
	label="PDF estimada con KDE")


#frameon=False quita el marco
ax2.legend(loc="best", frameon=False)
ax2.set_title("Normal analítica vs estimada")
ax2.set_ylabel("Probabilidad")
#Lenguaje LaTeX
ax2.text(-2,0.35,r"$f(x) = \frac{e{^2/2}}{\sqrt{2\pi}}$",
	fontsize=14)
plt.show()
plt.close()





