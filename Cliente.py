from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self, nombre, apellido, mail, password, direccion : str, direccion_facturacion : str, forma_pago : str, telefono=None, verificacion=None, DNI, ID_cliente):
        super().__init__(nombre, apellido, mail, password, telefono, verificacion)
        self.historial_compras = [] #agregar funcion que conecte los datos del carrito de compras de un usuario a su historial
        self.direccion = direccion
        self.direccion_facturacion = direccion_facturacion
        self.forma_pago = forma_pago
        self.DNI = DNI
        self.ID_cliente = ID_cliente
