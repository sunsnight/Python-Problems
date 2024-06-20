cantidad = int(input("Escribe un número"))

if cantidad > 0:
    print("*"*cantidad)
    
    for i in range(cantidad-2):
        print("*" + " "*int(cantidad-2)+ "*")
    
    print("*"*cantidad)
else: 
    print("Escribe un número mayor a 0")