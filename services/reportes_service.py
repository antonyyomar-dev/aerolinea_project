from services import pasajero_service as ps
from services import aeropuerto_service as a
from services import piloto_service as p
from services import vuelo_service as v
from tabulate import tabulate 
import pandas as pd
from data import logica_data as ld
import matplotlib.pyplot as plt 


def total_pasaheros_registrados ():
    print()
    print("--"*30)
    print(f"Total de pasajeros registrados: {len(ps.data_pasajeros)}")
    print("--"*30)
    print()

def total_pilotos ():
    print()
    print("--"*30)
    print(f"Total de pilotos registrados: {len(p.data_pilotos)}")
    print("--"*30)
    print()

def total_aeropuertos ():
    print()
    print("--"*30)
    print(f"Total de aeropuertos registrados: {len(a.data_aeropuertos)}")
    print("--"*30)
    print()

def total_vuelos ():
    print()
    print("--"*30)
    print(f"Total de vuelos registrados: {len(v.data_vuelos)}")
    print("--"*30)
    print()


def reporte_vuelos_por_estado ():
    print()
    print("--"*30)
    print("Reporte de vuelos por estado")
    print("--"*30)
    print()
    
    data_vuelos = ld.cargar_vuelos() 
    filtro = data_vuelos.groupby("Estado_Vuelo").size()
    data = pd.DataFrame(filtro)
    data.columns = ["Cantidad"]
    print(data)
    print()
    
    # grafico de lineas
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data["Cantidad"], marker="o")
    plt.title("Cantidad de vuelos por estado")
    plt.xlabel("Estado del vuelo")
    plt.ylabel("Cantidad")
    plt.grid(True)
    plt.show()


def reporte_vuelos_por_pais ():
    print()
    print("--"*30)
    print("Reporte de vuelos por país")
    print("--"*30)
    print()
    data_vuelos = ld.cargar_vuelos()
    data_aeropuertos = ld.cargar_aeropuertos()
    merged_data = pd.merge(data_vuelos, data_aeropuertos, left_on="Aeropuerto_Salida", right_on="ID_Aeropuerto")
    filtro = merged_data.groupby("Pais").size()
    data = pd.DataFrame(filtro)
    data.columns = ["Cantidad"]
    
    print(data)
    print()
    # grafico de barras
    plt.figure(figsize=(10,6))
    plt.bar(data.index, data["Cantidad"])
    plt.title("Cantidad de vuelos por país")
    plt.xlabel("País")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.show()




