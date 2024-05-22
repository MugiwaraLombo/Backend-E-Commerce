class Usuario():
    def __init__(self, nombre, apellido, mail, password, telefono=None , verificacion=None):
        self.id_usuario = "lo define la DB" #es auto incremental
        self.name = [nombre, apellido]
        self.mail = mail
        self.__password = password
        self.telefono = telefono
        self.verificacion = verificacion
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def get_password(self):
            return self.__password