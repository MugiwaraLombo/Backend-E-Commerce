from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask (__name__)


MONGO_URI = 'mongodb+srv://tu_usuario:tu_contraseña@tu_cluster.mongodb.net/tu_base_de_datos?retryWrites=true&w=majority'
client = MongoClient(MONGO_URI)
db = client ['e-commerce']
carritos_collection =db['carritos']

@app.route('/cart', methods=['GET'])
def get_cart():
    carritos = list(carritos_collection.find())
    for carrito in carritos:
        carrito['_id'] = str(carrito['_id'])
    return jsonify(carritos)

if __name__ == '__main__':
    app.run(debug=True)

from app import app

if __name__ == "__main__":
    app.run()

MONGO_URI = 'mongodb+srv://tu_usuario:tu_contraseña@tu_cluster.mongodb.net/tu_base_de_datos?retryWrites=true&w=majority'
client = MongoClient(MONGO_URI)