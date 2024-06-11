import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient
from Producto import Producto
from Usuario import Usuario

app = Flask(__name__)

# Configurar credenciales de WooCommerce
WC_API_URL = 'URL'  # Reemplaza con la URL de tu tienda WooCommerce
WC_CONSUMER_KEY = 'consumer_key'  # Reemplaza con tu Consumer Key
WC_CONSUMER_SECRET = 'consumer_secret'  # Reemplaza con tu Consumer Secret

# Conexión a MongoDB
MONGO_HOST = 127.0.0.1  
MONGO_PORT = 27017  
MONGO_USER = 'admin'  
MONGO_PASSWORD = '9#fG7$K2&Z'
MONGO_DB = 'admin'  

# Cadena de conexión
mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource={MONGO_DB}"
client = MongoClient(mongo_uri)

db = client['tienda']
carritos_collection = db['carritos']

client = MongoClient('mongodb://localhost:27017/')  
db = client['tienda']
carritos_collection = db['carritos']

def get_wc_auth_params():
    return {
        'consumer_key': WC_CONSUMER_KEY,
        'consumer_secret': WC_CONSUMER_SECRET
    }

class CarritoCompras:
    def __init__(self, producto_agregado, cantidad_producto, costo_envio, codigo_postal, pais_region, estado_envio):
        self.id_compra = None  # Debe definirlo la DB
        self.lista_productos = [(producto_agregado, cantidad_producto)]
        self.subtotal_sin_envio = producto_agregado.precio * cantidad_producto
        self.costo_envio = costo_envio
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
    carritos = list(carritos_collection.find())
    return jsonify(carritos)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']

    # Aquí debes obtener el producto de la base de datos o de una API
    # Por ejemplo:
    producto = Producto(product_id, "Nombre del Producto", 100)  # Reemplaza con datos reales
    carrito = CarritoCompras(producto, quantity, 10, "12345", "MX", "Ciudad de México")
    
    carrito_dict = {
        "lista_productos": [(producto.__dict__, quantity)],
        "subtotal_sin_envio": carrito.subtotal_sin_envio,
        "total_carrito": carrito.total_carrito,
        "codigo_postal": carrito.codigo_postal,
        "pais_region": carrito.pais_region,
        "estado_envio": carrito.estado_envio
    }

    result = carritos_collection.insert_one(carrito_dict)
    return jsonify({"_id": str(result.inserted_id)})

@app.route('/cart/update', methods=['POST'])
def update_cart():
    data = request.get_json()
    cart_id = data['cart_id']
    product_id = data['product_id']
    quantity = data['quantity']

    # Aquí debes obtener el producto de la base de datos o de una API
    producto = Producto(product_id, "Nombre del Producto", 100)  # Reemplaza con datos reales

    carrito = carritos_collection.find_one({"_id": cart_id})
    if carrito:
        carrito_obj = CarritoCompras(producto, quantity, carrito['costo_envio'], carrito['codigo_postal'], carrito['pais_region'], carrito['estado_envio'])
        carrito_obj.lista_productos = carrito['lista_productos']
        carrito_obj.subtotal_sin_envio = carrito['subtotal_sin_envio']
        carrito_obj.total_carrito = carrito['total_carrito']

        carrito_obj.agregar_producto(producto, quantity)

        carritos_collection.update_one(
            {"_id": cart_id},
            {"$set": {
                "lista_productos": carrito_obj.lista_productos,
                "subtotal_sin_envio": carrito_obj.subtotal_sin_envio,
                "total_carrito": carrito_obj.total_carrito
            }}
        )
        return jsonify({"status": "Carrito actualizado"})
    else:
        return jsonify({"error": "Carrito no encontrado"}), 404

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    cart_id = data['cart_id']
    product_id = data['product_id']
    quantity = data['quantity']

    carrito = carritos_collection.find_one({"_id": cart_id})
    if carrito:
        producto = Producto(product_id, "Nombre del Producto", 100)  # Reemplaza con datos reales

        carrito_obj = CarritoCompras(producto, quantity, carrito['costo_envio'], carrito['codigo_postal'], carrito['pais_region'], carrito['estado_envio'])
        carrito_obj.lista_productos = carrito['lista_productos']
        carrito_obj.subtotal_sin_envio = carrito['subtotal_sin_envio']
        carrito_obj.total_carrito = carrito['total_carrito']

        carrito_obj.quitar_producto(producto, quantity)

        carritos_collection.update_one(
            {"_id": cart_id},
            {"$set": {
                "lista_productos": carrito_obj.lista_productos,
                "subtotal_sin_envio": carrito_obj.subtotal_sin_envio,
                "total_carrito": carrito_obj.total_carrito
            }}
        )
        return jsonify({"status": "Producto eliminado del carrito"})
    else:
        return jsonify({"error": "Carrito no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
