## LISTAS
# Las listas equivalen a los arrays de R
# Se definen como contenedores que permiten almacenar una colección de objetos en un orden determinado. 
# Se pueden acceder, añadir o eliminar objetos de forma sencilla.

L1 = [] #Lista vacía
L2 = ["a","b","r"] #Lista con valores iniciales
L3 = [2,4,6] #Listas con valores enteros

#Las listas en Python pueden tener valores heterogeneos mezclados
L4 = ["Ramon",11,True]
print(L4)

#Para acceder a un elemento se emplea L[posición del elemento]
#En Python la numeración empieza en 0, mientras que en R empieza en 1
L4[0]
print (L4[0])
#La modificación de valores en las Listas se hace como abajo
L4[0]=78
print (L4)

#A la hora de proceder a acceder un rango de a:n, tener en cuenta:
#El valor n no se toma en cuenta
print(L4[0:2])

#Para añadir objeto a la lista se emplea lista.append()
#Esta función inserta el elemento en última posición
L4.append("Ursula")
print (L4)

#Para eliminar un objeto de una lista se emplea lista.remove()
# Se indica el elemento a eliminar
#Se elimina solo un elemento, el primero coincidente de la lista
L4.remove(11)
print (L4)

#lista.reverse inivierte la lista
L4.reverse()
print (L4)

#lista.count() permite contar elementos dentro de una lista
print(L4.count(True))

#lista.index() indica el indice del elemento
print(L4.index("Ursula"))

#La función len(lista) da la longitud de la lista
print(len(L4))

L=[1,2,3,4,5,6]
#Para seleccionar elementos de 2 en 2 a partir de la posición 1
print(L[1::2]) #PAR
#Esto es así porque lista[1º elemento : ultimo elemento : cada cuantos elemento se insertan]
print(L[::2]) #IMPAR

print(L[-1])

#Comprobar si la lista tiene un elemento 
# elemento in lista
print(8 in L)