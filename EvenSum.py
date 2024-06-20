print("Vamos a sumar numeros pares")
limite = input("¿Hasta que número quieres sumar?")
limite=int(limite)+1

numeros=[]
for i in range(limite):
    if i % 2 == 0:
        numeros.append(i)

suma=sum(numeros)

limite=int(limite)-1
print("La suma de los numeros pares hasta " + str(limite) + " es " + str(suma))