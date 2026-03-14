from data import logica_data as ld
pasajeros = ld.cargar_pasajeros()
from data import logica_data as ld 

from datetime import datetime
data_aeropuertos = ld.cargar_aeropuertos()
while True:
    print("--"*6)
    print("ESTADO DE VUELO")
    print("--"*6)
    print("1. A tiempo")
    print("2. Retrasado")
    print("3. Cancelado")
    print("4. Cancelar operación")
    print("--"*6)
    print()
    while True:
        try:
            estado_vuelo = input("Ingrese el estado del vuelo : ")
            if 1<= estado_vuelo <= 4:
                break 
            else:
                print("El estado del vuelo no es valido")
        except ValueError:
            print("Error en el ingreso de datos")
            
    if estado_vuelo == 4:
        break
    if estado_vuelo == "1":
        estado_vuelo = "A tiempo"
        break 
    if estado_vuelo == "2":
        estado_vuelo = "Retrasado"
        break 
    if estado_vuelo == "3":
        estado_vuelo = "Cancelado"
        break 
    
while True:
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ").strip()
    try:
        fecha = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
        
        if fecha >= datetime.now().date():
            break
        else:
            print("Fecha de salida inválida, no puede ser en el pasado")
    except ValueError:
        print("Fecha de salida inválida")
    