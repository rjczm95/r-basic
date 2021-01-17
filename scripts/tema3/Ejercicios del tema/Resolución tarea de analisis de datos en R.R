#Cread un vector llamado "Harry" formado
#por la sucesión de números consecutivos
#entre el -10 y 27. Pedidle a R que os 
#devuelva el elemento de índice 7.
Harry <- -10:27
Harry[7]


#Dad el máximo de la sucesión 
#(100*2^n -7*3^n) con n=0,...,200
n <- 0:200
f_x <- function (n){100*2^n-7*3^n}
max(f_x(n))


#Cread la sucesión de números consecutivos 
#entre 0 y 40. A continuación, cread el 
#vector (3*5^n - 1) con n=0,...,40. 
#Ponedle como nombre x. Ahora, dad el 
#subvector de los elementos que son 
#estrictamente mayores que 3.5
n <- 0:40
f_x <- function(n){3*5^n - 1}
x <- f_x(n)
x[3.5<x]


#Cread una función que os devuelva la 
#parte real, la imaginaria, el módulo, 
#el argumento y el conjugado de un 
#número, mostrando solo 2 cifras significativas
x=3
complex_function <- function(x){round(c(Re(x),Im(x),Mod(x),Arg(x),Conj(x)),2)}
complex_function(x)


#Cread una función que resuelva 
#ecuaciones de segundo grado (de la 
#forma Ax^2+Bx+C=0). No importa, por 
#ahora, que tengáis en cuenta las que 
#no tienen solución
pol_2_grado=function(A,B,C){c((-B+sqrt(B^2-4*A*C))/2*A,(-B-sqrt(B^2-4*A*C))/2*A)}
pol_2_grado(3,2,2)


#Tomando el vector vec = c(0,9,98,2,6,7,5,19,88,20,16,0), 
#dad 3 opciones diferentes para calcular 
#el subvector c(9,19,20,16)
vec = c(0,9,98,2,6,7,5,19,88,20,16,0)
#Métodos Subvectores c(9,19,20,16)
vec[c(2,8,10,11)]
vec[8 < vec & 21 > vec]
vec[which(vec==9 | vec==19 | vec==20 | vec==16)]
#- qué entradas son pares
which(vec%%2==0)
vec[which(vec%%2==0)]
#- qué entradas no son pares y 
#mayores que 20
vec[which(vec%%2!=0 & vec>20)]
which(vec%%2!=0 & vec>20)
#- dónde toma vec su valor máximo
which(vec==max(vec))
vec[which(vec==max(vec))]
#- dónde toma vec sus valores mínimo
which(vec==min(vec))


#PDF 1
A=rbind(c(1,3),c(2,4))
Expresion_A= A %*% (A+A) %*% A
Expresion_A [2,2]


#PDF 2
B=rbind(c(2,4,-6),c(0,0,3),c(0,-2,5))
eigen(B)$values


#PDF 3
C=rbind(c(-48,35,-12),c(-134,95,-32),c(-194,133,-44))
round(eigen(C)$vectors,3)


#PDF 4
D = rbind(c(-2,-8,-2,3),c(-3,-6,-1,2),c(-9,-22,-3,7),c(-18,-44,-8,15))
qr(D)$rank
