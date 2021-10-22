A=int(input("Ingresa el valor de A:"))
B=int(input("Ingresa el valor de B:"))
#Se elige el numero mayor intercambiandolos con un temporal
if A<B:
  C=A
  A=B
  B=C
#Se hace modulo de A y B hasta que el residuo sea 0
while B!=0:
  R=A%B
  A=B
  B=R
#Se imprime el minimo comun divisor
print("El MCD: ",A)