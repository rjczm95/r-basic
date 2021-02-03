
""" NOTAS DE BACHILLERATO """

import numpy as np 
import pandas as pd 


#Fijo la semilla
np.random.seed(5008)

notas = np.random.randint(0,10,100)

#Recupero la aletoriedad del script
np.random.get_state()

#Extremos de los intervalos del estudio de las notas
L = [0, 5, 7, 9, 10]
L_names = ["Suspenso", "Aprobado", "Notable", "Sobresaliente"]


#Realizo el agrupamiento con cut() y empleando como etiqueta L_names
st_notas = pd.cut(notas, bins=L, right=False, 
	labels=L_names, include_lowest=True)


F_Abs = pd.crosstab(st_notas, columns=0).values.flatten()
F_Rel = F_Abs/len(notas)
F_Abs_sum = np.cumsum(F_Abs)
F_Rel_sum = np.cumsum(F_Rel)

intervalos = st_notas.value_counts().index

Tabla_resumen = pd.DataFrame({
	"Intervalos":intervalos,
	"Estado":L_names,
	"Frec. Abs.":F_Abs,
	"Frec. Abs. Acum.":F_Abs_sum,
	"Frec. Rel.":F_Rel,
	"Frec. Rel. Acum.":F_Rel_sum
	})

print(Tabla_resumen)











