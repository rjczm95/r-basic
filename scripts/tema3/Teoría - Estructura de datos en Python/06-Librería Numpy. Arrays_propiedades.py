
## NUMPY // PROPIEDADES DE LOS ARRAYS

import numpy as np

#Vamos a ver como preguntar a los array el tipo de dato, la dimensión...
#NumPy tiene la limitación de que solo trabaja con un tipo de elemento
#El tipo de dato debe de ser homogéneo

x= np.arange(12)
x= x.reshape((3,4))

#Para conocer el nº de dimensiones de un array
#se usa la función array.ndim
#En este caso son dos dimensiones (filas y columnas)
print(x.ndim)

#Para comprobar el tamaño de las dimenciones 
#se usa la array.shape
#da una tupla indicando ndim de filas y columnas
#la longitu de la tupla coincide con la dimensión del array
print(x.shape)

#la expresión array.size 
#nos informa del numero total de elementos que tiene el array
print(x.size)

#la expresión array.dtype 
#indica el tipo de dato del que está formado el array
print(x.dtype)

#la expresión array.itemsize
#da el tamaño en bytes de cada elemento de la matriz
#util para saber el tamaño total de la matriz
print(x.itemsize)

#la expresión array.data
#da el buffer que contiene los elementos de la matriz
#indica una posición de memoria RAM en la que se almacena este array
#no suele ser necesario
print(x.data)

#Para seleccionar elementos del array se realiza una metodología
#similar a las listas o tuplas en Python
# array[nº_fila , nº_columna...]
print(x[2])
print(x[2,2])
print(x[0:2,1:3])

# array.shape = (filas, columnas)
#permite cambiar las dimensiones del array
x.shape = (4,3)
print(x)

#Más formas de seleccionar en un array unidimensional
y = np.arange(12)
print(y[3:8])
print(y[1:7:2])

#Seleccionar un array a partir de otro array
z = np.arange(10, 6, -1)
print(y[z])

#Se puede acceder al array a traves de condiciones booleanas
x2=np.arange(50)
print(x2[x2>45])

#Se pueden asignar cambios de valores en el array
x2[12:24]=1
print(x2)

x2[13:16]=[0,-7,67]
print(x2)


## EJERCICIO

#3. Crear la identidad 7x7. Luego poner el numero 5 en todos los extremos
matriz=np.eye(7,7)
matriz [0] = 5
matriz [6] = 5
matriz [:,0] = 5
matriz [:,6] = 5
print(matriz)