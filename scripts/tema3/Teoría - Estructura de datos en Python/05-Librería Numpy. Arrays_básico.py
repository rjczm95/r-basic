
## LIBRERIA NUMPY // INTRO ARRAYS

#Numpy es el acrónimo de Numeric Python

#Cargar la librería de numpy en el script de python
import numpy as np

L1 =[1,2,3,4,5,6,7,8] #Crear una lista

x1 = np.array(L1) #Se transforma la lista en array con la función np.array(lista)
print(x1)

x2 = np.array(L1, dtype = "float32") #dtype se utiliza para especificar el tipo de dato
print(x2)

#En los arrays hay diferentes tipos de datos:
# - bool_ (para booleanos)
# - int_, intc, intp, int8 (8 bytes), int16, int32 e int64 (para nºs enteros)
# - unit8, unit16, unit32, unit64 (para nºs enteros sin signo)
# - float_ (==float64), float16, float32, float64 (para nºs decimales) (+/-999.9999999e99999)
# - complex_ (==complex64), complex64, complex128 (a+bi; a,b  ∈  float_)

#Para generar arrays de ceros se emplea np.zeros(dimensión)
#la dimensión pueden ser filas y columnas)
print(np.zeros((3,4)))

#Para generar arrays de unos se emplea np.ones(dimensión)
print(np.ones((2,2,)))

#La función np.arange() permite generar 
#una lista de nºs que se incrementan de forma regular
print(np.arange(10))
#Para generar lista de "a" a "b" se usa np.arange(a,b)
print(np.arange(3,12,dtype = float))
#Para agenerar nºs de "a" a "b" con intervalos n
#se usa np.arange(a,b,n)
print(np.arange(4,5,0.1))

#Una variante de np.arange() es la función np.linspace()
#Permite crear un array entre "a" y "b" con un nº especifico de elementos (p)
#estos elementos están separados con la misma distancia
#Sintaxis: np.linspace(a,b,p)
print(np.linspace(1,7,12)) #12 numeros tiene el arrange

#En cuanto a matrices, cuando se requiere crear la matriz identidad
#se emplea np.eye(tamaño matriz)
print(np.eye(5,5))

#Se puede modificar un array
x3=np.arange(24)
#Para redimensionar se emplea array.reshape(nueva_distribucion)
#La nueva redistribución debe ser válida para los valores que tengamos
print(x3.reshape((6,4)))
print(x3.reshape((3,8)))

#La función np.ravel(array) devuelve el mismo array en forma unidimensional
x4=np.array([[1,2,3,4], [5,6,7,8]])
print(x4)
print(np.ravel(x4))

#Una variante de np.ravel(array) es array.flatten()
#Genera una copia del array colapsado en una sola diemnsión
print(x4.flatten())

#Otra acción útil es transponer el array
#para ello se usa np.transpose(array)
print(np.transpose(x4))

# función np.resize(array,dimensión_nueva)
#Permite crear un nuevo array con la forma especifica
#De este modo se crea el array de datos con la dimensión indicada
#Si hay más elementos que en el array origen repite los elementos
print(np.resize(x4,(5,3)))


#EJERCICIOS

#1. Crear un array de datos con valores entre 5 y 120.
print(np.arange(5,121))

#2. Crear una matriz 4x4 con los valores desde 0 hasta 15.
ej2=np.arange(0,16)
print(ej2.reshape((4,4)))

#3. Crear la identidad 7x7
print(np.eye(7,7))

#4. Crear un array de 20 elementos y transformarlos en una matrix 5x4
ej4=np.arange(0,20)
print(ej4.reshape((5,4)))

#5. Crear un array con 20 números con los valores entre 0 y 5 espaciados de forma uniforme
print(np.linspace(0,5,20))