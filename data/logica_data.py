import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "data.xlsx"

def cargar_pasajeros():
    df = pd.read_excel(DATA_FILE, sheet_name="pasajeros")   # o la hoja que corresponda
    return df
def cargar_aeropuertos():
    df = pd.read_excel(DATA_FILE, sheet_name="aeropuertos")
    return df
def cargar_pilotos():
    df = pd.read_excel(DATA_FILE, sheet_name="pilotos")
    return df
def cargar_vuelos():
    df = pd.read_excel(DATA_FILE, sheet_name="vuelos")
    return df


def guardar_pasajeros(df):
    with pd.ExcelWriter(DATA_FILE, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="pasajeros", index=False)
        
def guardar_aeropuertos(df):
    with pd.ExcelWriter(DATA_FILE, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="aeropuertos", index=False) 

def guardar_pilotos(df):
    with pd.ExcelWriter(DATA_FILE, mode = 'a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="pilotos", index=False)  

def guardar_vuelos(df):
    with pd.ExcelWriter(DATA_FILE, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="vuelos", index=False)  

