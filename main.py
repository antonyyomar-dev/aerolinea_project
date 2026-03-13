from models import  menus as m
from services import pasajero_service as ps
from services import aeropuerto_service as a
from services import piloto_service as p
from services import vuelo_service as v
from services import reportes_service as r
import os 

def limpiar_pantalla():
    os.system("cls")

def main():
    while True:
        while True:
            try:
                m.menu_principal()
                opcion = int(input("Seleccione una opción: "))
                if 1<= opcion <= 7:
                    break 
                else:
                    print("Opcion no valida")
            except ValueError:
                print("Error en el ingreso de datos")

        if opcion == 6:
            print("Saliendo del sistema......")
            break
        
        if opcion == 1:
            limpiar_pantalla()
            while True:
                while True:
                    try:
                        m.menu_pasajeros()
                        opcion = int(input("Seleccione una opción: "))
                        if 1<= opcion <= 7:
                            break 
                        else:
                            print("Opcion invalida")
                    except ValueError:
                        print("Error en el ingreso de datos")
            
                if opcion == 7:
                    break
                if opcion == 1:
                    ps.registrar_pasajero()
                if opcion == 2:
                    ps.mostrar_pasajeros()
                if opcion == 3:
                    ps.buscar_pasajero_por_id()
                if opcion == 4:
                    ps.buscar_pasajero_por_nombre()
                if opcion == 5:
                    ps.actualizar_pasajero()
                if opcion == 6:
                    ps.eliminar_pasajero()
            
        
        if opcion == 2:
            limpiar_pantalla()
            while True:
                while True:
                    try:
                        m.menu_aeropuertos()
                        opcion = int(input("Seleccione una opción: "))
                        if 1<= opcion <= 7:
                            break 
                        else:
                            print("Opcion invalida")
                    except ValueError:
                        print("Error en ek ingreso de datos")
                
                if opcion == 7:
                    break
                if opcion == 1:
                    a.registrar_aeropuerto()
                if opcion == 2:
                    a.mostrar_aeropuertos()
                if opcion == 3:
                    a.buscar_aeropuerto_por_id()
                if opcion == 4:
                    a.buscar_aeropuerto_por_pais()
                if opcion == 5:
                    a.actualizar_aeropuerto()
                if opcion == 6:
                    a.eliminar_aeropuerto()
        
        if opcion == 3:
            limpiar_pantalla()
            while True:
                while True:
                    try:
                        m.menu_pilotos()
                        opcion = int(input("Seleccione una opción: "))
                        if 1<= opcion <= 7:
                            break 
                        else:
                            print("Opcion invalida")
                    except ValueError:
                        print("Error en ek ingreso de datos")
                
                if opcion == 7:
                    break
                if opcion == 1:
                    pass
                if opcion == 2:
                    pass
                if opcion == 3:
                    pass
                if opcion == 4:
                    pass
                if opcion == 5:
                    pass
                if opcion == 6:
                    pass
        
        if opcion == 4:
            limpiar_pantalla()
            while True:
                while True:
                    try:
                        m.menu_vuelos()
                        opcion = int(input("Seleccione una opción: "))
                        if 1<= opcion <= 8:
                            break 
                        else:
                            print("Opcion invalida")
                    except ValueError:
                        print("Error en ek ingreso de datos")
                
                if opcion == 8:
                    break
                if opcion == 1:
                    pass
                if opcion == 2:
                    pass
                if opcion == 3:
                    pass
                if opcion == 4:
                    pass
                if opcion == 5:
                    pass
                if opcion == 6:
                    pass
                if opcion == 7:
                    pass
        
        if opcion == 5:
            limpiar_pantalla()
            while True:
                while True:
                    try:
                        m.menu_reportes()
                        opcion = int(input("Seleccione una opción: "))
                        if 1<= opcion <= 7:
                            break 
                        else:
                            print("Opcion invalida")
                    except ValueError:
                        print("Error en ek ingreso de datos")
                
                if opcion == 7:
                    break
                if opcion == 1:
                    pass
                if opcion == 2:
                    pass
                if opcion == 3:
                    pass
                if opcion == 4:
                    pass
                if opcion == 5:
                    pass
                if opcion == 6:
                    pass
    

if __name__ == "__main__":
    main()
    