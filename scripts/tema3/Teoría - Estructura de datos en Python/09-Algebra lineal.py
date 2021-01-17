
## ALGEBRA LINEAL (INTRODUCCIÓN)

#Se pueden crear matrices sin cargar la libreria NumPy 
#Para ello se emplean las listas de Python

row = [1,2,3] #Tres filas con un elemento

columns = [[1],[2],[3]] # Una fila con tres columnas

matriz =[[1,3,5],[1,1,1],[0,4,6]]
print(matriz[0]) #Obtenemos la primera fila
print(matriz[0][0]) #Obtenemos el primer elemento de primera fila y primera columna

#No obstante es mejor utilizar NumPy para tratar con matrices
#Ya que puede generar problemas
import numpy as np

matriz= np.array(matriz)
print(matriz)

matrizA=np.array([[1,2],[3,4]])
matrizB=np.array([[3,0],[1,-1]])

print(matrizA+matrizB) #Para sumar matrices

print(matrizA.dot(matrizB)) # Para multiplicar matrices (producto matricial)

print(matrizA.transpose()) #La transpuesta de matrizA

print(matrizA.trace()) #Da la traza de una matriz (suma de elementos de la diagonal)


#Subpaquete LINALG dentro de la Libreria NumPy
#Se relaciona con la regresión lineal algebraica

print(np.linalg.matrix_rank(matrizA)) #Da el rango de la matriz
print(np.linalg.matrix_power(matrizA,5)) #Elevar una matriz a un nº x
print(np.linalg.det(matrizA)) #Da el determinante de la matriz
print(np.linalg.inv(matrizA)) #Da la matriz inversa de una matriz

#CUIDADO CON LOS REDONDEOS
print(np.linalg.inv(matrizA).dot(matrizA)) #Se genera la matriz identidad al multiplicar la matriz y su inversa
#Solo se pueden calcular la matriz inversa de matrices cuadradas
#Tampoco s epuede calcular la matriz inversa de aquella matriz cuyo ranago sea inferior a su orden

#Para obtener una columna de la matriz se hace un bucle
for i in matrizA:
	print(i[0])

print(matrizA[:,0])


