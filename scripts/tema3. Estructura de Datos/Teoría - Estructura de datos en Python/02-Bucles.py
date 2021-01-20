
## BUCLES

L = [1,2,3,4,5,6]

#Los bucles for iteran 
#sobre una colección (una lista, un string, un objeto iterable)

#Iterar significa ir recorriendo algo
for numero in L:
    print(numero)
#numero se queda al final con el último elemento recorrido
print(numero)

#Uso de un rango de valores entre a y b es range (a,b)
for x in range(0,10): # range(10) = range(0,10)
    print(x)

#Tambien se puede iterar sobre un string
for c in "Ramon Ceballos":
    print(c)

#Ejemplo: Calculo de las medias de unas notas (USO FOR)
notas = [3.5, 6.7, 8, 9, 4.5]
suma = 0
for nota in notas:
    suma = suma + nota
print(suma/len(notas))


#El bucle while se repite hasta que 
#la condición booleana deja de ser cierta.
#No se conoce cuantas veces se va a ejecutar el bucle
count = 0
while count < 10:
    print(count)
    count +=1

#Hay una variante del bucle for para guardar la posición del elemento
# for posición, elemento in enumerate(lista)
primos = [2,3,5,7,11,13,17,19,23,29]
for idx, p in enumerate(primos): 
    print(idx, p)

#Cuando solo queremos la posición de los objetos se emplea:
#for posición in range (len(lista))
for idx in range(len(primos)):
    print(idx, primos[idx])

#Ejercicio: CRIBA DE ERATOSTENES

#Solución 1
n_primos=list(range(2,121))

for primo in n_primos:
	for no_primo in n_primos:
		if primo == no_primo:
			pass
		elif no_primo%primo == 0:
			n_primos.remove(no_primo)

print(n_primos)

#Solución 2
n = int(input("Introduce un número para determinar los números primos comprendidos hasta dicho número: "))

def criba_eratostenes (n):
	primos=[]
	no_primos=[]

	for i in range(2,n+1):
		if i not in no_primos:
			primos.append(i)
			for j in range (i+1,n+1):
				if j%i==0:
					no_primos.append(j)
		else:
			pass
	print (primos)

criba_eratostenes(n)
