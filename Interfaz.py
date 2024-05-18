# Interfaz para interactuar con la base de datos
class BaseDeDatos():
    def guardar_usuario(self, usuario):
        pass

    def obtener_usuario_por_email(self, email):
        pass

    def guardar_producto(self, producto):
        pass

    def obtener_productos(self):
        pass

# Implementación de la base de datos usando Amazon DynamoDB y JSON
class DynamoDB(BaseDeDatos):
    def guardar_usuario(self, usuario):
        # guardar un usuario en DynamoDB en formato JSON
        pass

    def obtener_usuario_por_email(self, email):
        # obtener un usuario por email desde DynamoDB en formato JSON
        pass

    def guardar_producto(self, producto):
        # guardar un producto en DynamoDB en formato JSON
        pass

    def obtener_productos(self):
        # obtener todos los productos desde DynamoDB en formato JSON
        pass
