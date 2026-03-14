from models import vuelo as v 
from data import logica_data as ld 
from datetime import datetime
from services import aeropuerto_service as AS
from services import piloto_service as PS
import pandas as pd 
from tabulate import tabulate

# Carga de data
data_vuelos = ld.cargar_vuelos()

# Métodos
def existe_vuelo(id):
    for _, row in data_vuelos.iterrows():
        if row["ID_Vuelo"] == id:
            return True
    return False

def gurdar_vuelo(v):
    global data_vuelos
    vuelo_dic = {"ID_Vuelo": v.ID_Vuelo,
                 "Aeropuerto_Salida": v.Aeropuerto_Salida,
                 "Aeropuerto_Llegada": v.Aeropuerto_Llegada,
                 "Fecha_Salida": v.Fecha_Salida,
                 "ID_Piloto": v.ID_Piloto,
                 "Estado_Vuelo": v.Estado_Vuelo}
    data_vuelos = pd.concat([data_vuelos, pd.DataFrame([vuelo_dic])], ignore_index=True)
    ld.guardar_vuelos(data_vuelos)
    
    
def registrar_vuelo ():
    estado_vuelo = None
    while True:
        try:
            print("Formato de ID: V....1")
            id_vuelo = input("Ingrese el ID del vuelo (6 caracteres): ").strip().upper()
            if (len(id_vuelo) == 6 and 
                id_vuelo.startswith("V") and  
                id_vuelo[1:].isdigit() and 
                not existe_vuelo(id_vuelo)):
                break
            else:
                print("El ID del vuelo es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            print()
            print("--"*30)
            print("Aeropuertos registrados")
            print("--"*30)
            AS.mostrar_aeropuertos()
            print("--"*30)
            print()
            print("Formato de ID: AP...1")
            id_aeropuerto_salida = input("Ingrese el ID del aeropuerto de salida: ").strip().upper()
            if (len(id_aeropuerto_salida) == 6 and
                id_aeropuerto_salida.startswith("AP") and  
                id_aeropuerto_salida[2:].isdigit() and
                AS.existe_aeropuerto(id_aeropuerto_salida)):
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
            
    while True:
        try:
            print()
            print("--"*30)
            print("Aeropuertos registrados")
            print("--"*30)
            AS.mostrar_aeropuertos()
            print("--"*30)
            print()
            print("Formato de ID: AP...1")
            id_aeropuerto_llegada = input("Ingrese el ID del aeropuerto de llegada: ").strip().upper()
            if (len(id_aeropuerto_llegada) == 6 and
                id_aeropuerto_llegada.startswith("AP") and  
                id_aeropuerto_llegada[2:].isdigit() and
                AS.existe_aeropuerto(id_aeropuerto_llegada)) and id_aeropuerto_llegada != id_aeropuerto_salida:
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")

    while True:
        print()
        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
            
            if fecha >= datetime.now().date():
                fecha_hora_salida = datetime.combine(fecha, datetime.now().time())
                break
            else:
                print("Fecha de salida inválida, no puede ser en el pasado")
        except ValueError:
            print("Fecha de salida inválida")
    
    """ | Función    | Convierte     | Uso                           |
        | ---------- | ------------- | ----------------------------- |
        | `strptime` | texto → fecha | validar o trabajar con fechas |
        | `strftime` | fecha → texto | mostrar fechas bonitas        |
        """
    
    while True:
        try:
            print()
            print("--"*30)
            print("Pilotos registrados")
            print("--"*30)
            PS.mostrar_pilotos()
            print("--"*30)
            print()
            id_piloto = input("Ingrese el ID del piloto: ").strip().upper()
            if id_piloto.startswith("PL") and  PS.existe_piloto(id_piloto):
                break 
            else:
                print("El ID del piloto es invalido o ya esta registrado")
        except ValueError:
            print("Error en el ingreso de datos")
            
    print()
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
        while True:
            try:
                opcion  = int(input("Ingrese el estado del vuelo : "))
                if 1<= opcion <= 4:
                    break 
                else:
                    print("El estado del vuelo no es valido")
            except ValueError:
                print("Error en el ingreso de datos")
                
        if opcion  == 4:
            return 
        if opcion  == 1:
            estado_vuelo = "A tiempo"
            break 
        if opcion  == 2:
            estado_vuelo = "Retrasado"
            break 
        if opcion  == 3:
            estado_vuelo  = "Cancelado"
            break 
        
    vuelo = v.Vuelo(id_vuelo, id_aeropuerto_salida, id_aeropuerto_llegada, fecha_hora_salida, id_piloto, estado_vuelo)
    gurdar_vuelo(vuelo)
    print("--"*30)
    print(f"Vuelo {id_vuelo} registrado correctamente")
    print("--"*30)
    print()
    
def mostrar_vuelos ():
    if data_vuelos.empty:
        print()
        print("--"*30)
        print("No hay vuelos registrados")
        print("--"*30)
        print()
        return
    else:
        cabezales = ["ID_Vuelo", "Aeropuerto_Salida", "Aeropuerto_Llegada", "Fecha_Salida", "ID_Piloto", "Estado_Vuelo"]
        print(tabulate(data_vuelos, headers=cabezales, tablefmt="grid"))


def buscar_vuelo_por_id ():
    while True:
        try:
            print("Formato de ID: V....1")
            id_vuelo = input("Ingrese el ID del vuelo (6 caracteres): ").strip().upper()
            if (len(id_vuelo) == 6 and 
                id_vuelo.startswith("V") and  
                id_vuelo[1:].isdigit()):
                break
            else:
                print("El ID del vuelo es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
            
    if not existe_vuelo(id_vuelo):
        print("El vuelo no esta registrado")
        return 
    
    print()
    print("--"*30)
    print("Vuelo encontrado ...... Cargando información ...")
    print("--"*30)
    for _, row in data_vuelos.iterrows():
        if row["ID_Vuelo"] == id_vuelo:
            print(row)
            break
    print("--"*30)
    print()
    

def buscar_vuelos_por_aeropuerto_salida ():
    while True:
        try:
            print()
            print("--"*30)
            print("Aeropuertos registrados")
            print("--"*30)
            AS.mostrar_aeropuertos()
            print("--"*30)
            print()
            print("Formato de ID: AP...1")
            id_aeropuerto_salida = input("Ingrese el ID del aeropuerto de salida: ").strip().upper()
            if (len(id_aeropuerto_salida) == 6 and
                id_aeropuerto_salida.startswith("AP") and  
                id_aeropuerto_salida[2:].isdigit()):
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
            
    if not AS.existe_aeropuerto(id_aeropuerto_salida):
        print("El aeropuerto no esta registrado")
        return 
    resultados = data_vuelos[data_vuelos["Aeropuerto_Salida"] == id_aeropuerto_salida]
    if resultados.empty:
        print(f"No se encontraron vuelos desde {id_aeropuerto_salida}.")
    else:
        # Mostrar resultados en tabla
        tabla = resultados[["ID_Vuelo", "Aeropuerto_Salida", "Aeropuerto_Llegada", "Fecha_Salida", "ID_Piloto", "Estado_Vuelo"]]
        print(f"\nVuelos desde {id_aeropuerto_salida}:")
        print(tabulate(tabla, headers=["ID", "Salida", "Llegada", "Fecha", "Piloto", "Estado"], tablefmt="grid"))
    print()
    
def buscar_vuelos_por_piloto ():
    while True:
        try:
            print()
            print("--"*30)
            print("Pilotos registrados")
            print("--"*30)
            PS.mostrar_pilotos()
            print("--"*30)
            print()
            id_piloto = input("Ingrese el ID del piloto: ").strip().upper()
            if id_piloto.startswith("PL"):
                break 
            else:
                print("El ID del piloto es invalido o ya esta registrado")
        except ValueError:
            print("Error en el ingreso de datos")
    
    if not  PS.existe_piloto(id_piloto):
        print("El piloto no esta registrado")
        return 
    
    resultados = data_vuelos[data_vuelos["ID_Piloto"] == id_piloto]
    if resultados.empty:
        print(f"No se encontraron vuelos del piloto {id_piloto}.")
    else:
        tabla = resultados[["ID_Vuelo", "Aeropuerto_Salida", "Aeropuerto_Llegada", "Fecha_Salida", "ID_Piloto", "Estado_Vuelo"]]
        print(f"\nVuelos del piloto {id_piloto}:")
        print(tabulate(tabla, headers= ["ID", "Salida", "Llegada", "Fecha", "Piloto", "Estado"], tablefmt="grid" ))
        print()

def actualizar_estado_vuelo ():
    while True:
        print()
        print("--"*30)
        print("1. Actualizar estado de vuelo ... ")
        print("2. Actualizar aeropuerto de salida ... ")
        print("3. Actualizar aeropuerto de llegada ... ")
        print("4. Actualizar fecha de salida ... ")
        print("5. Actualizar piloto ... ")
        print("6. Volver al menú principal")
        print("--"*30)
        print()
        while True:
            try:
                opcion = int(input("Ingrese una opción: "))
                if 1<= opcion <= 6:
                    break 
                else:
                    print("La opción esta fuera de rango")
            except ValueError:
                print("Error en el ingreso de datos")
        
        if opcion == 6:
            break 
        
        while True:
            try:
                print("Formato de ID: V....1")
                id_vuelo = input("Ingrese el ID del vuelo (6 caracteres): ").strip().upper()
                if (len(id_vuelo) == 6 and 
                    id_vuelo.startswith("V") and  
                    id_vuelo[1:].isdigit()):
                    break
                else:
                    print("El ID del vuelo es invalido")
            except ValueError:
                print("Error en el ingreso de datos")
                
        if not existe_vuelo(id_vuelo):
            print("El vuelo no esta registrado")
            return 

        if opcion == 1:
            print()
            print("Estado de vuelo actual: ", data_vuelos.loc[data_vuelos["ID_Vuelo"] == id_vuelo, "Estado_Vuelo"].values[0])
            print()
            while True:
                try:
                    estado_vuelo = input("Ingrese el nuevo estado del vuelo: ").strip()
                    if estado_vuelo in ["A tiempo", "Retrasado", "Cancelado"]:
                        break 
                    else:
                        print("El estado del vuelo no es valido")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_vuelos.iterrows():
                if row["ID_Vuelo"] == id_vuelo:
                    data_vuelos.at[row.name, "Estado_Vuelo"] = estado_vuelo
                    ld.guardar_vuelos(data_vuelos)
                    break
            print()
            print("--"*30)
            print(f"Vuelo {id_vuelo} actualizado correctamente")
            print("--"*30)
            print()
        
        if opcion == 2:
            
            while True:
                try:
                    print()
                    print("--"*30)
                    print("Aeropuertos registrados")
                    print("--"*30)
                    AS.mostrar_aeropuertos()
                    print("--"*30)
                    print()
                    print("Formato de ID: AP...1")
                    id_aeropuerto_salida = input("Ingrese el nuevo ID del aeropuerto de salida: ").strip().upper()
                    if (len(id_aeropuerto_salida) == 6 and
                        id_aeropuerto_salida.startswith("AP") and  
                        id_aeropuerto_salida[2:].isdigit()):
                        break
                    else:
                        print("El ID del aeropuerto es invalido")
                except ValueError:
                    print("Error en el ingreso de datos")
                    
            if not AS.existe_aeropuerto(id_aeropuerto_salida):
                print("El aeropuerto no esta registrado")
                return 
            
            for _, row in data_vuelos.iterrows():
                if row["ID_Vuelo"] == id_vuelo:
                    data_vuelos.at[row.name, "Aeropuerto_Salida"] = id_aeropuerto_salida
                    ld.guardar_vuelos(data_vuelos)
                    break
            print()
            print("--"*30)
            print(f"Vuelo {id_vuelo} actualizado correctamente")
            print("--"*30)
            print()
            
        if opcion == 3:
            while True:
                try:
                    print()
                    print("--"*30)
                    print("Aeropuertos registrados")
                    print("--"*30)
                    AS.mostrar_aeropuertos()
                    print("--"*30)
                    print()
                    print("Formato de ID: AP...1")
                    id_aeropuerto_llegada = input("Ingrese el nuevo ID del aeropuerto de llegada: ").strip().upper()
                    if (len(id_aeropuerto_llegada) == 6 and
                        id_aeropuerto_llegada.startswith("AP") and  
                        id_aeropuerto_llegada[2:].isdigit() and
                        id_aeropuerto_llegada != id_aeropuerto_salida):
                        break
                    else:
                        print("El ID del aeropuerto es invalido")
                except ValueError:
                    print("Error en el ingreso de datos")
        
            if not AS.existe_aeropuerto(id_aeropuerto_llegada):
                print("El aeropuerto no esta registrado")
                return 

            for _, row in data_vuelos.iterrows():
                if row["ID_Vuelo"] == id_vuelo:
                    data_vuelos.at[row.name, "Aeropuerto_Llegada"] = id_aeropuerto_llegada
                    ld.guardar_vuelos(data_vuelos)
                    break  
                
            print()
            print("--"*30)
            print(f"Vuelo {id_vuelo} actualizado correctamente")
            print("--"*30)
            print()
            
        if opcion == 4:
            while True:
                print()
                fecha_salida = input("Ingrese la nueva fecha de salida (YYYY-MM-DD): ").strip()
                try:
                    fecha = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
                    
                    if fecha >= datetime.now().date():
                        fecha_hora_salida = datetime.combine(fecha, datetime.now().time())
                        break
                    else:
                        print("Fecha de salida inválida, no puede ser en el pasado")
                except ValueError:
                    print("Fecha de salida inválida")
            
            for _, row in data_vuelos.iterrows():
                if row["ID_Vuelo"] == id_vuelo:
                    data_vuelos.at[row.name, "Fecha_Salida"] = fecha_hora_salida
                    ld.guardar_vuelos(data_vuelos)
                    break
            print()
            print()
            print("--"*30)
            print(f"Vuelo {id_vuelo} actualizado correctamente")
            print("--"*30)
            print()
        
        if opcion == 5:
            while True:
                try:
                    print()
                    print("--"*30)
                    print("Pilotos registrados")
                    print("--"*30)
                    PS.mostrar_pilotos()
                    print("--"*30)
                    print()
                    id_piloto = input("Ingrese el nuevo ID del piloto: ").strip().upper()
                    if id_piloto.startswith("PL"):
                        break 
                    else:
                        print("El ID del piloto es invalido o ya esta registrado")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            if not  PS.existe_piloto(id_piloto):
                print("El piloto no esta registrado")
                return 
            
            for _, row in data_vuelos.iterrows():
                if row["ID_Vuelo"] == id_vuelo:
                    data_vuelos.at[row.name, "ID_Piloto"] = id_piloto
                    ld.guardar_vuelos(data_vuelos)
                    break
            
            print()
            print()
            print("--"*30)
            print(f"Vuelo {id_vuelo} actualizado correctamente")
            print("--"*30)
            print()
            
            
def eliminar_vuelo ():  
    while True:
        try:
            print("Formato de ID: V....1")
            id_vuelo = input("Ingrese el ID del vuelo (6 caracteres)a eliminar: ").strip().upper()
            if (len(id_vuelo) == 6 and 
                id_vuelo.startswith("V") and  
                id_vuelo[1:].isdigit()):
                break
            else:
                print("El ID del vuelo es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
    
    if not existe_vuelo(id_vuelo):
        print("El vuelo no esta registrado")
        return
    
    for _, row in data_vuelos.iterrows():
        if row["ID_Vuelo"] == id_vuelo:
            data_vuelos.drop(row.name, inplace=True)
            ld.guardar_vuelos(data_vuelos)
            break
    print()
    print("--"*30)
    print(f"Vuelo {id_vuelo} eliminado correctamente")
    print("--"*30)
    print()

