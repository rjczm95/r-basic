
### DISTRIBUCIÓN HIPERGEOMÉTRICA ###

#Supongamos que tenemos 20 animales, de los cuales 7 son 
#perros. Queremos medir la probabilidad de encontrar un 
#número determinado de perros si elegimos $k=12$ 
#animales al azar.

from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

#M es el nº total, n solo los que nos interesan y N es el 2º tipo presente
[M, n, N] = [20, 7, 6]

#generamos una hipergeométrica con la definición de arriba
rv = hypergeom(M, n, N)


#Determino la "x" y la "y"
x = np.arange(0, n+1)
y = rv.pmf(x)

#Estadísticos para la distribución hipergeométrica
mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig = plt.figure()
ax = fig.add_subplot(111) #para que sea grande

ax.plot(x, y, 'bo' )

#linea verticales
ax.vlines(x,0,y, lw = 2, alpha = 0.5)

ax.set_xlabel("Número de perros entre los 12 elegidos al azar")

ax.set_ylabel("Distribución de probabilidad de H(13,7,12)")

plt.show()
plt.close()