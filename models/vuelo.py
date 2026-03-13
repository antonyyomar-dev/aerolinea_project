class Vuelo:
    def __init__(self, ID_Vuelo, Aeropuerto_Salida, Aeropuerto_Llegada,  Fecha_Salida, ID_Piloto, Estado_Vuelo):
        self.__ID_Vuelo = ID_Vuelo
        self.__Aeropuerto_Salida = Aeropuerto_Salida
        self.__Aeropuerto_Llegada = Aeropuerto_Llegada
        self.__Fecha_Salida = Fecha_Salida
        self.__ID_Piloto = ID_Piloto
        self.__Estado_Vuelo = Estado_Vuelo  
    
    @property
    def ID_Vuelo(self):
        return self.__ID_Vuelo
    @property
    def Aeropuerto_Salida(self):
        return self.__Aeropuerto_Salida
    @property
    def Aeropuerto_Llegada(self):
        return self.__Aeropuerto_Llegada
    @property
    def Fecha_Salida(self):
        return self.__Fecha_Salida 
    @property
    def ID_Piloto(self):
        return self.__ID_Piloto
    @property
    def Estado_Vuelo(self):
        return self.__Estado_Vuelo
    
    @ID_Vuelo.setter
    def ID_Vuelo(self, value):
        self.__ID_Vuelo = value

    @Aeropuerto_Salida.setter
    def Aeropuerto_Salida(self, value):
        self.__Aeropuerto_Salida = value

    @Aeropuerto_Llegada.setter
    def Aeropuerto_Llegada(self, value):
        self.__Aeropuerto_Llegada = value

    @Fecha_Salida.setter
    def Fecha_Salida(self, value):
        self.__Fecha_Salida = value

    @ID_Piloto.setter
    def ID_Piloto(self, value):
        self.__ID_Piloto = value

    @Estado_Vuelo.setter
    def Estado_Vuelo(self, value):
        self.__Estado_Vuelo = value

    def __str__(self):
        return f"ID Vuelo: {self.__ID_Vuelo} | Salida: {self.__Aeropuerto_Salida} | Llegada: {self.__Aeropuerto_Llegada} | Fecha: {self.__Fecha_Salida} | Piloto ID: {self.__ID_Piloto} | Estado: {self.__Estado_Vuelo}"
