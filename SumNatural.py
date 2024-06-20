limite=input("Hasta que numero quieres sumar?")
limite=int(limite)+1

numeros=[]
for i in range(int(limite)):
    numeros.append(i)

sumaValores=sum(numeros)  

limite=int(limite)-1
print("La suma de los numeros naturales hasta " + str(limite) + " es " + str(sumaValores))