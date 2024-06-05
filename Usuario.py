class Usuario:
    def __init__(self, nombre : str, apellido : str, mail : str, password : str, telefono=None , verificacion=None):
        self.id_usuario = None #lo define la DB y es auto incremental
        self.name = [nombre, apellido]
        self.__mail = mail
        self.__password = password
        self.__telefono = telefono
        self.verificacion = verificacion
    
    def set_password(self, new_password : str):
        self.__password = new_password
    
    def get_password(self):
            return self.__password
    
    def set_mail(self, new_mail : str):
        self.__mail = new_mail
    
    def get_mail(self):
            return self.__mail
    
    def set_telefono(self, new_telefono : str):
        self.__telefono = new_telefono
    
    def get_telefono(self):
            return self.__telefono
    
    def __str__(self) -> str:
        pantalla = f'nombre : {self.name}, mail : {self.get_mail()}, telefono : {self.get_telefono()}'
        return pantalla