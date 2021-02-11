# V. A. continua

### FUNCIÓN UNIFORME ###


# Supongamos que X∼U([0,1]) entonces podemos 
# estudiar sus parámetros.


from scipy.stats import uniform
import matplotlib.pyplot as plt 
import numpy as np

#Definimos el primer punto (a) y la amplitud del intervalo (b)
a = 0
b = 1

#sintaxis de python
loc = a
scale = b-a

#Gráfica
fig, ax = plt.subplots(1,1)

#random variable de la uniforme para los datos predefinidos
rv = uniform(loc = loc, scale = scale)

#Sacamos los estadísticos
mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

#Determinamos los valores del eje "x"
x = np.linspace(-0.1, 1.1, 120)

#Gráfico de función de densidad (es continua)
ax.plot(x, rv.pdf(x), 'k-', lw = 2, label = "U(0,1)")
ax.legend(loc = 'best', frameon = False)
plt.show()
plt.close()


fig, ax = plt.subplots(1,1)
#Genero una serie de nºs aleatorios
r = rv.rvs(size = 100000)
#Represento el histogramas de los datos aleatorios
ax.hist(r, density = True, 
	histtype = "stepfilled", alpha = 0.25)
plt.show()
plt.close()

