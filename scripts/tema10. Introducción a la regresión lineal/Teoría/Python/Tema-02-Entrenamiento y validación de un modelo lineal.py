  
### ENTRENAMIENTO Y VALIDACIÓN DE UN MODELO LINEAL ###


# Una técnica muy empleada para testear el modelo es
# dividir la muestra de la variable en dos conjuntos.
# Un conjunto sirve para entrenar el modelo y el otro
# conjunto sirve para validarlo.

# Esta técnica se emplea para evitar el problema 
# conocido como "overfitting", que se genera por el
# empleo de demasiados datos para estimar el modelo.
# En castellano, se dice de problemas de sobreajuste.

import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


diabetes = datasets.load_diabetes()

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


#Vamos a seleccionar los datos que van a ser empleados
#para testear / validar el modelo (x_test, y_test) y los
#que serán empleados para entrenarlo (x_train, y_train).
x_train = x[:-60]
x_test = x[-60:] #tomamos las últimas 60 filas
y_train = y[:-60]
y_test = y[-60:] #tomamos las últimas 60 filas


""" A. ENTRENAMIENTO DEL MODELO """

#Definimos el modelo por el método de regresión lineal
#Empleamos LinearRegression() con los datos de entrenamiento
mod = linear_model.LinearRegression()
mod.fit(x_train, y_train)

#Coeficiente del eje "x" al hacer la regresión (pte)
print(mod.coef_)
print("")

#Es el punto de corte en el eje "x" de la recta de regresión
print(mod.intercept_)
print("")


# MODELO LINEAL OBTENIDO PARA LOS DATOS (x_train, y_train)
# 𝑦̃ = 940.0556 ⋅ 𝑥 + 152.80162
# LaTeX -> $$\tilde{y} = 940.0556 \cdot x + 152.80162 $$


#Representamos los ptos de los datos estudiados con plt.scatter()
plt.scatter(x_train,y_train,color="black")
#Representamos el modelo de regresión lineal obtenido
#Para el eje "y" utilizamos mod.predict(x)
plt.plot(x_train, mod.predict(x_train), color="blue",linewidth=3)

plt.show()

#Para comprobar si este modelo de regresión se ajusta bien
#a los datos empleamos mean_squared_error y r2_score
#Estas dos funciones están en sklearn

#LaTeX -> MSE = \frac{\sum_{i=1}^n(y_i - \tilde{y_i})^2}{n}$$
#Error cuadrado medio
mse = mean_squared_error(y_train, mod.predict(x_train))
print(mse)
print("")

#Factor R cuadrado
r2s = r2_score(y_train, mod.predict(x_train))
print(r2s)
print("")


""" B. VALIDACIÓN DEL MODELO """

# Tomo el conjunto de los datos de validación, que en
# este caso es "x_test", y empleo el modelo de regresión
# definido con anterioridad con los datos de entrenamiento
# para ver como se le ajustán los datos de validación
# a dicho modelo.
# Guardamos la predicción de los datos "y" en y_pred.
y_pred = mod.predict(x_test)


#Calculo el MSE y R2
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
#Se ve que no hay problemas de "overfitting" porque
#MSE y R2 presentan mejores perspectivas.


#Represento la nube de ptos de los datos de entrenamiento
plt.scatter(x_train, y_train, color = 'black')
#Represento la nube de ptos de los datos de validación
plt.scatter(x_test, y_test, color = "red")
#Estimo la curva del modelo lineal en función de los
#datos de entrenamiento
plt.plot(x_train, mod.predict(x_train), color='blue', linewidth=3)
plt.show()





