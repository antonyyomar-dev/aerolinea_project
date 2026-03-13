from data import logica_data as ld
pasajeros = ld.cargar_pasajeros()
from data import logica_data as ld 

# Carga de data
data_pasajeros = ld.cargar_pasajeros()

def existe_pasajero(id_pasajero):
    for _, row in data_pasajeros.iterrows():
        if row["ID_Pasajero"] == id_pasajero:
            return True
    return False
while True:
    try:
        id_pasajero = input("Ingrese el ID del pasajero (P001): ")
        if "P" in id_pasajero[0] and not existe_pasajero(id_pasajero):
            break 
        else:
            print("El ID del pasajero es invalido")
    except ValueError:
        print("Error en el ingreso de datos")


