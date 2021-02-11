
# HISTOGRAMAS EN PYTHON SIN USO DE LIBRERÍAS #

#Útil para algoritmos especificos con pocos datos

# El histograma es muy útil y permite unir la estadística
# descriptiva y la teoría de probabilidades

#Utilizaremos un diccionario para establecer la 
#tabla de frecuencias

x = [0,1,1,1,2,2,3,7,7,7,25]

#Método a mano del curso
def count_elements (seq) -> dict:
	""" Función que cuenta las frecuencias
    de aparición de cada elemento de la
    secuencia dada, creando un diccionario como
    si fuese una tabla de frecuencias """
	hist = {}
	for i in seq:
    	#get() permite obtener el objeto con clave i-esima dentro del histograma, sino vale 0
		# el "+1" permite incrementar el valor en una unidad
		hist[i] = hist.get(i, 0) + 1	
	return hist

#Otro método hecho por mí
def contar_elementos (variable):
	count={}
	for i in variable:
		if i in count:
			count[i]=1+count[i]
		else:
			count[i]=1
	return count 
print(contar_elementos(x))
print("")


fAbs = count_elements(x)
print(fAbs)
print("")

#Python tiene una función que calcula directamente esto
#en la librería "collections" que es la función "Counter"
from collections import Counter
fAbs2 = Counter(x)
print(fAbs2)
print("")

#Compruebo si es verdad
print(fAbs.items() == fAbs2.items())
print("")

#Para construir el histograma lo vamos a hacer en "ASCII"
#ASCII es el estandar internacional de caracteres
def ascii_histogram(seq):
    """
    Genera un histograma de frecuencias absolutas
    colocado en horizontal y con caracteres ASCII
    """
    fAbs = count_elements(seq)
    #ordeno las claves del diccionario
    #los count se representan por "+"
    for k in sorted(fAbs):
        print('{0:5d} {1}'.format(k, '+'*fAbs[k]))

#Represento el histograma
print(ascii_histogram(x))
print("")
print("")


import numpy as np 

#Creamos una semilla
np.random.seed(2019)

vals = [1,2,3,5,7,8,9,10]

#frecuencias absolutas son creadas aquí de forma aleatoria
freqs = (np.random.randint(5,20) for i in vals)

data = []
#zip() junta dos arrays de datos y permite recorrerlos a la par
for k, v in zip(vals, freqs):
    data.extend([k]*v)

ascii_histogram(data)
print("")
















