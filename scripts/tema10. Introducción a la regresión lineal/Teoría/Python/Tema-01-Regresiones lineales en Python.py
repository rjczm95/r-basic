
### REGRESIONES LINEALES EN PYTHON ###


# Importante el conocer el paquete SCIKIT LEARN
# Tiene un subpaquete enfocado a la regresión lineal.

import matplotlib.pyplot as plt 
import numpy as np 
#Para importar datasets
from sklearn import datasets
#Para emplear el modelo de regresión lineal
from sklearn import linear_model
#Importamos el error cuadrado medio
#Importamos el coeficiente de determinación
from sklearn.metrics import mean_squared_error, r2_score



# El conjuto de datos a estudiar en este script tiene que
# ver con la "diabetes".
# Vamos a realizar un plot de dos dimensiones y una
# regresión de dos variables del dataset de "diabetes".

# También existe la "regresión multiple" donde en lugar de 
# emplear una sola variable como predictora, se pueden 
# todas las variables que queramos para estimar el valor
# de la variable predicha.


diabetes = datasets.load_diabetes()

#El tipo de dato es un sklearn.utils.Bunch
#Es un empaquetamiento de los datos que hace scikit learn
print(type(diabetes))
print("")

#Transformamos el tipo de dato a un array con "data"
print(type(diabetes.data))
print("")

#Forma del array
#Vemos que hay 10 columnas y 442 filas
print(diabetes.data.shape)
print("")

#Seleccionamos como variable independiente la columna
#2 del DF diabetes
#Se debe realizar reshape(-1, 1).astype(np.float32)
#para poder trabajar con los datos. Es debido a que
#se debe de dar esta estructura de datos en LinearRegression()
#ERROR DE WINDOW lo de que tenga que ser np.float32
x = diabetes.data[:, 2].reshape(-1, 1).astype(np.float32)

#Seleccionamos como variable dependiente a la columna
#target (objetivo de la predicción) del DF diabetes
#Suele haber un target para cada DF de sklearn
y = diabetes.target


#Definimos el modelo por el método de regresión lineal
#Empleamos LinearRegression()
mod = linear_model.LinearRegression()

#Crea el ajuste de la regresión lineal en base a los datos dados
mod.fit(x, y)

#Coeficiente del eje "x" al hacer la regresión (pte)
print(mod.coef_)
print("")

#Es el punto de corte en el eje "x" de la recta de regresión
print(mod.intercept_)
print("")


# MODELO LINEAL OBTENIDO PARA LOS DATOS
# 𝑦̃ = 940.05574082 ⋅ 𝑥 + 152.80161883617347
# LaTeX -> $$\tilde{y} = 940.05574082\cdot x + 152.80161883617347 $$


#Representamos los ptos de los datos estudiados con plt.scatter()
plt.scatter(x,y,color="black")
#Representamos el modelo de regresión lineal obtenido
#Para el eje "y" utilizamos mod.predict(x)
plt.plot(x, mod.predict(x), color="blue",linewidth=3)

plt.show()

#Para comprobar si este modelo de regresión se ajusta bien
#a los datos empleamos mean_squared_error y r2_score
#Estas dos funciones están en sklearn

#LaTeX -> MSE = \frac{\sum_{i=1}^n(y_i - \tilde{y_i})^2}{n}$$
#Error cuadrado medio
mse = mean_squared_error(y, mod.predict(x))
print(mse)
print("")

#Factor R cuadrado
r2s = r2_score(y, mod.predict(x))
print(r2s)
print("")

#r cuadrado es 0.34 y vemos que no se ajusta bien este tipo de regresión
#No se puede concluir que los datos se ajusten a un modelo lineal


