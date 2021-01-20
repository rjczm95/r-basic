
## LIBRERÍA MATPLOTLIB

#Se prodían utilizar multitud de librerías en Python para 
#la representación gráfica como: 
#  - GGPlot (usado también en R).
#  - Plotly (web interactiva donde se suben los datos y te devuelve la gráfica).
#  - Matplotlib (es la librería básica de Python)

import matplotlib.pyplot as plt
import numpy as np

#matplotlib tiene una sublibrería llamada pyplot (alias plt)
#pyplot tiene una colección de funciones de estilizado

x = [1,2,3,4]
#Al dar solamente un valor a plt.plot() los valores son del eje y
#El vector de x por defecto empieza en 0 y sigue con 1,2,...,len(vector y)
plt.plot(x)
plt.xlabel("Eje de abcisas")
plt.ylabel("Eje de ordenadas")
#Para mostrar la figura se utiliza plt.show(), se genera un gráfico continuo
plt.show()
plt.close()

x =[1,2,3,4]
y =[1,4,9,16]
plt.plot(x,y)
plt.show() #Une los puntos discreto
plt.close()

#Para evitar que se unan puntos discretos y pintar una linea continua
#se usan parámetros adicionales en la función plt.plot()
#estos parámetros se han heredado de matlab
#en "ro" la "r" refiere al colr rojo y la "o" al punto
plt.plot(x,y,"ro")
#plt.axis() permite configurar la longitud de los ejes en la gráfica
plt.axis([0,4,0,20])
plt.show()
plt.close()


data = np.arange(0.0,10.0,0.2)
#Graficos de potencia 1, 2 y 3 en la misma gráfica
plt.plot(data, data,"r--",data, data**2,"bs",data,data**3,"g^")
plt.show()
plt.close()

#linewidth permite variar el grosor de la linea del plot
plt.plot(x,y,linewidth=2.0)
plt.show()
plt.close()

#Para evitar que la linea se difumina se emplea guarda el plot en una variable
#Se guarda en variable (especial) y pon set_antialiased
line, =plt.plot(x,y,linewidth=2.0)
line.set_antialiased(False)
plt.show()
plt.close()

#Para variar propiedades globales de todo el gráfico
#se emplea la función plt.setp()
#modifica parámetros de configuración
lines = plt.plot(data, data,data, data**2)
plt.setp(lines, color ="r", linewidth=2.0)
plt.show()
plt.close()

#alpha varía la opacidad/transparencia de la línea del gráfico
#hay más marcadores para las líneas y puntos
#"+" permite remarcar los puntos
plt.plot(x,y,alpha=0.8, marker = "+", linestyle = ":")
plt.show()
plt.close()

#Para ver todas las opciones que podemos variar en un gráfico
#emplea plt.stp(plot)
plt.setp(lines)