# V. A. continua

### FUNCIÓN EXPONENCIAL ###


from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)

#Definimos la lambda como 3
lam = 3
#inversa de la lambda
rv = expon(scale = 1/lam)

#Etadísticos
mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

#definimos eje x con 1000 valores
x = np.linspace(0, 3, 1000)
#gráfica de la función de densidad de una exponencial
ax.plot(x, rv.pdf(x), 'r-', lw = 4, alpha = 0.6, 
	label = "Exp(10)")

#creamos datos aleatorios y los representamos en un histograma
r = rv.rvs(size = 100000)
ax.hist(r, bins=25, density = True, histtype = 'stepfilled', 
	alpha = 0.2)

ax.legend(loc = "best", frameon= False)
plt.show()
plt.close()