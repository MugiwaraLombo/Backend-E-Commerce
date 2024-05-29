from Cliente import Cliente
from Producto import Producto
from Empresa import Empresa
from flask import Flask, jsonify, request

app = Flask(__name__)

class Factura:
    def __init__(self, numero_factura, empresa, cliente, productos, descuentos, total, fecha, domicilio_entrega):
        self.numero_factura = numero_factura
        self.empresa = empresa
        self.cliente = cliente
        self.productos = productos
        self.descuentos = descuentos
        self.total = total
        self.fecha = fecha
        self.domicilio_entrega = domicilio_entrega

    def calcular_descuento_producto(self, producto):
        descuento_total = 0
        for descuento in self.descuentos:
            if producto["ID"] in descuento.get("productos_aplicables", []):
                descuento_total += descuento["monto"]
        return descuento_total

    def actualizar_descuentos_y_total(self):
        for producto in self.productos:
            descuento = self.calcular_descuento_producto(producto)
            producto["descuento"] = descuento

        total_productos = sum((producto["precio"] - producto["descuento"]) * producto["cantidad"] for producto in self.productos)
        self.total = total_productos

    def agregar_descuento(self, tipo, monto, productos_aplicables):
        nuevo_descuento = {
            "tipo": tipo,
            "monto": monto,
            "productos_aplicables": productos_aplicables
        }
        self.descuentos.append(nuevo_descuento)

    def to_dict(self):
        return {
            "numero_factura": self.numero_factura,
            "empresa": self.empresa,
            "cliente": self.cliente,
            "productos": self.productos,
            "descuentos": self.descuentos,
            "total": self.total,
            "fecha": self.fecha,
            "domicilio_entrega": self.domicilio_entrega
        }



    @app.route('/facturacion', methods=['GET'])
    def obtener_facturacion():
        Factura.actualizar_descuentos_y_total()
        return jsonify(Factura.to_dict())

    @app.route('/facturacion/descuento', methods=['POST'])
    def agregar_descuento():
        data = request.get_json()
        tipo = data.get('tipo')
        monto = data.get('monto')
        productos_aplicables = data.get('productos_aplicables')

        Factura.agregar_descuento(tipo, monto, productos_aplicables)
        Factura.actualizar_descuentos_y_total()

        return jsonify(Factura.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
