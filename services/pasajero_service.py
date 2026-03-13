from models import pasajero as  p 
from data import logica_data as ld 
import pandas as pd 
from tabulate import tabulate

# Carga de data
data_pasajeros = ld.cargar_pasajeros()

# Métodos

def existe_pasajero(id_pasajero):
    for _, row in data_pasajeros.iterrows():
        if row["ID_Pasajero"] == id_pasajero:
            return True
    return False

def contiene_numeros (nombre):
    for caracter in nombre:
        if caracter.isdigit():
            return True
    return False

def guardar_pasajero(p):
    global data_pasajeros
    pasajero_dict = {"ID_Pasajero": p.ID_Pasajero, 
            "Nombre": p.Nombre,
            "Apellido": p.Apellido, 
            "Genero": p.Genero, 
            "Edad": p.Edad,
            "Nacionalidad": p.Nacionalidad}
    data_pasajeros = pd.concat([data_pasajeros, pd.DataFrame([pasajero_dict])], ignore_index=True)
    ld.guardar_pasajeros(data_pasajeros)

    # data_pasajeros es el archivo global
    # convertimos el pasajero_dic a un DataFrame para poder unir 
    # ignore_index = True reorganizamos los indices
    


def registrar_pasajero ():
    while True:
        try:
            print("Formato de ID: P001")
            id_pasajero = input("Ingrese el ID del pasajero: ")
            if id_pasajero.startswith("P00") and not existe_pasajero(id_pasajero):
                break 
            else:
                print("El ID del pasajero es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
            
    while True:
        try:
            nombre = input("Ingrese el nombre del pasajero: ")
            if not contiene_numeros(nombre):
                break
            else:
                print("El nombre no debe de contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")

    while True:
        try:
            apellido = input("Ingrese el apellido del pasajero: ")
            if not contiene_numeros(apellido):
                break
            else:  
                print("El apellido no debe de tener numeros")
        except ValueError:
            print("Error en el ingreso de datos")


    while True:
        try:
            genero = input("Ingrese el genero del pasajero (M/F): ").upper()
            if genero in ["M", "F"]:
                if genero == "M":
                    genero = "Masculino"
                else:
                    genero = "Femenino"
                break 
            else:
                print("El genero del pasajero no es correcto")
        except ValueError:
            print("Error en el ingreso de datos")

    while True:
        try:
            edad = int(input("Ingrese la edad del pasajero: "))
            if edad > 0:
                break
            else:
                print("La edad del pasajero no es valida")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            nacionalidad = input("Ingrese la nacionalidad del pasajero: ")
            if not contiene_numeros(nacionalidad):
                break
            else:
                print("La nacionalidad es invalidad")
        except ValueError:
            print("Error en el ingreso de datos")
    
    pasajero = p.Pasajero(id_pasajero, nombre, apellido, genero, edad, nacionalidad)
    guardar_pasajero(pasajero)
    print("--"*30)
    print(f"Pasajero {nombre} {apellido} registrado correctamente")
    print("--"*30)
    print()
    

def mostrar_pasajeros ():
    cabezales = ["ID_Pasajero", "Nombre", "Apellido", "Genero", "Edad", "Nacionalidad"]
    print(tabulate(data_pasajeros, headers=cabezales, tablefmt="grid"))
          
def buscar_pasajero_por_id ():
    while True:
        try:
            print("Formato de ID: P001")
            id_pasajero = input("Ingrese el ID del pasajero: ")
            if id_pasajero.startswith("P00") and  existe_pasajero(id_pasajero):
                break 
            else:
                print("El ID del pasajero es invalido")
        except ValueError:
            print("Error en el ingreso de datos")

    print("--"*30)
    for _, row in data_pasajeros.iterrows():
        if row["ID_Pasajero"] == id_pasajero:
            print(row)
            break
    print("--"*30)
    print()

def buscar_pasajero_por_nombre ():
    while True:
        try:
            nombre = input("Ingrese el nombre del pasajero: ")
            if not contiene_numeros(nombre):
                break
            else:
                print("El nombre no debe de contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")

    print("--"*30)
    for _, row in data_pasajeros.iterrows():
        if row["Nombre"] == nombre:
            print(row)
    print("--"*30)
    print()

def actualizar_pasajero ():
    
    while True:
        print()
        print("--"*30)
        print("Actualizar pasajero ... ")
        print("1. Actualizar nombre")
        print("2. Actualizar apellido")
        print("3. Actualizar genero")
        print("4. Actualizar edad")
        print("5. Actualizar nacionalidad")
        print("6. Volver al menú principal")
        print("--"*30)
        print()
        while True:
            try:
                opcion = int(input("Ingrese una opción: "))
                if 1<= opcion <= 6:
                    break
                else:
                    print("La opción no es valida")
            except ValueError:
                print("Error en el ingreso de datos")
        
        
        if opcion == 6:
            break
        
        while True:
            try:
                print("Formato de ID: P001")
                id_pasajero = input("Ingrese el ID del pasajero: ")
                if id_pasajero.startswith("P00"):
                    break 
                else:
                    print("El ID del pasajero es invalido")
            except ValueError:
                print("Error en el ingreso de datos")
                
        if not  existe_pasajero(id_pasajero):
            print("El pasajero no esta registrado")
            return 
        
        if opcion == 1:
            while True:
                try:
                    nombre = input("Ingrese el nuevo nombre del pasajero: ")
                    if not contiene_numeros(nombre):
                        break
                    else:
                        print("El nombre no debe de contener numeros")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _,row in data_pasajeros.iterrows():
                if row["ID_Pasajero"] == id_pasajero:
                    data_pasajeros.loc[row.name, "Nombre"] = nombre
                    ld.guardar_pasajeros(data_pasajeros)
            
            print("--"*30)
            print(f"Pasajero {id_pasajero} actualizado correctamente")
            print("--"*30)
            print()
    
        if opcion == 2:      
            while True:
                try:
                    apellido = input("Ingrese el nuevo apellido del pasajero: ")
                    if not contiene_numeros(apellido):
                        break
                    else:  
                        print("El apellido no debe de tener numeros")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_pasajeros.iterrows():
                if row["ID_Pasajero"] == id_pasajero:
                    data_pasajeros.loc[row.name, "Apellido"] = apellido
                    ld.guardar_pasajeros(data_pasajeros)
            
            print("--"*30)
            print(f"Pasajero {id_pasajero} actualizado correctamente")
            print("--"*30)
            print()

        if opcion == 3:
            while True:
                try:
                    genero = input("Ingrese el nuevo genero del pasajero (M/F): ").upper()
                    if genero in ["M", "F"]:
                        if genero == "M":
                            genero = "Masculino"
                        else:
                            genero = "Femenino"
                        break 
                    else:
                        print("El genero del pasajero no es correcto")
                except ValueError:
                    print("Error en el ingreso de datos")

            for _, row in data_pasajeros.iterrows():
                if row["ID_Pasajero"] == id_pasajero:
                    data_pasajeros.loc[row.name, "Genero"] = genero
                    ld.guardar_pasajeros(data_pasajeros)
                    
            print("--"*30)
            print(f"Pasajero {id_pasajero} actualizado correctamente")
            print("--"*30)
            print()
            
        if opcion == 4:
            while True:
                try:
                    edad = int(input("Ingrese la nueva edad del pasajero: "))
                    if edad > 0:
                        break
                    else:
                        print("La edad del pasajero no es valida")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_pasajeros.iterrows():
                if row["ID_Pasajero"] == id_pasajero:
                    data_pasajeros.loc[row.name,"Edad"] = edad
                    ld.guardar_pasajeros(data_pasajeros)
                    
            print("--"*30)
            print(f"Pasajero {id_pasajero} actualizado correctamente")
            print("--"*30)
            print()

        if opcion == 5:
            while True:
                try:
                    nacionalidad = input("Ingrese la nueva nacionalidad del pasajero: ")
                    if not contiene_numeros(nacionalidad):
                        break
                    else:
                        print("La nacionalidad es invalidad")
                except ValueError:
                    print("Error en el ingreso de datos")
            
            for _, row in data_pasajeros.iterrows():
                if row["ID_Pasajero"] == id_pasajero:
                    data_pasajeros.loc[row.name, "Nacionalidad"] = nacionalidad
                    ld.guardar_pasajeros(data_pasajeros)
                    
            print("--"*30)
            print(f"Pasajero {id_pasajero} actualizado correctamente")
            print("--"*30)
            print()
        

def eliminar_pasajero ():
    while True:
        try:
            print("Formato de ID: P001")
            id_pasajero = input("Ingrese el ID del pasajero a eliminar: ")
            if id_pasajero.startswith("P00"):
                break 
            else:
                print("El ID del pasajero es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
                
    if not  existe_pasajero(id_pasajero):
        print("El pasajero no esta registrado")
        return
    
    for _, row in data_pasajeros.iterrows():
        if row["ID_Pasajero"] == id_pasajero:
            data_pasajeros.drop(row.name, inplace=True)
            ld.guardar_pasajeros(data_pasajeros)
            break
        