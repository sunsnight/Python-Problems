total=int(input("¿Cuantos alumnos son en total?"))
niñas=int(input("¿Cuantas niñas estan inscritas?"))

porcentajeNiñas=(niñas*100)/total
porcentajeNiños=100-porcentajeNiñas

print("El total de alumnos se conforma por " + str(porcentajeNiñas) + "% niñas y " + str(porcentajeNiños) + "% niños")
