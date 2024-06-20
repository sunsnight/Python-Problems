
print("Vamos a calcular el factorial de un número dado")
numero=int(input("Cuál es el número?"))
fact=1

for i in range (1, numero+1):
    fact=fact * i

print("El factorial de " +str(numero) +" es " +str(fact))