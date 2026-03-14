from models import aeropuerto as a 
from data import logica_data as ld 
from tabulate import tabulate
import pandas as pd
from services import pasajero_service as ps
from data import base_paises as bp

# Carga de data
data_aeropuertos = ld.cargar_aeropuertos()

# Métodos

def existe_aeropuerto(id_aeropuerto):
    for _, row in data_aeropuertos.iterrows():
        if row["ID_Aeropuerto"] == id_aeropuerto:
            return True
    return False 

def guardar_aeropuerto(a):
    global data_aeropuertos
    aeropuerto_dic = {"ID_Aeropuerto": a.ID_Aeropuerto, 
            "Nombre_Aeropuerto": a.Nombre_Aeropuerto,
            "Pais": a.Pais, 
            "Codigo_Pais": a.Codigo_Pais, 
            "Continente": a.Continente}
    data_aeropuertos = pd.concat([data_aeropuertos, pd.DataFrame([aeropuerto_dic])], ignore_index = True)
    ld.guardar_aeropuertos(data_aeropuertos)

# utilidad para códigos de país



def mostrar_codigos_paises():
    info = bp.obtener_codigos_paises()
    tabla = [[code, name] for code, name in info.items()]
    print(tabulate(tabla, headers=["Código", "País"], tablefmt="grid"))

def lista_codigos_paises():
    """Devuelve lista de abreviaturas de países disponibles."""
    return list(bp.obtener_codigos_paises().keys())

def verificar_continente(continente):
    continentes = ["America", "Asia", "Europa", "Africa"]
    for e in continentes:
        if e.lower() == continente.lower():
            return True
    return False

def registrar_aeropuerto ():
    # Validar ID: patrón AP + 3 dígitos (ej. AP001)
    while True:
        print("Formato de ID: AP...1")
        id_aeropuerto = input("Ingrese el ID del aeropuerto: ").strip().upper()
        if (len(id_aeropuerto) == 6
            and id_aeropuerto.startswith("AP")
            and id_aeropuerto[2:].isdigit()
            and not existe_aeropuerto(id_aeropuerto)
        ):
            break
        print("El ID del aeropuerto es inválido o ya existe")
    
    # Nombre sin números y no vacío
    while True:
        nombre_aeropuerto = input("Ingrese el nombre del aeropuerto: ").strip()
        if nombre_aeropuerto and not ps.contiene_numeros(nombre_aeropuerto):
            break
        print("El nombre no debe contener números ni estar vacío")
    
    # País sin números y no vacío
    while True:
        pais = input("Ingrese el país del aeropuerto: ").strip()
        if pais and not ps.contiene_numeros(pais):
            break
        print("El país no debe contener números ni estar vacío")
    
    # Resolver código de país (ISO2) a partir del nombre; si no existe, pedir manual
    codigo_pais = None
    paises = bp.obtener_codigos_paises()
    for clave, valor in paises.items():
        if valor.lower() == pais.lower():
            codigo_pais = clave
            break
    
    if codigo_pais is None:
        print("El país no está en el catálogo, ingrese el código manual (2 letras)")
        while True:
            cod = input("Código de país (ej. PE): ").strip().upper()
            if len(cod) == 2 or len(cod) == 3 and cod.isalpha():
                codigo_pais = cod
                break
            print("El código debe tener exactamente 2 letras")

    # Continente válido
    while True:
        continente = input("Ingrese el continente del aeropuerto: ").strip()
        if continente and not ps.contiene_numeros(continente) and verificar_continente(continente):
            break
        print("El continente no es válido")
    
    cont = a.Aeropuerto(id_aeropuerto, nombre_aeropuerto, codigo_pais, pais, continente)
    guardar_aeropuerto(cont)
    print()
    print("--"*30)
    print(f"Aeropuerto {nombre_aeropuerto} registrado correctamente")
    print("--"*30)
    print()

def mostrar_aeropuertos ():
    if data_aeropuertos.empty:
        print()
        print("--"*30)
        print("No hay aeropuertos registrados")
        print("--"*30)
        print()
        return
    else:
        cabezales = ["ID_Aeropuerto", "Nombre_Aeropuerto", "Pais", "Codigo_Pais", "Continente"]
        print(tabulate(data_aeropuertos, headers=cabezales, tablefmt="grid"))

def buscar_aeropuerto_por_id ():
    while True:
        try:
            print("Formato de ID: AP...1")
            id_aeropuerto = input("Ingrese el ID del aeropuerto a buscar: ").strip().upper()
            if (len(id_aeropuerto) == 6 and
                id_aeropuerto.startswith("AP") and  
                id_aeropuerto[2:].isdigit() and
                existe_aeropuerto(id_aeropuerto)):
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
    
    print("--"*30)
    for _, row in data_aeropuertos.iterrows():
        if row["ID_Aeropuerto"] == id_aeropuerto:
            print(row)
            break
    print("--"*30)
    print()


def buscar_aeropuerto_por_pais ():
    while True:
        try:
            pais = input("Ingrese el pais del aeropuerto a buscar: ").strip()
            if not ps.contiene_numeros(pais) and pais:
                break
            else:
                print("El pais no debe contener numeros y no puede estar vacío")
        except ValueError:
            print("Error en el ingreso de datos")

    # Filtrar aeropuertos por país (ignorando mayúsculas)
    resultados = data_aeropuertos[data_aeropuertos["Pais"].str.lower() == pais.lower()]

    if resultados.empty:
        print(f"No se encontraron aeropuertos en {pais}.")
    else:
        # Mostrar resultados en tabla
        tabla = resultados[["ID_Aeropuerto", "Nombre_Aeropuerto", "Codigo_Pais", "Continente"]]
        print(f"\nAeropuertos encontrados en {pais}:")
        print(tabulate(tabla, headers=["ID", "Nombre", "Código País", "Continente"], tablefmt="grid"))
    print()


def actualizar_aeropuerto ():
    while True:
        print()
        print("--"*30)
        print("Actualizar aeropuerto ... ")
        print("1. Actualizar nombre")
        print("2. Actualizar pais")
        print("3. Actualizar continente")
        print("4. Volver al menú principal")
        print("--"*30)
        print()
        
        while True:
            try:
                opcion = int(input("Ingrese una opción: "))
                if 1<= opcion <= 4:
                    break
                else:
                    print("La opción no es valida")
            except ValueError:
                print("Error en el ingreso de datos")
        
        if opcion == 4:
            break
        
        while True:
            try:
                print("Formato de ID: AP001")
                id_aeropuerto = input("Ingrese el ID del aeropuerto: ").upper()
                if (len(id_aeropuerto) == 6 and 
                    id_aeropuerto.startswith("AP")and 
                    id_aeropuerto[2:].isdigit() and 
                    existe_aeropuerto(id_aeropuerto)):
                    break
                
                else:
                    print("El ID del aeropuerto es invalido")
            except ValueError:
                print("Error en el ingreso de datos")

        if not existe_aeropuerto(id_aeropuerto):
            print("El aeropuerto no esta registrado")
            return 
        
        if opcion == 1:
            while True:
                try:
                    nombre_aeropuerto = input("Ingrese el nuevo nombre del aeropuerto: ")
                    if not ps.contiene_numeros(nombre_aeropuerto):
                        break 
                    else:
                        print("El nombre no debe contener numeros")
                except ValueError:
                    print("Error en el ingreso de datos")

            for _, row in data_aeropuertos.iterrows():
                if row["ID_Aeropuerto"] == id_aeropuerto:
                    data_aeropuertos.at[row.name, "Nombre_Aeropuerto"] = nombre_aeropuerto
                    ld.guardar_aeropuertos(data_aeropuertos)
                    break
                
            print("--"*30)
            print(f"Aeropuerto {id_aeropuerto} actualizado correctamente")
            print("--"*30)
            print()
        
        if opcion == 2:
            while True:
                try:
                    pais = input("Ingrese el pais del aeropuerto: ")
                    if not ps.contiene_numeros(pais):
                        break 
                    else:
                        print("El pais no debe contener numeros")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_aeropuertos.iterrows():
                if row["ID_Aeropuerto"] == id_aeropuerto:
                    data_aeropuertos.at[row.name, "Pais"] = pais
                    ld.guardar_aeropuertos(data_aeropuertos)
                    break
                
            print("--"*30)
            print(f"Aeropuerto {id_aeropuerto} actualizado correctamente")
            print("--"*30)
            print()
    
        if opcion == 3:
            while True:
                try:
                    continente = input("Ingrese el continente del aeropuerto: ")
                    if not ps.contiene_numeros(continente) and verificar_continente(continente):
                        break 
                    else:
                        print("El continente no es valido")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_aeropuertos.iterrows():
                if row["ID_Aeropuerto"] == id_aeropuerto:
                    data_aeropuertos.at[row.name, "Continente"] = continente
                    ld.guardar_aeropuertos(data_aeropuertos)
                    break
                        
            print("--"*30)
            print(f"Aeropuerto {id_aeropuerto} actualizado correctamente")
            print("--"*30)
            print()
    
            

def eliminar_aeropuerto ():
    while True:
        try:
            print("Formato de ID: AP001")
            id_aeropuerto = input("Ingrese el ID del aeropuerto: ").upper()
            if (len(id_aeropuerto) == 6 and 
                id_aeropuerto.startswith("AP") and 
                id_aeropuerto[2:].isdigit()
                and existe_aeropuerto(id_aeropuerto)): 
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")


    if not existe_aeropuerto(id_aeropuerto):
        print("El aeropuerto no esta registrado")
        return 
    
    for _, row in data_aeropuertos.iterrows():
        if row["ID_Aeropuerto"] == id_aeropuerto:
            data_aeropuertos.drop(row.name, inplace=True)
            ld.guardar_aeropuertos(data_aeropuertos)
            break
    
    print("--"*30)
    print(f"Aeropuerto {id_aeropuerto} eliminado correctamente")
    print("--"*30)
    print()
    
    
    # Notas 
    # Verificar que los codigos y paises se validen correctamente x 
    # Implementar la función actualizar x 
    
