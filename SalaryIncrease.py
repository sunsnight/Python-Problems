
salario=int(input("¿Cuál es el salario a evaluar?"))

if salario<=15000.00:
    print("Incrementa el salario 20%")
    salario=salario*1.2
    print("El nuevo salario es: " + str(salario))
else: 
    print("Incrementa el salario 15%")
    salario=salario*1.15
    str(salario)
    print("El nuevo salario es: " + str(salario))
