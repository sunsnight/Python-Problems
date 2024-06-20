from datetime import datetime
from dateutil.relativedelta import relativedelta

def dias_para_evento(evento):
    hoy = datetime.now()
    if evento == "muertos":
        fecha_evento = datetime(hoy.year, 11, 2)
    elif evento == "navidad":
        fecha_evento = datetime(hoy.year, 12, 25)
    else:
        print("Evento no reconocido.")
        return
    
    if fecha_evento < hoy:  # Si el evento ya pasó este año, calcular para el próximo año
        fecha_evento += relativedelta(years=1)
    
    dias_faltantes = (fecha_evento - hoy).days
    return dias_faltantes

# Uso del algoritmo
dias_para_muertos = dias_para_evento("muertos")
dias_para_navidad = dias_para_evento("navidad")

print("Días faltantes para el Día de Muertos:", dias_para_muertos)
print("Días faltantes para Navidad:", dias_para_navidad)