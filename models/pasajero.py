class Pasajero:
    def __init__(self, ID_Pasajero, Nombre, Apellido, Genero, Edad, Nacionalidad):
        self.__ID_Pasajero = ID_Pasajero
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Genero = Genero
        self.__Edad = Edad
        self.__Nacionalidad = Nacionalidad
        
    @property
    def ID_Pasajero(self):
        return self.__ID_Pasajero
    @property
    def Nombre(self):
        return self.__Nombre
    @property
    def Apellido(self):
        return self.__Apellido
    @property
    def Genero(self):
        return self.__Genero
    @property
    def Edad(self):
        return self.__Edad
    @property
    def Nacionalidad(self):
        return self.__Nacionalidad
    
    @ID_Pasajero.setter
    def ID_Pasajero(self, value):
        self.__ID_Pasajero = value

    @Nombre.setter
    def Nombre(self, value):
        self.__Nombre = value

    @Apellido.setter
    def Apellido(self, value):
        self.__Apellido = value

    @Genero.setter
    def Genero(self, value):
        self.__Genero = value

    @Edad.setter
    def Edad(self, value):
        self.__Edad = value

    @Nacionalidad.setter
    def Nacionalidad(self, value):
        self.__Nacionalidad = value

    def __str__(self):
        return f"ID: {self.__ID_Pasajero} | Nombre: {self.__Nombre} {self.__Apellido} | Género: {self.__Genero} | Edad: {self.__Edad} | Nacionalidad: {self.__Nacionalidad}"
