class Administrador():
    def __init__(self, nombre, correo, rol="Administrador"):
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def asignar_rol(self, nuevo_rol):
        self.rol = nuevo_rol

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Rol: {self.rol}")

admin1 = Administrador(nombre="", correo="")
admin1.mostrar_informacion()  
admin1.asignar_rol("Superadministrador")
admin1.mostrar_informacion() 