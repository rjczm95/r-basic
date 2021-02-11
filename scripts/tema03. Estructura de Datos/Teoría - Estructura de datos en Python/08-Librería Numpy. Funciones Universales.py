
## NUMPY // FUNCIONES UNIVERSALES (ufunc)

#Las funciones universales son funciones que realizan operaciones
#sobre todos los elementos de un array sin tener que 
#implementar un bucle para aplicar la operación elemento a elemento

#Hay dos tipos de operaciones:
#  - Operaciones unarias: se hacen elemento a elemento (sqrt(), sin(), cos()...)
#  - Operaciones binarias: se trabaja sobre dos arrays y suelen dar un array de resultado (maximun(),minimun()...)

import numpy as np

#OPERACIONES ARITMÉTICAS BÁSICAS
#Así se hace la suma, resta, división o multiplicación de un numero cualquiera en todos los elementos de un array
#Estas 4 operaciones aritméticas son unarias
x = np.arange(1,10)
print(x+3)
print(x-4)
print(x/2)
print(x*5)

#OPERACIONES TRIGONOMETRICAS
#np.sin(array)
#np.cos(array)
#np.tan(array)
#np.pi da el número pi
alpha = np.linspace(0,2*np.pi, 4) #cuatro angulos de 0 a 2*pi (0,pi/2,pi,3*pi/2,2*pi)
print(np.sin(alpha))
print(np.cos(alpha))
print(np.tan(alpha))

#OPERACIONES EXPONENCIALES Y LOGARITMICAS
np.exp(x) #nº e elevado a los elementos del array
np.exp2(x) # 2 elevado a los elementos del array
np.power(3,x) # 3 elevado a los elementos del array
np.power(x, 2) # los elementos del array elevados a 2
np.log(x) # logaritmo de los nºs del array
np.log2(x) # logaritmo en base 2 de los nºs del array
np.log10(x) # logaritmo en base 10 de los nºs del array

#MÉTODOS ESTADÍSTICOS DE NUMPY
#NumPy tiene dos versiones de operaciones:
#  - Libres de nan donde se pone np.nan"op"(array)
#  - Operaciones normales con nan np."op"(array)
np.sum(x) # sumar los valores del array (cuidado con los nan)
np.nansum(x) # sumar los valores del array eliminando nan
np.prod(x) # multiplicar los valores del array (está la versión nan)
np.mean(x) # la media de los elementos ((está la versión nan))
np.median(x) # la mediana (está la versión nan)
np.min(x) # el valor más grande del array (está la versión nan)
np.max(x) # el valor más pequeño del array (está la versión nan)
np.std(x) # la desviación típica del array (está la versión nan)
np.var(x) # la varianza (cuadrado de std) del array (está la versión nan)
np.argmin(x) # la posición en la que está el valor más pequeño
np.argmax(x) # la posición en la que está el valor más grande
np.percentile(x, q=0.95) # permite calcular percentiles

#PREGUNTAR SI EL ARRAY CUMPLE UNA CONDICIÓN
y = np.array([True, False, False, True])
np.any(y) #pregunta si algun valor del array es verdadero en base a una condición
np.all(y) #pregunta si todos los valores del array son verdaderos en base a una condición


#np.random.seed(valores) permite establecer las semillas o valores
#que se van a utilizar a posteriori en la distribución aleatoria
#permite que los valores que salgan a posteriori no varien cada
#vez que se ejecute el script
np.random.seed(2019)

#np.random.random genera tres filas y cinco columnas con valoress aleatorios
z = np.random.random((3,5))
print(z)

print(z.sum()) #Suma todos los valores de array z
print(z.sum(axis=0)) #Suma por columnas dando en este caso 5 valores
print(z.sum(axis=1)) #Suma por filas dando en este caso 3 valores


## DISTRIBUCIONES ALEATORIAS
# Es importante tener en cuenta la siguiente sucesión:
#    np.random a partir de la cual se pueden utilizar diversas funciones
