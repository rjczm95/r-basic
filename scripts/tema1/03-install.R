#instalar el paquete tidyverse
install.packages("tidyverse", dep = TRUE)

#Para cargar el paquete una vez se ha descargado
library(tidyverse)

#Magic sirve para crear cuadrados mágicos
#Permiten crar cuadrados que sumen lo mismo en filas
install.packages("magic", dep = TRUE)

library(magic)

magic(6)

#Ver paquetes ya instalados
installed.packages()