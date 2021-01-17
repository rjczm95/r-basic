
## TUPLAS

#Una tupla es una colección de objetos que no puede modificarse (tiene tamaño y contenido fijo).
#En R no existe esta composición
#Se define con ()
#Las tuplas se emplea para evitar sobrecargas del uso de la memoria RAM

p2 = (1,2,3,4)
print(p2)

p3 = (1,2,'c',3.1415)
print(p3)
#Para acceder a un elemento de la tupla se hace de la misma manera que con las listas
print(p3[0])
print(p3[0:2])

#Se pueden asignar los valores recogidos en las tuplas a varias variables directas
a,b,c,d = p3
print (a,b,c,d)

#Para trasnformar la lista en tuplas se emplea la función list()
list3=list(p3)
print(list3)

#Se puede crear una tupla a partir de una lista con la función tuple()
list5=[8, 0, 0, 0, 0, 0, 3.1415, 2, 1, 0]
p5=tuple(list5)
print (p5)

#La función split() que permite dividir un string o numeros
print("Hola que tal  estás".split(" ")) #Se separa por espacios blancos
print("4,6,2,7,9,4,2".split(",")) #Se separa por comas

#Ejercicio. Leer del teclado una colección de nºs separados por comas
#Pasalo a lista y luego a tupla
coleccion = input("Introduce numeros separados por coma: " )
lista_coleccion=coleccion.split(",")
print(lista_coleccion)
tupla_coleccion=tuple(lista_coleccion)
print(tupla_coleccion)

#La tupla generada es de strings
#Para el calculo de la media de los numeros podemos usar
suma = 0
for i in tupla_coleccion:
	suma += float(i)

media = suma/len(tupla_coleccion)
print("La media es " + str(media))
