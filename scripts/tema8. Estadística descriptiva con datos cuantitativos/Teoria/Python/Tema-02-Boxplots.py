
## DIAGRAMA DE CAJA Y BIGOTES (BOXPLOT)

import numpy as np
import matplotlib.pyplot as plt

# Para establecer una semilla y hacer que siempre nos
# salgan los mismos datos aleatorios se emplea:
# np.random.seed()
np.random.seed(19880519)

#Vamos a crear 4 distribuciones
#rand genera nºs aleatorios entre 0 y 1
#ones solo genera 1
dist1 = 100*np.random.rand(50) #datos entre 0 y 100
dist2 = 50*np.ones(25) #para que la mediana quede mas o menos centrada
dist3 = 100+100*np.random.rand(10) #colas de dispersión (por arriba)
dist4 = -100*np.random.rand(10) #colas de dispersión (por abajo)

#concateno las distribuciones generadas
data = np.concatenate((dist1, dist2, dist3, dist4))

#Boxplot básico -> función boxplot()
fig1, ax1 = plt.subplots()
ax1.set_title("Boxplot básico")
ax1.boxplot(data)
plt.show()
plt.close()


#Boxplot con muescas
fig2, ax2 = plt.subplots()
ax2.set_title("Boxplot con muescas")
ax2.boxplot(data, notch = True)
plt.show()
plt.close()


#Boxplot con outliers personalizados
green_diamond = dict(markerfacecolor="g", marker="D") #diamantes
fig3, ax3 = plt.subplots()
ax3.set_title("Boxplot con outliers personalizados")
ax3.boxplot(data, flierprops=green_diamond)
plt.show()
plt.close()

#Boxplot sin outliers
fig4, ax4 = plt.subplots()
ax4.set_title("Boxplot sin outliers")
ax4.boxplot(data, showfliers=False)
plt.show()
plt.close()

#Boxplot personalizado en horizontal
red_square = dict(markerfacecolor="r", marker="s") #cuadrado
fig5, ax5 = plt.subplots()
ax5.set_title("Boxplot personalizado y en horizontal")
#vert =False para que sea horizontal
#Para cambiar el tamaño de los bigotes se usa "whis ="
ax5.boxplot(data, vert=False, flierprops=red_square, whis=0.75)
plt.show()
plt.close()


"""VARIOS BOXPLOT EN LA MISMA GRÁFICA"""

#CREO UN NUEVO DATA
dist1 = 100*np.random.rand(50)
dist2 = 40*np.ones(25)
dist3 = 100+100*np.random.rand(10)
dist4 = -100*np.random.rand(10)
data2 = np.concatenate((dist1, dist2, dist3, dist4))


data.shape = (-1,1) #aplana el vector en filas
data2.shape = (-1,1) #aplana el vector en filas

#En la tercera variable se toman los datos de 
#data2 de 2 en 2 para la porimera columna
#flatten aplana el vector en filas
fulldata = [data.flatten(), data2.flatten(), data2[::2,0].flatten()]

fig7, ax7 = plt.subplots()
ax7.set_title("Múltiples muestras de diferente naturaleza")
ax7.boxplot(fulldata)
plt.show()
plt.close()







