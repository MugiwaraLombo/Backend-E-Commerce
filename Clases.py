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
 

class Cliente():
    def __init__(self, id_cliente, usuario, historial_compras, direccion, direccion_facturacion, forma_pago=None):
        self.id_cliente = id_cliente
        self.usuario = usuario
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









