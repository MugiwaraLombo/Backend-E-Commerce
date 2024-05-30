from Usuario import Usuario
from Carrito import CarritoCompras
class Cliente:
    def __init__(self, usuario, direccion : str, direccion_facturacion : str, forma_pago : str, dni, id_cliente):
        self.id_cliente = id_cliente
        self.historial_compras = [] #agregar funcion que conecte los datos del carrito de compras de un usuario a su historial
        self.direccion = direccion
        self.direccion_facturacion = direccion_facturacion
        self.forma_pago = forma_pago
        self.dni = dni
        self.usuario = usuario.id_usuario
 
    def compra_hecha(self, carrito):
        self.historial_compras.append(carrito.lista_productos, carrito.total_carrito)