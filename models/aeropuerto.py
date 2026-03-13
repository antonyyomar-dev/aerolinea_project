class Aeropuerto:
    def __init__(self, ID_Aeropuerto, Nombre_Aeropuerto, Codigo_Pais, Pais, Continente):
        self.__ID_Aeropuerto = ID_Aeropuerto
        self.__Nombre_Aeropuerto = Nombre_Aeropuerto
        self.__Pais = Pais
        self.__Codigo_Pais = Codigo_Pais
        self.__Continente = Continente
    
    @property
    def ID_Aeropuerto(self):
        return self.__ID_Aeropuerto
    @property
    def Nombre_Aeropuerto(self):
        return self.__Nombre_Aeropuerto
    @property
    def Codigo_Pais(self):
        return self.__Codigo_Pais
    @property
    def Pais(self):
        return self.__Pais
    @property
    def Continente(self):
        return self.__Continente
    
    @ID_Aeropuerto.setter
    def ID_Aeropuerto(self, value):
        self.__ID_Aeropuerto = value

    @Nombre_Aeropuerto.setter
    def Nombre_Aeropuerto(self, value):
        self.__Nombre_Aeropuerto = value

    @Codigo_Pais.setter
    def Codigo_Pais(self, value):
        self.__Codigo_Pais = value

    @Pais.setter
    def Pais(self, value):
        self.__Pais = value

    @Continente.setter
    def Continente(self, value):
        self.__Continente = value
    
    def __str__(self):
        return f"ID: {self.__ID_Aeropuerto} | Nombre: {self.__Nombre_Aeropuerto} | Código de País: {self.__Codigo_Pais} | País: {self.__Pais} | Continente: {self.__Continente}"