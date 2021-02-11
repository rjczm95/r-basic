
""" EJERCICIOS DE GRÁFICOS CON PYTHON"""

import matplotlib.pyplot as plt
import numpy as np


##EJERCICIO 1
#A partir del siguiente código, intenta obtener el gráfico 
#del dibujo llamado ejercicio 1 en el enunciado.

#n = 256
#X = np.linspace(-np.pi, np.pi, n, endpoint=True)
#Y = np.sin(2 * X) 
#plt.plot(X, Y + 1, color='blue', alpha=1.00)
#plt.plot(X, Y - 1, color='blue', alpha=1.00)

#Pista: investiga el parámetro fill_between de matplotlib.

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X) 

plt.figure(1,figsize=(9,8))
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.xlim(-np.pi, np.pi)
plt.ylim(-2.5, 2.5)

#Creo lineas horizontales para los dos plots
plus_one = 1
less_one = -1

#Relleno el plot que le suma 1 a Y. Pongo color azul
plt.fill_between(X, Y+1, plus_one, color="lightskyblue")

#Relleno el plot que le resta 1 a Y. Pongo condición para poner dos colores.
plt.fill_between(X,Y-1,less_one, where=(Y-1>=-1),
	color="lightskyblue")
plt.fill_between(X,Y-1,less_one, where=(Y-1<=-1),
	color="lightsalmon")

#Poner el recuadro en el eje de la figura
ax =plt.gca()
ax.spines['right'].set_color('black')
ax.spines['top'].set_color('black')

#Quito los ticks
plt.xticks([])
plt.yticks([])

plt.show()
plt.close()


##EJERCICIO 2
#A partir del siguiente código, intenta obtener el gráfico del 
#dibujo llamado ejercicio 2 en el enunciado.

#n = 1024
#X = np.random.normal(0,1,n)
#Y = np.random.normal(0,1,n) 
#plt.scatter(X,Y)

#Pista: el color viene dado por el ángulo que forman 
#x e y con la horizontal

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n) 

#Establezco la relación que da el color
#Es el ángulo que establecen "x" e "y" con la horizontal
#Para definir dicho ángulo calculo el arco tangente de "x" e "y"
#El primer parámetro dado es el del eje x y el segundo el eje y
angle = np.arctan2(Y,X) 

#Defino el color en función de angle
plt.axes([0.015, 0.015, 0.95, 0.95])
plt.scatter(X,Y, s=50, c=angle, alpha= 0.75)
plt.axes

#Define los límites de los ejes y quito los ticks
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks([])
plt.yticks([])

plt.show()
plt.close()



##EJERCICIO 3
#A partir del siguiente código, intenta obtener el gráfico 
#del dibujo llamado ejercicio 3 en el enunciado.

#Pista: cuidado con la alineación del texto en el centro 
#de las barras.

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) 

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white') 

for x, y in zip(X, Y1):     
        plt.text(x, y + 0.05, '%.2f' % y, 
        	ha='center', va='bottom') 

for x, y in zip(X, Y2):     
        plt.text(x, -y - 0.05, '%.2f' % y, 
        	ha='center', va='top') 

#Define los límites de los ejes y quito los ticks

plt.xticks([])
plt.yticks([])
plt.xlim(-1, n)
plt.ylim(-1.25, +1.25)

plt.show()
plt.close()



## EJERCICIO 4
#A partir del siguiente código, intenta obtener el gráfico 
#del dibujo llamado ejercicio 4 en el enunciado.

#Z = np.random.uniform(0, 1, 20)

#Pista: tendrás que modificar la Z.

#Hago que Z sea un array de 20 valores de 1
n = 20
Z = np.ones(n)
#Transformo el último valor de Z en 2
Z[-1] *= 2

#Ajusto la visualización del gráfico
plt.axes([0.015, 0.015, 0.95, 0.95])

#Gráfico circular con plt.pie()
#Extraigo cada quesito de información con explode un0.05
plt.pie(Z, 
	explode =[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1], 
	colors = ['%f' % (i/float(n)) for i in range(n)])

#Hacer que las escalas del eje x e y sean iguales
plt.axis('equal')

#Hago desaparecer los marcadores
plt.xticks([])
plt.yticks([])

plt.show()
plt.close()

#OTRO METODO
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.figure(1,figsize = (15,15))

#Z = np.random.uniform(0, 1, 20)

X = np.arange(0,20) *0 +1
X[len(X)-1]= X[len(X)-1]*2

exp = np.arange(20) *0+0.03
exp [len(exp )-1]= exp [len(exp)-1]*4

colors = plt.cm.gray(np.linspace(0.2, 0.8, 20))
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

plt.pie(X, explode=exp, )

plt.show()
plt.close()
