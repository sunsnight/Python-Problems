print("¿Tienes un titulo de bachiller?")
respuesta =  input().lower

if respuesta() == "si":
    print("Bienvenido al grado de eduación superior")

if respuesta() == "no":
    print("Debemos aplicar una prueba matematica")
    operacion = int(input("¿Cuál es el cuadrado de 25?"))
    if operacion == 25**2:
        print("La respuesta es correcta, bienvenido al grado de educación superior")
    else:
        print("La respuesta es incorrecta, no es posible concretar tu inscripción")