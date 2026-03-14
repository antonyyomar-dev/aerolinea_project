from models import piloto as pi
from data import logica_data as ld
from tabulate import tabulate
import pandas as pd
from services import pasajero_service as ps
from data import base_paises as bp




# Carga de data
data_pilotos = ld.cargar_pilotos()

# Métodos
def existe_piloto(id_piloto):
    for _, row in data_pilotos.iterrows():
        if row["ID_Piloto"] == id_piloto:
            return True
    return False

def guardar_piloto(p):
    global data_pilotos
    piloto_dic = {
        "ID_Piloto": p.ID_Piloto, 
        "Nombre_Piloto": p.Nombre_Piloto,
        "Nacionalidad": p.Nacionalidad, 
        "Anios_Experiencia": p.Anios_Experiencia
    }
    
    data_pilotos = pd.concat([data_pilotos, pd.DataFrame([piloto_dic])], ignore_index= True)
    ld.guardar_pilotos(data_pilotos)

    
def registrar_piloto ():
    while True:
        try:
            id_piloto = input("Ingrese el ID del piloto: ").strip().upper()
            if id_piloto.startswith("PL") and not existe_piloto(id_piloto):
                break 
            else:
                print("El ID del piloto es invalido o ya esta registrado")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            nombre = input("Ingrese el nombre completo del piloto: ").capitalize()
            if not ps.contiene_numeros(nombre):
                break
            else:
                print("El nombre no debe de contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            nacionalidad = input("Ingrese la nacionalidad del piloto: ").title()
            if not ps.contiene_numeros(nacionalidad) and bp.obtener_nombre_paises(nacionalidad):
                break
            else:
                print("La nacionalidad es invalida")
        except ValueError:
            print("Error en el ingreso de datos")

    while True:
        try:
            anios_experiencia = int(input("Ingrese los años de experiencia del piloto: "))
            if anios_experiencia > 0:
                break
            else:
                print("Los años de experiencia no son validos")
        except ValueError:
            print("Error en el ingreso de datos")
    
    piloto = pi.Piloto(id_piloto, nombre, nacionalidad, anios_experiencia)
    guardar_piloto(piloto)
    print("--"*30)
    print(f"Piloto {nombre} registrado correctamente")
    print("--"*30)
    print()
    
def mostrar_pilotos ():
    if data_pilotos.empty:
        print()
        print("--"*30)
        print("No hay pilotos registrados")
        print("--"*30)
        print()
        return
    else:
        cabezales = ["ID_Piloto", "Nombre_Piloto", "Nacionalidad", "Anios_Experiencia"]
        print(tabulate(data_pilotos, headers = cabezales, tablefmt = "grid"))
        

def buscar_piloto_por_id ():
    while True:
        try:
            id_piloto = input("Ingrese el ID del piloto a buscar: ").strip().upper()
            if id_piloto.startswith("PL"):
                break 
            else:
                print("El ID del piloto es invalido o ya esta registrado")
        except ValueError:
            print("Error en el ingreso de datos")
    
    if not existe_piloto(id_piloto):
        print("El piloto no esta registrado")
        return 

    print()
    print("Piloto encontrado ...... Cargando información ...")
    print("--"*30)
    for _, row in data_pilotos.iterrows():
        if row["ID_Piloto"] == id_piloto:
            print(row)
            break
    print("--"*30)
    print()


def buscar_piloto_por_nombre ():
    while True:
        try:
            nombre = input("Ingrese el nombre completo del piloto a buscar: ").capitalize()
            if not ps.contiene_numeros(nombre):
                break
            else:
                print("El nombre no debe de contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")
        
    encontrado = None
    for _, row in data_pilotos.iterrows():
        if row["Nombre_Piloto"] == nombre:
            encontrado = row
            break
    
    if encontrado is None:
        print("Piloto no encontrado")
    else:
        print("--"*30)
        print(encontrado)
        print("--"*30)
    print()
    
    
def actualizar_piloto ():
    while True:
        print()
        print("--"*30)
        print("Actualizar piloto ... ")
        print("1. Actualizar nombre")
        print("2. Actualizar nacionalidad")
        print("3. Actualizar años de experiencia")
        print("4. Volver al menú principal")
        print("--"*30)
        print()
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if 1<= opcion <= 4:
                    break 
                else:
                    print("La opción esta fuera de rango")
            except ValueError:
                print("Error en el ingreso de datos")
        
        if opcion == 4:
            break 
                
        while True:
            try:
                id_piloto = input("Ingrese el ID del piloto a buscar: ").strip().upper()
                if id_piloto.startswith("PL"):
                    break 
                else:
                    print("El ID del piloto es invalido o ya esta registrado")
            except ValueError:
                print("Error en el ingreso de datos")
        
        if not existe_piloto(id_piloto):
            print("El piloto no esta registrado")
            return 
            
        if opcion == 1:
            while True:
                try:
                    nombre = input("Ingrese el nuevo nombre completo del piloto a buscar: ").capitalize()
                    if not ps.contiene_numeros(nombre):
                        break
                    else:
                        print("El nombre no debe de contener numeros")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_pilotos.iterrows():
                if row["ID_Piloto"] == id_piloto:
                    data_pilotos.loc[row.name, "Nombre_Piloto"] = nombre
                    ld.guardar_pilotos(data_pilotos)
                    break
            
            print("--"*30)
            print(f"Piloto {id_piloto} actualizado correctamente")
            print("--"*30)
            print()

        if opcion == 2:
            while True:
                try:
                    nacionalidad = input("Ingrese la nueva nacionalidad del piloto: ").title()
                    if not ps.contiene_numeros(nacionalidad) and bp.obtener_nombre_paises(nacionalidad):
                        break
                    else:
                        print("La nacionalidad es invalida")
                except ValueError:
                    print("Error en el ingreso de datos")
            for _, row in data_pilotos.iterrows():
                if row["ID_Pilotos"] == id_piloto:
                    data_pilotos.loc[row.name, "Nacionalidad"] = nacionalidad
                    ld.guardar_pilotos(data_pilotos)
                    break
            print("--"*30)
            print(f"Piloto {id_piloto} actualizado correctamente")
            print("--"*30)
            print()

        if opcion == 3:
            while True:
                try:
                    anios_experiencia = int(input("Ingrese los nuevos años de experiencia del piloto: "))
                    if anios_experiencia > 0:
                        break
                    else:
                        print("Los años de experiencia no son validos")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_pilotos.iterrows():
                if row["ID_Piloto"] == id_piloto:
                    data_pilotos.loc[row.name , "Anios_Experiencia"] = anios_experiencia
                    ld.guardar_pilotos(data_pilotos)
                    break
            

def eliminar_piloto ():
    while True:
        try:
            id_piloto = input("Ingrese el ID del piloto: ").strip().upper()
            if id_piloto.startswith("PL"):
                break 
            else:
                print("El ID del piloto es invalido o ya esta registrado")
        except ValueError:
            print("Error en el ingreso de datos")
    
    if not existe_piloto(id_piloto):
        print("El piloto no esta registrado")
        return 
    
    for _, row in data_pilotos.iterrows():
        if row["ID_Piloto"] == id_piloto:
            data_pilotos.drop(row.name, inplace=True)
            ld.guardar_pilotos(data_pilotos)
            break 
        
    print("--"*30)
    print(f"Piloto {id_piloto} eliminado correctamente")
    print("--"*30)
    print()
    
    