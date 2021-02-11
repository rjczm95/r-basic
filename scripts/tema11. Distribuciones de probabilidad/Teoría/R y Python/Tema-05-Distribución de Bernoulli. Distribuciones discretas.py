
### DISTRIBUCIÓN DE BERNOULLI ###


# **Función de probabilidad**

# Sea X = Be(p = 0.7),, la distribución que modela la 
# probabilidad de obtener una cara usando 
# una moneda trucada. 

#Para emplear Bernoulli necesitamos el paquete scipy
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

#probabilidad de éxito
p = 0.7

#Con bernoulli.stats se pueden obtener varios
# estadísticos en una sola línea de código
#Sacamos los estadísticos siguientes:
#  - mean()
#  - var()
#  - skew(). Sesgo
#  - kurt(). Curtosis
mean, var, skew, kurt = bernoulli.stats(p, 
	moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew) #Sesgo negativo
print("Curtosis %f"%kurt) #Para ver sis es pronunciada la curva

#Representamos la distribución de Bernoulli generada
fig, ax = plt.subplots(1,1)
x = bernoulli.rvs(p, size = 1000)
ax.hist(x)
plt.show()
plt.close()
