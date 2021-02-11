

## DISTRIBUCIÓN DE POISSON ###

#Supongamos que X modela el número de errores por página 
#que tiene un valor esperado lambda = 5 de errores.


import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt


mu = 5 #lambda


#Estadístivos de la distr. de Poisson
mean, var, skew, kurt = poisson.stats(mu, 
	moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)


fig, ax = plt.subplots(1,1)

#genero valores de x
x = np.arange(0, 14)

ax.plot(x, poisson.pmf(x, mu), 'bo', ms = 8, 
	label = 'Poisson(5)')

#lineas verticales
ax.vlines(x,0, poisson.pmf(x,mu), colors = 'b', 
	lw = 4, alpha = 0.5)

ax.legend(loc = "best", frameon = False)

plt.show()
plt.close()




