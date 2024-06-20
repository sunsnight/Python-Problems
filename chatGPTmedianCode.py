def calcular_estadisticas(valores):
    if not valores:
        return None, None, None
    
    maximo = max(valores)
    minimo = min(valores)
    media = sum(valores) / len(valores)
    
    return maximo, minimo, media

def main():
    valores = []
    
    while True:
        try:
            valor = float(input("Ingrese un valor (o 0 para detenerse): "))
            if valor == 0:
                break
            valores.append(valor)
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    if valores:
        maximo, minimo, media = calcular_estadisticas(valores)
        
        print("El mayor valor es:", maximo)
        print("El menor valor es:", minimo)
        print("La media de los valores es:", media)
    else:
        print("No se ingresaron valores.")

if __name__ == "__main__":
    main()
