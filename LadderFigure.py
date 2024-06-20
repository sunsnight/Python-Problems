cantidad = int(input("Escribe un número"))

if cantidad > 0:
    for i in range(cantidad, 0, -1):
        print(" "*(cantidad - i) + "+"*i)
else:
     print("Escribe un numero mayor a 0")