
numeros=int(input("¿Cuantos números quieres sumar?"))

data=[]
print("Escribe los números a sumar:")
for i in range(numeros):
    valores=int(input())
    data.append(valores)

print("La suma de los valores es " + str(sum(data)))
