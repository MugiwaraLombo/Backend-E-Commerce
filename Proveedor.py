class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def agregar_producto(self, producto):
        if not producto in self.productos :
            self.productos.append(producto)
        else:
            print(f'el producto : {producto} ya se encuentra en la lista')

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"{producto} no está en la lista de productos del proveedor.")









