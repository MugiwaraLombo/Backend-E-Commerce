from Producto import Producto
from Usuario import Usuario
class CarritoCompras(Producto, Usuario):
    def __init__(self, producto_agregado, cantidad_producto, costo_envio, codigo_postal, pais_region, estado_envio):
        self.id_compra = "lo define la DB" #es auto incremental
        self.productos = [producto_agregado, cantidad_producto]
        self.subtotal_sin_envio = producto_agregado.precio * cantidad_producto
        self.total_carrito = self.subtotal_sin_envio + costo_envio
        self.usuario = self.id_usuario
        self.codigo_postal = codigo_postal
        self.pais_region = pais_region
        self.estado_envio = estado_envio