import requests
from flask import Flask, request, jsonify
from carpeta_producto.Producto import Producto
from carpeta_usuario.Usuario import Usuario

app = Flask(__name__)

# Configurar credenciales de WooCommerce
WC_API_URL = 'https:/wp-json/wc/v3'
WC_CONSUMER_KEY = 'your_consumer_key'
WC_CONSUMER_SECRET = 'your_consumer_secret'

def get_wc_auth_params():
    return {
        'consumer_key': WC_CONSUMER_KEY,
        'consumer_secret': WC_CONSUMER_SECRET
    }

class CarritoCompras:
    def __init__(self, producto_agregado, cantidad_producto, costo_envio, codigo_postal, pais_region, estado_envio):
        self.id_compra = None  # Será definido por la base de datos (DB)
        self.lista_productos = [(producto_agregado, cantidad_producto)]
        self.subtotal_sin_envio = producto_agregado.precio * cantidad_producto
        self.total_carrito = self.subtotal_sin_envio + costo_envio
        self.usuario = None  # Aquí podrías asignar un usuario si lo deseas
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



@app.route('/cart', methods=['GET'])
def get_cart():
    response = requests.get(f'{WC_API_URL}/cart', params=get_wc_auth_params())
    return jsonify(response.json())

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    response = requests.post(f'{WC_API_URL}/cart/add', json={
        'product_id': product_id,
        'quantity': quantity
    }, params=get_wc_auth_params())
    return jsonify(response.json())

@app.route('/cart/update', methods=['POST'])
def update_cart():
    data = request.get_json()
    cart_item_key = data['cart_item_key']
    quantity = data['quantity']
    response = requests.post(f'{WC_API_URL}/cart/update', json={
        'cart_item_key': cart_item_key,
        'quantity': quantity
    }, params=get_wc_auth_params())
    return jsonify(response.json())

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    cart_item_key = data['cart_item_key']
    response = requests.post(f'{WC_API_URL}/cart/remove', json={
        'cart_item_key': cart_item_key
    }, params=get_wc_auth_params())
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
