import statistics

numbers=[]

print ("Escribe los numeros para obtener el menor, mayor y la media, para parar escribe 0")

while True:
        valores = int(input())
        if valores == 0:
             break
        numbers.append(valores)

maximo=max(numbers)
minimo=min(numbers)
media=statistics.mean(numbers)

print(" El máximo es: " + str(maximo) + "\n El mínimo es: " + str(minimo) + "\n La media es: " + str(media))

