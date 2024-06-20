print("Quieres saber si es un año bisiesto?")
year=int(input("Escribe el año"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print( str(year) + " es un año bisiesto")
else: 
    print( str(year) + " no es un año bisiesto")


