

## DISTRIBUCIÓN BINOMIAL NEGATIVA ###

#Una compañía petrolera tiene una probabilidad p = 0,20 
#de encontrar petróleo al perforar un pozo. ¿Cuál es la 
#probabilidad de que la empresa perfore x=20 pozos de 
#encontrar petróleo r=3 veces?


import numpy as np
from scipy.stats import nbinom
import matplotlib.pyplot as plt

#Defino los parámetros
n = 20 #nº de intentos
r = 3 #nº éxitos
p = 0.2 #probabilidad


#Estadístivos de la distr. de Binomila negativa
mean, var, skew, kurt = nbinom.stats(r, p,
	moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)


fig, ax = plt.subplots(1,1)

#genero valores de x
x = np.arange(r, n+1)

ax.plot(x, nbinom.pmf(x, r, p), 'bo', ms = 8, 
	label = 'Binomial negativa')

#lineas verticales
ax.vlines(x,0, nbinom.pmf(x,r,p), colors = 'b', 
	lw = 4, alpha = 0.5)

ax.legend(loc = "best", frameon = False)

plt.show()
plt.close()

