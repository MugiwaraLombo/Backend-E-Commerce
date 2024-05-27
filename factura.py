from Cliente import Cliente
from Producto import Producto
from empresa import Empresa
from flask import Flask, jsonify, request

app = Flask(__name__)

class Factura:
    def __init__(self,numero_factura,empresa,cliente,productos,descuentos,total,fecha,domicilio_entrega):
        self.numero_factura = numero_factura
        self.empresa = empresa
        self.cliente = cliente
        self.productos = productos
        self.descuentos = descuentos
        self.total = total
        self.fecha = fecha
        self.domicilio_entrega = domicilio_entrega

  def calcular_descuento_producto(producto, descuentos):
    descuento_total = 0
    for descuento in descuentos:
        if producto["id_producto"] in descuento.get("productos_aplicables", []):
            descuento_total += descuento["monto"]
    return descuento_total

  def actualizar_descuentos_y_total(self):
    for producto in self.productos:
        descuento = self.calcular_descuento_producto(producto)
        producto["descuento"] = descuento

      total_productos = sum((producto["precio"] - producto["descuento"]) * producto["cantidad"] for producto in self.productos)
      self.total = total_productos

  @app.route('/facturacion', methods=['GET'])
  def obtener_facturacion():
      factura.actualizar_descuentos_y_total()
      return jsonify(factura.to_dict())
  
  @app.route('/facturacion/descuento', methods=['POST'])
  def agregar_descuento():
      data = request.get_json()
      tipo = data.get('tipo')
      monto = data.get('monto')
      productos_aplicables = data.get('productos_aplicables')
      
      factura.agregar_descuento(tipo, monto, productos_aplicables)
      factura.actualizar_descuentos_y_total()
      
      return jsonify(factura.to_dict()), 201
  
  if __name__ == '__main__':
      app.run(debug=True)

