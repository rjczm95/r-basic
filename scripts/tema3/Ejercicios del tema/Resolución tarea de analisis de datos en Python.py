
# EJERCICIOS // SECCIÓN ANALISIS DATOS EN PYTHON

# Ejercicio 1
# Crea una función que reciba los tres coeficientes a, b y c 
# para resolver una ecuación de segundo grado. Muestra la 
# solución por pantalla y ayúdate de la librería Math para 
# acceder a la función raíz cuadrada

import math
def segundo_grado (a,b,c):
	discriminante1 = -b + math.sqrt(b**2-4*a*c)
	discriminante2 = -b - math.sqrt(b**2-4*a*c)

	solve1=discriminante1/2*a
	solve2=discriminante2/2*a

	print("El polinomio de {}x^2+{}x+c=0 tiene como solución: \n x = {} // x = {}".format(a,b,c,solve1,solve2))

segundo_grado(2,7,3)


# Ejercicio 2
# Crea una función que lea una frase de teclado y nos diga si 
# es o no un palíndromo (frase que se lee igual de izquierda a 
# derecha o al revés como por ejemplo La ruta nos aportó otro 
# paso natural)

def palindromo (frase):
	letras_frase=[]

	for letra in frase:
		if letra == " " or letra=="," or letra==".":
			pass #No se cuentan los ".", "," y " "
		else:
			letra=letra.lower() #poner en minúscula todas las letras
			letra=letra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u")
			letras_frase.append(letra)

	
	letras_invertidas = letras_frase.copy()
	letras_invertidas.reverse()

	if letras_frase==letras_invertidas:
		print ("La frase introducida es un palíndromo")
	else:
		print("No es un palíndromo")

palindromo("La ruta nos aportó otro paso natural.")


# Ejercicio 3
# Crea un diccionario que tenga por claves los números del 1 
# al 10 y como valores sus raíces cuadradas

import math

numeros=list(range(1,11))
raices=[]
for i in numeros:
	i=math.sqrt(i)
	raices.append(i)
dicc_raices=dict(zip(numeros,raices))
print(dicc_raices)


# Ejercicio 4
# Crea un diccionario que tenga como claves las letras del 
# alfabeto castellano y como valores los símbolos del código 
# morse (los tienes todos en la Wikipedia). A continuación crea 
# un programa que lea una frase del teclado y te la convierta a 
# Morse utilizando el diccionario anterior

letras = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z"
lista_letras=letras.split(", ")
morse=["· —","— · ·","— · — ·","— · ·","·","· · — ·","— — ·","· · · ·","· ·","· — — —","— · —","· — · ·","— —","— ·","— — · — —","— — —","· — — ·","— — · —","· — ·","· · ·","—","· · —","· · · —","· — —","— · · —","— · — —","— — · ·"]
dicc_morse=dict(zip(lista_letras,morse))
print(dicc_morse)


# Ejercicio 5
# Crea una función que dados dos diccionarios nos diga que 
# claves están presentes en ambos

def claves_repetidas (dic1,dic2):
	repeticiones=[]
	for i in dic1.keys():
		for j in dic2.keys():
			if i in repeticiones:
				pass
			elif i == j:
				repeticiones.append(i)

	if len(repeticiones)==0:
		print("No hay ninguna clave repetida")
	else:
		print("Las claves repetidas aparecen en la siguiente lista: {}".format(repeticiones))

valor={"e":2,"r":9,"q":3,"e":4}
t={"e":4,"b":3,"s":0,"r":9,"e":0}	
claves_repetidas(valor,t)

# Ejercicio 6
# Crea una función que dado un número N nos diga si es primo 
# o no (tiene que ir dividiendo por todos los números x 
# comprendidos entre 2 y el propio número N menos uno y 
# ver si el cociente de N/x tiene resto entero o no).

def es_primo (N):
	numeros =list(range(2,N))
	suma=0
	for i in numeros:
		if N%i==0:
			suma+=1
	if suma !=0:
		print("El número {} no es primo".format(N))
	elif suma==0:
		print("El número {} es primo".format(N))

es_primo(23)


# Ejercicio 7
# Investiga la documentación de la clase string y crea un 
# método que lea una frase del teclado y escriba la primera 
# letra de cada palabra en Mayúscula.

def mayuscula (frase2):
	palabras = frase2.title()
	print(palabras)

mayuscula("hola soy ramon, esto es una prueba.")


# Ejercicio 8
# Crea una función que calcule el máximo común divisor de 
# dos números introducidos por el usuario por teclado.

def gcm (a,b):
	if a>b:
		target=list(range(1,a+1))
	elif b>a:
		target=list(range(1,b+1))
	elif a==b:
		target=list(range(1,a+1))

	numero=0
	for i in target:
		if a%i==0 and b%i==0:
			numero=i

	print("El máximo común divisor de {} y {} es {}.".format(a,b,numero))

gcm(15,20)


# Ejercicio 9
# Investiga el Cifrado del César y crea una función que lo 
# reproduzca en Python. Cada letra del mensaje original se 
# desplaza tres posiciones en el alfabeto estándar. La A se 
# convierte en la D, la B se convierte en la E, la C se 
# convierte en la F... y cuando se acaba el alfabeto se le 
# vuelve a dar la vuelta: la X se convierte en la A, la Y en la 
#B y la X en la C. Los números no sufren ninguna modificación.

def cifrado_cesar (texto):

	abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	texto=texto.upper()
	desplazamiento=3
	#Variable que permite guardar el mensaje cifrado
	mens_cifrado=""

	for i in texto:
    # Si la letra está en el abecedario se reemplaza
		if i in abecedario:
			posicion_letra=abecedario.index(i)
		# Sumamos 3 para movernos a la derecha del abecedario
			nueva_posicion=(posicion_letra+desplazamiento) % len(abecedario)
		#Se incluye la nueva letra en el mensaje
			mens_cifrado+=abecedario[nueva_posicion]

		else:
		#Si no está en el abecedario
			mens_cifrado+=i

	print("Mensaje cifrado: {}".format(mens_cifrado))

texto="hola caracola"
cifrado_cesar(texto)




# Ejercicio 10
#Dado una lista de nombres de persona, escribe un algoritmo 
# que los ordene de tres formas diferentes:
#A. De forma alfabética
#B. De forma alfabética invertida
#C. De nombre más corto al más largo.

def nombres_ordenados (lista_nombres):
	lista_nombres.sort() #lista_nombre los ordena alfabeticamente
	invertida=lista_nombres.copy()
	invertida.reverse()
	longitud=lista_nombres.copy()
	longitud=sorted(longitud,key=len)

	print("Lista de nombres ordenada alfabeticamente: {}\nLista de nombres invertida: {}\nLista ordenadas por longitud de nombre: {}".format(lista_nombres,invertida,longitud))


c=["Alfred","Rui","Alba","Carmina","Victor","Jorge"]
nombres_ordenados(c)