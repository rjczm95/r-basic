
""" CREACIÓN DE FUNCIONES PARA TABLA DE FRECUENCIAS DE DATOS AGRUPADO """

import numpy as np
import pandas as pd

# Cargo el DF de iris y guardo la longitud de petalos
iris = pd.read_table("../../../../data/iris2.txt", 
	sep=" ", header=0)
#Aplano la columna a un vector
petals = iris[["Petal.Length"]].values.flatten()


### PRIMERA FUNCIÓN

# La primera sirve en el caso en que vayamos a tomar 
# todas las clases de la misma amplitud. 

# Sus parámetros son: 
#  - x, el vector con los datos cuantitativos
#  - k, el número de clases.
#  - A, su amplitud.
#  - p, la precisión de los datos.

def TableFrecs (x,k,A,p):
	L = (min(x)-1/2*p) + A*(np.arange(k+1))
	x_cut = pd.cut(x, bins=L, right=False)
	intervals = x_cut.value_counts().index
	marca_clase = (L[0:len(L)-1] + L[1:len(L)])/2
	Fr_abs = pd.crosstab(x_cut, columns=0, dropna=False).values.flatten()
	Fr_rel = np.round(Fr_abs/len(x),4)
	Fr_abs_cum = np.cumsum(Fr_abs)
	Fr_rel_cum = np.cumsum(Fr_rel)
	tabla = pd.DataFrame({
		"Intervals":intervals,
		"Class marks":marca_clase,
		"Fr_abs":Fr_abs,
		"Fr_abs_cum":Fr_abs_cum,
		"Fr_rel":Fr_rel,
		"Fr_rel_cum":Fr_rel_cum, 
		})
	print(tabla)


print (TableFrecs(petals,6,1,0.1))


print("\n")

### SEGUNDA FUNCIÓN

# La segunda es para cuando conocemos los extremos de 
# las clases. 

# Sus parámetros son: 
#  - x, el vector con los datos cuantitativos.
#  - L, el vector de extremos de clases.
#  - V, un valor lógico, que ha de ser `TRUE` si queremos que el último intervalo sea cerrado, y `FALSE` en caso contrario.

def TableFrecs_L (x,L,V):
	x_cut = pd.cut(x, bins=L, right=False, include_lowest=V)
	intervals = x_cut.value_counts().index
	marca_clase = (L[0:(len(L)-1)] + L[1:len(L)])/2
	Fr_abs = pd.crosstab(x_cut, columns=0, dropna=False).values.flatten()
	Fr_rel = np.round(Fr_abs/len(x),4)
	Fr_abs_cum = np.cumsum(Fr_abs)
	Fr_rel_cum = np.cumsum(Fr_rel)
	tabla = pd.DataFrame({
		"Intervals":intervals,
		"Class marks":marca_clase,
		"Fr_abs":Fr_abs,
		"Fr_abs_cum":Fr_abs_cum,
		"Fr_rel":Fr_rel,
		"Fr_rel_cum":Fr_rel_cum, 
		})
	print(tabla)

print(TableFrecs_L(petals, L = np.array([1, 3, 4, 5, 5.5, 6, 6.5, 7]), V = False))





