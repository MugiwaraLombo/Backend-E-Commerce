from Producto import Producto
from Usuario import Usuario
class CarritoCompras(Producto, Usuario):
    def __init__(self, producto_agregado, cantidad_producto, costo_envio, codigo_postal, pais_region, estado_envio):
        self.id_compra = "lo define la DB" #es auto incremental
        self.lista_productos = [(producto_agregado, cantidad_producto)]
        self.subtotal_sin_envio = producto_agregado.precio * cantidad_producto
        self.total_carrito = self.subtotal_sin_envio + costo_envio
        self.usuario = self.id_usuario
        self.codigo_postal = codigo_postal
        self.pais_region = pais_region
        self.estado_envio = estado_envio

    def agregar_producto(self, producto, cantidad):
        self.lista_productos.append((producto, cantidad))
        self.subtotal_sin_envio += producto.precio * cantidad
        self.total_carrito = self.subtotal_sin_envio + self.costo_envio

    def quitar_producto(self, producto, cantidad):
        for i, (prod, cant) in enumerate(self.lista_productos):
            if prod.id_producto == producto.id_producto:
                if cantidad >= cant:
                    self.subtotal_sin_envio -= prod.precio * cant
                    del self.lista_productos[i]
                else:
                    self.lista_productos[i] = (prod, cant - cantidad)
                    self.subtotal_sin_envio -= prod.precio * cantidad
                self.total_carrito = self.subtotal_sin_envio + self.costo_envio
                break
        else:
            print("Producto no encontrado en el carrito")