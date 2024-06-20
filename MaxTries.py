print("Ingresa la contraseña")
respuesta = input().lower

maxTries=2
tries=0
contraseña = "padawan"

while respuesta() != contraseña and tries < maxTries:
        respuesta = input("La contraseña es incorrecta, intentalo de nuevo\n").lower
        tries += 1

if respuesta() == contraseña:
        print("La contraseña es correcta. ¡Bienvenida!")
else:
        print("Lo siento, has superado el número de intentos.")

