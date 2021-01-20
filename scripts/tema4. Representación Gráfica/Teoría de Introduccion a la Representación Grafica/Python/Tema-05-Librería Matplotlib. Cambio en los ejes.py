
## LIBRERÍA MATPLOTLIB.PYPLOT

# Cambio en los ejes // Ejemplo de gráfico detallado

import matplotlib.pyplot as plt
import numpy as np 

#endpoint=True indica que tomamos el último punto dado
x=np.linspace(-np.pi,np.pi,256,endpoint=True)

#Creo dos funciones con la coma
s, c= np.sin(x), np.cos(x)


plt.figure(1,figsize=(10,8))
#Dibujar plots
plt.plot(x,s,color="blue",linewidth=1.2,linestyle="-",label="Seno")
plt.plot(x,c,color="green",linewidth=1.2,linestyle="-",label="Coseno")


#Cambiar longitud de ejes
#plt.xlim(-4,4)
plt.xlim(x.min()*1.1,x.max()*1.1)
#plt.ylim(-1.2,1.2)
plt.ylim(s.min()*1.1,s.max()*1.1) #Expandir el eje un 10 % más de la función


#Cambiar las marcas en ejes
#plt.xticks(np.linspace(-4,4,9,endpoint=True))
#Poner el angulo en función de pi
#La segunda lista corresponde a una etiqueta de los valores
plt.xticks([-np.pi,-np.pi/2, 0,np.pi/2,np.pi],
	[r"$-\pi$", r"$-\pi/2$", r"$0$", r"$+\pi/2$", r"$+\pi$"])
plt.yticks(np.linspace(-1,1,5,endpoint=True),
	["-1","-0,5","","+0,5","+1"])


#Obtener los ejes de ordenadas x e y en (0,0)
ax =plt.gca()
#Da acceso a bordes del gráfico plt.gca().spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#Colocar los ticks abajo
ax.xaxis.set_ticks_position('bottom')
#Cambiar posición de eje x con set_position (("data",0))
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
#Cambiar posición de eje y con set_position ((0,"data"))
ax.spines['left'].set_position(('data', 0))


#Colocar una leyenda en el gráfico
plt.legend(loc="upper left")


#Marcar puntos del gráfico (cos y sen de 2*pi/3)
x_0=2*np.pi/3

##SENO
#Dibuje recta desde eje x hasta sin(x)
plt.plot([x_0,x_0],[0,np.sin(x_0)],color="blue",linewidth=2.5,linestyle="--")
#Para marcar un punto en donde corresponde sen(x)
#plt.scatter()
plt.scatter([x_0, ],[np.sin(x_0), ],50,color="blue")


#plt.annotate() para colocar texto en el punto
plt.annotate(r"$ \sin ( \frac {2\pi} {3} ) = \frac {\sqrt {3}} {2}$",
	xy=(x_0,np.sin(x_0)), xycoords = "data", 
	xytext=(x_0+0.2,np.sin(x_0)+0.15), fontsize=10,
	arrowprops = dict(arrowstyle = "->", connectionstyle="arc3,rad=.2"))

##COSENO
plt.plot([x_0,x_0],[0,np.cos(x_0)], color="green",linewidth=2.5,linestyle="--")
plt.scatter([x_0, ],[np.cos(x_0), ],color="green",s=50)
plt.annotate(r"$\cos ( \frac {2\pi} {3} ) = \frac {-1} {2}$",
	xy=(x_0,np.cos(x_0)),xytext=(x_0+0.15,np.cos(x_0)),
	fontsize=10)


#Hacer que la función sea semitransparente en los nºs
for label in ax.get_xticklabels() + ax.get_yticklabels():
	#Aumenta tamaño de las etiquetas
    label.set_fontsize(16)
    #poner una caja en las etiquetas
    label.set_bbox(dict(facecolor='aliceblue', edgecolor='None', alpha = 0.6))


plt.show()
plt.close()