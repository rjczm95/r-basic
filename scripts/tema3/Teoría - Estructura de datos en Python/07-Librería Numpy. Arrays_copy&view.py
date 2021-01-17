
# NUMPY / ARRAYS / COPY AND VIEW 

import numpy as np

#Cuando se trabajo con arrays habria que distinguir si es el original o una copia

## TRES FORMAS DE TRABAJAR CON ARRAYS:

#### ARRAYS ASIGNADOS (array_original = nuevo_array)
#### ARRAYS COPIADOS (nuevo_array = array_original.copy())
#### ARRAYS VISTOS  (nuevo_array = array_original.view())


#En este caso se da una asignación de array (CUIDADO)
#Esto significa que si se cambia la forma de la nueva copia creada(y)
#el array original (x) también se modificará
x = np.arange(10)
y = x
y.shape = (2,5)
print(x)
print(y)

#Para evitar las asignaciones de arrays se emplea
#la función array.copy()
#Así si se crea un nuevo array que permite modificar el nuevo array
#sin modificar el antiguo
z = x.copy()
print(z)

print(z is x) #Esto es porque es una copia
print(y is x)

# Hay arrays que puede compartir la misma o parte de la misma info
#y a su vez tener propiedades diferentes
#Esto se conoce como una vista y se genera con
#el empleo de la función array.view()
#Si se modifica los valores de una vista, también se modifica
#el array original
t = x.view()
print(t)
#Se puede cambiar la forma de t sin cambiar la forma de x
t.shape =(5,2)
print(t)
print(x)


s = x[0:2, 1:3] #esto es una vista
s[:] = 5
print(s) #Subarray o submatriz del array x // vista
print(x) #Array original
print(y) #Array asignado
print(z) #array copiado // uno array que no cambia