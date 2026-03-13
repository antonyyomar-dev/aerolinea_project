from models import aeropuerto as a 
from data import logica_data as ld 
from tabulate import tabulate
import pandas as pd
from services import pasajero_service as ps

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

def obtener_codigos_paises():
    """Devuelve diccionario {abreviatura: nombre} con países de LATAM, ASIA y EUROPA."""
    return {
        # Latinoamérica
        "AR": "Argentina", "BO": "Bolivia", "BR": "Brasil", "CL": "Chile",
        "CO": "Colombia", "CR": "Costa Rica", "CU": "Cuba", "DO": "República Dominicana",
        "EC": "Ecuador", "SV": "El Salvador", "GT": "Guatemala", "HN": "Honduras",
        "MX": "México", "NI": "Nicaragua", "PA": "Panamá", "PY": "Paraguay",
        "PE": "Perú", "PR": "Puerto Rico", "UY": "Uruguay", "VE": "Venezuela",
        # Asia
        "AF": "Afganistán", "AM": "Armenia", "AZ": "Azerbaiyán", "BH": "Baréin",
        "BD": "Bangladesh", "BT": "Bután", "BN": "Brunéi", "KH": "Camboya",
        "CN": "China", "CY": "Chipre", "GE": "Georgia", "IN": "India",
        "ID": "Indonesia", "IR": "Irán", "IQ": "Irak", "IL": "Israel",
        "JP": "Japón", "JO": "Jordania", "KZ": "Kazajistán", "KW": "Kuwait",
        "KG": "Kirguistán", "LA": "Laos", "LB": "Líbano", "MY": "Malasia",
        "MV": "Maldivas", "MN": "Mongolia", "MM": "Myanmar", "NP": "Nepal",
        "KP": "Corea del Norte", "KR": "Corea del Sur", "OM": "Omán", "PK": "Pakistán",
        "PS": "Palestina", "PH": "Filipinas", "QA": "Qatar", "SA": "Arabia Saudita",
        "SG": "Singapur", "LK": "Sri Lanka", "SY": "Siria", "TJ": "Tayikistán",
        "TH": "Tailandia", "TL": "Timor Oriental", "TR": "Turquía", "TM": "Turkmenistán",
        "AE": "Emiratos Árabes Unidos", "UZ": "Uzbekistán", "VN": "Vietnam", "YE": "Yemen",
        # Europa
        "AL": "Albania", "AD": "Andorra", "AT": "Austria", "BY": "Bielorrusia",
        "BE": "Bélgica", "BA": "Bosnia y Herzegovina", "BG": "Bulgaria", "HR": "Croacia",
        "CZ": "Chequia", "DK": "Dinamarca", "EE": "Estonia", "FI": "Finlandia",
        "FR": "Francia", "DE": "Alemania", "GR": "Grecia", "HU": "Hungría",
        "IS": "Islandia", "IE": "Irlanda", "IT": "Italia", "LV": "Letonia",
        "LI": "Liechtenstein", "LT": "Lituania", "LU": "Luxemburgo", "MT": "Malta",
        "MD": "Moldavia", "MC": "Mónaco", "ME": "Montenegro", "NL": "Países Bajos",
        "MK": "Macedonia del Norte", "NO": "Noruega", "PL": "Polonia", "PT": "Portugal",
        "RO": "Rumanía", "RU": "Rusia", "SM": "San Marino", "RS": "Serbia",
        "SK": "Eslovaquia", "SI": "Eslovenia", "ES": "España", "SE": "Suecia",
        "CH": "Suiza", "UA": "Ucrania", "GB": "Reino Unido", "VA": "Ciudad del Vaticano"
    }


def mostrar_codigos_paises():
    info = obtener_codigos_paises()
    tabla = [[code, name] for code, name in info.items()]
    print(tabulate(tabla, headers=["Código", "País"], tablefmt="grid"))

def lista_codigos_paises():
    """Devuelve lista de abreviaturas de países disponibles."""
    return list(obtener_codigos_paises().keys())

def verificar_continente(continente):
    continentes = ["America", "Asia", "Europa", "Africa"]
    for e in continentes:
        if e.lower() == continente.lower():
            return True
    return False

def registrar_aeropuerto ():
    while True:
        try:
            print("Formato de ID: AP001")
            id_aeropuerto = input("Ingrese el ID del aeropuerto: ").upper()
            if id_aeropuerto.startswith("AP00") and not existe_aeropuerto(id_aeropuerto):
                break
            else:
                print("El ID del aeropuerto es invalido")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            nombre_aeropuerto = input("Ingrese el nombre del aeropuerto: ")
            if not ps.contiene_numeros(nombre_aeropuerto):
                break 
            else:
                print("El nombre no debe contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")
    
    while True:
        try:
            pais = input("Ingrese el pais del aeropuerto: ")
            if not ps.contiene_numeros(pais):
                break 
            else:
                print("El pais no debe contener numeros")
        except ValueError:
            print("Error en el ingreso de datos")
    
    
    
    # obtener solo las abreviaturas
    for clave, valor in obtener_codigos_paises().items():
        if valor == pais:
            codigo_pais = clave
            break
        else:
            print("El pais no es valido")
            while True:
                cod = input("Ingrese el codigo de forma manual (3 Caracteres): ")
                if  len(cod) == 3:
                    codigo_pais = cod
                    break 
                else:
                    print("El codigo no debe ser de 3 caracteres")
    
            break 
    
    while True:
        try:
            continente = input("Ingrese el continente del aeropuerto: ")
            if not ps.contiene_numeros(continente) and verificar_continente(continente):
                break 
            else:
                print("El continente no es valido")
        except ValueError:
            print("Error en el ingreso de datos")
    
    cont = a.Aeropuerto(id_aeropuerto, nombre_aeropuerto, codigo_pais, pais, continente)
    guardar_aeropuerto(cont)
    print()
    print("--"*30)
    print(f"Aeropuerto {nombre_aeropuerto} registrado correctamente")
    print("--"*30)
    print()
    

def mostrar_aeropuertos ():
    cabezales = ["ID_Aeropuerto", "Nombre_Aeropuerto", "Pais", "Codigo_Pais", "Continente"]
    print(tabulate(data_aeropuertos, headers=cabezales, tablefmt="grid"))

def buscar_aeropuerto_por_id ():
    while True:
        try:
            print("Formato de ID: AP001")
            id_aeropuerto = input("Ingrese el ID del aeropuerto a buscar: ").upper()
            if id_aeropuerto.startswith("AP00") and  existe_aeropuerto(id_aeropuerto):
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
    pass 

def eliminar_aeropuerto ():
    while True:
        try:
            print("Formato de ID: AP001")
            id_aeropuerto = input("Ingrese el ID del aeropuerto: ").upper()
            if id_aeropuerto.startswith("AP00"): 
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
    # Verificar que los codigos y paises se validen correctamente 
    # Implementar la función actualizar
    