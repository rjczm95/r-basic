
## DICCIONARIOS // ARRAYS ASOCIATIVOS

#Colección no ordenada de pares de valores: claves <-> valores. 
#Se indexa no por posición, si no utilizando las claves

#Se emplea %s para imprimir un string, sustituyendolo al final con %string
nombre = "Ramon"
print("Hola %s" %nombre)

primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("Los números primos son: %s" %primos)

#Se utiliza %d para números enteros
suma = 32
print("Sumando todo se obtiene %d" %suma)

#Se utiliza %f para numeros decimales
#Se podría poner %.decimalesf para indicar el nº de decimales que queremos
media = suma/7
print("El número decimal es: %f" %media)
print("El número decimal es: %.3f" %media)


#A la hora de definir un diccionario se emplean corchetes {}
edad = {
    "Juan Gabriel":30, 
    "María":20, 
    "Ricardo":53, 
    "Antonio":45
}
print(edad)

#Para obtener un valor se indica cual es su clave entre corchetes
print(edad["Ricardo"])

#Para cambiar el valor de una clave se realiza lo siguiente
edad["Ricardo"] = 52
print(edad)


#Para obtener cuales son las claves de un diccionario
#se emplea la función diccionario.key()
print(edad.keys())

#Para obtener cuales son los valores de un diccionario
#se emplea la función diccionario.values()
print(edad.values())

#Para conocer la longitud del diccionario
#se utiliza len()
print(len(edad))

#Se puede preguntar si una determinada clave está en el diccionario
#con la expresión clave in diccionario
#da True o False
print("Pepe" in edad)
print("María" in edad)

#Se puede eliminar un conjunto clave:valor de un diccionario
#para ello se emplea la función del diccionario[clave]
del edad["Antonio"]
print(edad)

