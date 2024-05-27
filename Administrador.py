class Administrador:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.__password = password

    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password

    def __str__(self):
        info = "nombre="+self.nombre+", correo="+self.correo
        return info