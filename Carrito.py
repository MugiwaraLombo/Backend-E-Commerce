import requests
from flask import Flask, request, jsonify

# Definición de clases
class Usuario:
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, telefono=None, verificacion=None):
        self.id_usuario = None  # Lo define la DB y es auto incremental
        self.name = [nombre, apellido]
        self.__mail = mail
        self.__password = password
        self.__telefono = telefono
        self.verificacion = verificacion

    def set_password(self, new_password: str):
        self.__password = new_password

    def get_password(self):
        return self.__password

    def set_mail(self, new_mail: str):
        self.__mail = new_mail

    def get_mail(self):
        return self.__mail

    def set_telefono(self, new_telefono: str):
        self.__telefono = new_telefono

    def get_telefono(self):
        return self.__telefono

    def __str__(self) -> str:
        pantalla = f'nombre: {self.name}, mail: {self.get_mail()}, telefono: {self.get_telefono()}'
        return pantalla

class Producto:
    def __init__(self, id_producto, nombre_producto: str, precio: float, descripcion: str, imagen, categoria: str):
        self.id_producto = id_producto
        self.nombre = nombre_producto
        self.precio = precio
        self.stock = "entra por la conexion a la DB del inventario"
        self.descripcion = descripcion
        self.imagen = imagen
        self.categoria = categoria
        self.calificaciones = []
        self.historial_ventas = []

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion,
            'imagen': self.imagen,
            'categoria': self.categoria
        }

class CarritoCompras:
    def __init__(self, producto_agregado, cantidad_producto, costo_envio, codigo_postal, pais_region, estado_envio):
        self.id_compra = None  # Debe definirlo la DB
        self.lista_productos = [(producto_agregado, cantidad_producto)]
        self.costo_envio = costo_envio
        self.actualizar_total()
        self.codigo_postal = codigo_postal
        self.pais_region = pais_region
        self.estado_envio = estado_envio

    def agregar_producto(self, producto, cantidad):
        for i, (prod, cant) in enumerate(self.lista_productos):
            if prod.id_producto == producto.id_producto:
                self.lista_productos[i] = (prod, cant + cantidad)
                self.actualizar_total()
                return
        self.lista_productos.append((producto, cantidad))
        self.actualizar_total()

    def quitar_producto(self, producto, cantidad):
        for i, (prod, cant) in enumerate(self.lista_productos):
            if prod.id_producto == producto.id_producto:
                if cantidad >= cant:
                    del self.lista_productos[i]
                else:
                    self.lista_productos[i] = (prod, cant - cantidad)
                self.actualizar_total()
                return
        else:
            print("Producto no encontrado en el carrito")

    def actualizar_total(self):
        self.subtotal_sin_envio = sum(prod.precio * cant for prod, cant in self.lista_productos)
        self.total_carrito = self.subtotal_sin_envio + self.costo_envio

# Ejemplo de datos del carrito para pruebas
producto_ejemplo = Producto('111', 'cuchillo de aire', 10.0, 'corta como los mejores', 'imagen1.jpg', 'Categoría 1')
carrito = CarritoCompras(
    producto_agregado=producto_ejemplo,
    cantidad_producto=2,
    costo_envio=5.0,
    codigo_postal='el de tu casa',
    pais_region='argentina papa',
    estado_envio='preparacion'
)

# Configuración de la aplicación Flask
app = Flask(__name__)

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify({
        'productos': [prod.to_dict() for prod, cant in carrito.lista_productos],
        'subtotal_sin_envio': carrito.subtotal_sin_envio,
        'costo_envio': carrito.costo_envio,
        'total_carrito': carrito.total_carrito
    })

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    producto_id = data.get('product_id')
    cantidad = data.get('cantidad')

    if not producto_id or not cantidad:
        return jsonify({'error': 'Debe proporcionar product_id y cantidad'}), 400

    nuevo_producto = Producto(id_producto="12p90", nombre_producto='cuchillo de metal', precio=20.0, descripcion='cuchillo hecho de metal', imagen='imagen_prueba.jpg', categoria='Categoría prueba')
    carrito.agregar_producto(nuevo_producto, cantidad)

    nombre_producto_agregado = nuevo_producto.nombre
    mensaje = f'Producto "{nombre_producto_agregado}" (ID: {producto_id}) agregado al carrito correctamente'

    return jsonify({'message': mensaje})

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    producto_id = data.get('producto_id')
    cantidad = data.get('cantidad')

    if not producto_id:
        return jsonify({'error': 'ID del producto no proporcionado'}), 400

    for prod, cant in carrito.lista_productos:
        if prod.id_producto == producto_id:
            carrito.quitar_producto(prod, cantidad)
            mensaje = f'Producto eliminado del carrito: {prod.nombre}'
            return jsonify({
                'message': mensaje,
                'subtotal_sin_envio': carrito.subtotal_sin_envio,
                'total_carrito': carrito.total_carrito
            })

    return jsonify({'error': 'Producto no encontrado en el carrito'}), 404

if __name__ == '__main__':
    app.run(debug=True)
