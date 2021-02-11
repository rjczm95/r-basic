

### DISTRIBUCIÓN BINOMIAL ###


#Sea nuestra Binomial la siguiente: X = B(n = 30, p = 0.6)


from scipy.stats import binom 
import matplotlib.pyplot as plt
import numpy as np

#Defino el nº de lanzamientos y la probabilidad
n = 7
p = 0.4

#Con binom.stats se pueden obtener varios
# estadísticos en una sola línea de código
#Sacamos los estadísticos siguientes:
#  - mean()
#  - var()
#  - skew(). Sesgo
#  - kurt(). Curtosis
mean, var, skew, kurt = binom.stats(n, p, 
	moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)



##FUNCIÓN DE PROBABILIDAD PARA UNA DISTR. BINOMIAL
#Los valores de x s epueden definir con los cuantiles
x = np.arange(binom.ppf(0.001,n,p), binom.ppf(0.999,n,p))
#O si directamente conocemos los que pueden ser, de este modo
x = np.arange(0, n+1)

fig, ax = plt.subplots(1,1)
ax.plot(x, binom.pmf(x, n, p), 'bo', ms = 8, 
	label = "Función de probabilidad de B(7, 0.4)")
#incorporo lineas veticales desde eje x hasta el valor y
ax.vlines(x, 0, binom.pmf(x,n,p), colors = 'b', 
	lw = 4, alpha = 0.5)

#Añadimos una curva teórica al gráfico de la distr. prob.
#para la binomial estudiada
rv = binom(n,p)
#Pongo en "y" los valores de rv según probability mass function
ax.vlines(x,0, rv.pmf(x), colors = 'k', linestyles='--', 
	lw = 2, color="red", 
	label = "Distribución teórica de la distr. prob.")

ax.legend(loc = 'upper right', frameon = False,
	fontsize=8)

plt.show()
plt.close()


##FUNCIÓN DE DISTRIBUCIÓN ACUMULADA PARA UNA DISTR. BINOMIAL

fig, ax = plt.subplots(1,1)
ax.plot(x, binom.cdf(x, n, p), 'bo', ms = 8, 
	label = "Función de distribución de B(7, 0.4)")
plt.title("Función de distribución de B(7, 0.4)")
#incorporo lineas veticales desde eje x hasta el valor y
ax.vlines(x, 0, binom.cdf(x,n,p), colors = 'b', 
	lw = 4, alpha = 0.5)

plt.show()
plt.close()


#GENERAR VALORES ALEATORIOS EN DISTR. BINOMIAL
#Histograma de datos generados aleatoriamente según una
#distribución binomial "n" y "p"
fix, ax = plt.subplots(1,1)
r = binom.rvs(n, p, size = 10000)
ax.hist(r, bins = n)
plt.show()
plt.close()



