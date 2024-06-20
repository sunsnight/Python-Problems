import math
numero=int(input("Escribe un número"))
if numero <= 0:
    print("ERROR: Escribe un número mayor a 0")
else:
    exp=numero**2
    raiz=math.sqrt(numero)
    print("El cuadrado de " + str(numero) + " es: " + str(exp) + " y la raíz cuadrada es: " + str(raiz))