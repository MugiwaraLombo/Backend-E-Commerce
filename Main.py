from abc import ABC, abstractmethod

# Definir las clases de Usuario, Cliente, Producto, Carrito de Compras, Proveedores y Administrador.

class Usuario():
    def __init__(self, id_usuario, nombre, apellido, email, telefono=None, contraseña=None, verificacion=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.contraseña = contraseña
        self.verificacion = verificacion

class Cliente(Usuario):
    def __init__(self, id_cliente, usuario, historial_compras, direccion, direccion_facturacion, forma_pago=None):
        super().__init__(usuario.id_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.telefono, usuario.contraseña, usuario.verificacion)
        self.id_cliente = id_cliente
        self.historial_compras = historial_compras
        self.direccion = direccion
        self.direccion_facturacion = direccion_facturacion
        self.forma_pago = forma_pago

class Producto():
    def __init__(self, id_producto, nombre, precio, stock, descripcion, imagen, categoria, calificacion=None, historial_ventas=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.imagen = imagen
        self.categoria = categoria
        self.calificacion = calificacion
        self.historial_ventas = historial_ventas

class CarritoCompras():
    def __init__(self, id_compra, productos, subtotal_sin_envio, total_carrito, usuario, codigo_postal, pais_region, estado_envio):
        self.id_compra = id_compra
        self.productos = productos
        self.subtotal_sin_envio = subtotal_sin_envio
        self.total_carrito = total_carrito
        self.usuario = usuario
        self.codigo_postal = codigo_postal
        self.pais_region = pais_region
        self.estado_envio = estado_envio

class Proveedor():
    def __init__(self, nombre, direccion, telefono, productos):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"{producto} no está en la lista de productos del proveedor.")

proveedor1 = Proveedor(nombre="", direccion="", telefono="", productos=["", ""])
print(proveedor1.nombre)  
proveedor1.agregar_producto("")
print(proveedor1.productos)  
proveedor1.eliminar_producto("")
print(proveedor1.productos)  

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


# Definir una clase abstracta para la autenticación de usuarios

class Autenticacion(ABC):
    @abstractmethod
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    
    def autenticar_usuario(self):
        return f'Usuario: {self.usuario}, Contraseña: {self.contraseña}'

import smtplib
from email.mime.text import MIMEText

# Implementar la clase Autenticacion

class ImplementacionAutenticacion(Autenticacion):
    def __init__(self, usuario, contraseña):
        super().__init__(usuario, contraseña)
        self.intentos_fallidos = 0
    
    def autenticar_usuario(self, usuario, contraseña):
        if self.usuario == usuario and self.contraseña == contraseña:
            return f'Usuario autenticado: {self.usuario}'
        else:
            raise ValueError("Credenciales incorrectas")
    
    def autenticacion_usuario(self, usuario, contraseña):  
        if self.usuario == usuario and self.contraseña == contraseña:
            return f'Usuario autenticado: {self.usuario}'
        else:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 3:
                self.enviar_correo(usuario)
                raise ValueError("Credenciales incorrectas. Se ha enviado un correo electrónico para restablecer la contraseña.")
            else:
                raise ValueError("Credenciales incorrectas. Inténtalo de nuevo.")
            
    def enviar_correo(self, usuario):
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "tu_correo@example.com"
        sender_password = "tu_contraseña"
        receiver_email = "correo_del_usuario@example.com"

        subject = "Restablecimiento de contraseña"
        body = f"Hola {usuario},\n\nTu cuenta ha sido bloqueada debido a intentos fallidos de inicio de sesión. Por favor, restablece tu contraseña."

        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

try:
    autenticacion = ImplementacionAutenticacion("nombre_de_usuario", "contraseña_incorrecta")
    autenticacion.autenticar_usuario("nombre_de_usuario", "contraseña_correcta")
except ValueError as e:
    print(f"Error: {e}")

# Definir una clase abstracta para la gestión de productos
class GestionProductos(ABC):
    @abstractmethod
    def __init__(self, productos, precio, codigo):
        self.productos = productos
        self.precio = precio
        self.codigo = codigo

    def listar_productos(self):
       return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Implementar la clase GestionProductos
class ImplementacionGestionProductos(GestionProductos):
    def __init__(self, productos, precio, codigo):
        super().__init__(productos, precio, codigo)

    def listar_productos(self):
        return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Definir una clase abstracta para la gestión del carrito de compras
class GestionCarritoCompras(ABC):
    @abstractmethod
    def __init__(self, id_item, id_carrito):
        self.id__item = id_item
        self.id_carrito = id_carrito
    
    def agregar_item_carrito(self):
        self.carrito = []

    
# Implementar la clase GestionCarritoCompras
class ImplementacionGestionCarritoCompras(GestionCarritoCompras):
    def __init__(self, id_item, id_carrito):
       super().__init__(id_item, id_carrito)

    def agregar_item_carrito(self, item):
        self.carrito.append(item)
        return f'Item agregado al carrito: {item}'

    def listar_carrito(self):
        if not self.carrito:
            return "El carrito está vacío."
        else:
            return f'Contenido del carrito: {", ".join(self.carrito)}'
        
carrito_compras = ImplementacionGestionCarritoCompras()
item1 = "Producto A"
item2 = "Producto B"
print(carrito_compras.agregar_item_carrito(item1))
print(carrito_compras.agregar_item_carrito(item2))
print(carrito_compras.listar_carrito())
    
   

# Uso de las clases e interfaces definidas
autenticacion = ImplementacionAutenticacion()
autenticacion.autenticar_usuario("nombre_de_usuario", "contraseña")

gestion_productos = ImplementacionGestionProductos()
gestion_productos.listar_productos("Producto", "precio", "Codigo")

gestion_carrito_compras = ImplementacionGestionCarritoCompras()
gestion_carrito_compras.agregar_item_carrito()


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





