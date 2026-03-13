class Piloto:
    def __init__(self, ID_Piloto, Nombre_Piloto, Nacionalidad, Anios_Experiencia):
        self.__ID_Piloto = ID_Piloto
        self.__Nombre_Piloto = Nombre_Piloto
        self.__Nacionalidad = Nacionalidad
        self.__Anios_Experiencia = Anios_Experiencia  
    
    @property
    def ID_Piloto(self):
        return self.__ID_Piloto
    @property
    def Nombre_Piloto(self):
        return self.__Nombre_Piloto
    @property
    def Nacionalidad(self):
        return self.__Nacionalidad
    @property
    def Anios_Experiencia(self):
        return self.__Anios_Experiencia
    
    @ID_Piloto.setter
    def ID_Piloto(self, value):
        self.__ID_Piloto = value

    @Nombre_Piloto.setter
    def Nombre_Piloto(self, value):
        self.__Nombre_Piloto = value

    @Nacionalidad.setter
    def Nacionalidad(self, value):
        self.__Nacionalidad = value

    @Anios_Experiencia.setter
    def Anios_Experiencia(self, value):
        self.__Anios_Experiencia = value
    
    def __str__(self):
        return f"ID: {self.__ID_Piloto} | Nombre: {self.__Nombre_Piloto} | Nacionalidad: {self.__Nacionalidad} | Años de Experiencia: {self.__Anios_Experiencia}"

