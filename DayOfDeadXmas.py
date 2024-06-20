from datetime import datetime
from dateutil.relativedelta import relativedelta

print("¿Quieres saber cuantos dias faltan para navidad o para dia de muertos?")
respuesta = input().lower

hoy=datetime.now()

while True:
    if respuesta == "dia de muertos":
        fechaEvento = datetime(hoy.year,11,2)
        if fechaEvento < hoy:
            fechaEvento += relativedelta(years=1)
        diasFaltantes= (fechaEvento - hoy).days
        print(diasFaltantes)
    
    elif respuesta == "navidad":
        fechaEvento = datetime(hoy.year,12,25)
    
    

    

