def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)- i -1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


data=[]
print("Escribe 5 números")
for i in range(0,5):
    numeros=int(input())
    data.append(numeros)

BubbleSort(data)

print("Los números de menor a mayor son:")
print(data)
