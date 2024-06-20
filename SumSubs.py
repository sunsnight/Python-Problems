import math

def Op(array):
        if data[0] >=0:
           print("La suma de los elementos es " + str(sum(data))) 
        elif data[0] <0:
            print("El producto de los elementos es " + str(math.prod(data)))
            
data=[]
print("Escribe 3 números")
for i in range(0,3):
    numeros=int(input())
    data.append(numeros)

Op(data)