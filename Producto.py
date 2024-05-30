class Producto:
    def __init__(self, nombre_producto : str, precio : float, descripcion : str, imagen, categoria : str):
        self.id_producto = "lo define la DB" #es auto incremental
        self.nombre = nombre_producto
        self.precio = precio
        self.stock = "entra por la conexion a la DB del inventario"
        self.descripcion = descripcion
        self.imagen = imagen
        self.categoria = categoria
        #agregar las respectivas funciones que hagan llegar las calificaciones e historial de ventas de cada producto y se almacenen respectivamente
        self.calificaciones = []
        self.historial_ventas = []