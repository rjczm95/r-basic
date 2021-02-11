 
""" EJERCICIO AGRUPACION DATOS CUANTITATIVOS"""

import pandas as pd
import numpy as np

#Cargo el fichero de estudio
crabs = pd.read_table("../../../data/datacrab.txt", 
	delimiter =" ", header=0)

#Investigo el data frame creado
print(crabs.head())
print("")
print(crabs.dtypes)
print("")

#Guardo la variable de estudio "width"
cw = crabs["width"]

#Determino la longitud de la variable cw
n = len(cw)


""" Regla de Scott """

#Calculo la amplitud teórica y el número de clases
As = 3.5 * cw.std() * n**(-1/3)
k1 = np.ceil((max(cw)-min(cw))/As)
print(k1)
#El nº de clases de la agrupación será 10
print("")


#Determino la amplitud de los intervalos 
A1 = (max(cw)-min(cw))/k1
print(A1)
#Se determina la amplitud que será de 1.3
A1 = 1.3
print("")


#Para determinar los extremos de los intervalos
#se determina el primer extremo en primer lugar
L1 = min(cw)-(1/2)*0.1
#Lista de extremos de los intervalos de la agrupación
L_scott = L1 + (A1*np.arange(11))
print(L_scott)
print("")

#Lista de marcas de clase de la agrupación
X_scott = (L_scott[0:len(L_scott)-1]+L_scott[1:len(L_scott)])/2 
print(X_scott)
print("")



""" Regla de la Raíz """

import math

#Calculo la amplitud teórica y el número de clases
k2 = np.ceil(math.sqrt(n))
print(k2)
#El nº de clases de la agrupación será 14
print("")


#Determino la amplitud de los intervalos 
A2 = (max(cw)-min(cw))/k2
print(A2)
#Se determina la amplitud que será de 0.9
A2 = 0.9
print("")


#Para determinar los extremos de los intervalos
#se determina el primer extremo en primer lugar
L1 = min(cw)-(1/2)*0.1
#Lista de extremos de los intervalos de la agrupación
L_sqrt = L1 + (A2*np.arange(15))
print(L_sqrt)
print("")

#Lista de marcas de clase de la agrupación
X_sqrt = (L_sqrt[0:len(L_sqrt)-1]+L_sqrt[1:len(L_sqrt)])/2 
print(X_sqrt)
print("")




""" Regla de Sturges """

import math

#Calculo la amplitud teórica y el número de clases
k3 = np.ceil(1+math.log(n,2))
print(k3)
#El nº de clases de la agrupación será 14
print("")


#Determino la amplitud de los intervalos 
A3 = (max(cw)-min(cw))/k3
print(A3)
#Se determina la amplitud que será de 1.4
A3 = 1.4
print("")


#Para determinar los extremos de los intervalos
#se determina el primer extremo en primer lugar
L1 = min(cw)-(1/2)*0.1
#Lista de extremos de los intervalos de la agrupación
L_sturges = L1 + (A3*np.arange(10))
print(L_sturges)
print("")

#Lista de marcas de clase de la agrupación
X_sturges = (L_sturges[0:len(L_sturges)-1]+L_sturges[1:len(L_sturges)])/2 
print(X_sturges)
print("")



""" Regla de Freedman-Diaconis """

#Calculo la amplitud teórica y el número de clases
Afd = 2 * (np.quantile(cw,0.75)-np.quantile(cw,0.25)) * n**(-1/3)
k4 = np.ceil((max(cw)-min(cw))/Afd)
print(k4)
#El nº de clases de la agrupación será 13
print("")


#Determino la amplitud de los intervalos 
A4 = (max(cw)-min(cw))/k4
print(A4)
#Se determina la amplitud que será de 1.1
A4 = 1.1
print("")


#Para determinar los extremos de los intervalos
#se determina el primer extremo en primer lugar
L1 = min(cw)-(1/2)*0.1
#Lista de extremos de los intervalos de la agrupación
L_fd = L1 + (A4*np.arange(14))
print(L_fd)
print("")

#Lista de marcas de clase de la agrupación
X_fd = (L_fd[0:len(L_fd)-1]+L_fd[1:len(L_fd)])/2 
print(X_fd)
print("")


