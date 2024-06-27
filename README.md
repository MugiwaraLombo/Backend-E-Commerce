
# E-commerce de Artículos de Cocina

Este proyecto es un e-commerce desarrollado en Python para su Back-end, dedicado a la venta de artículos de cocina. 
El sistema está diseñado para gestionar el inventario, procesar ventas ó pedidos de los clientes y 
mantener una base de datos de productos actualizada.

## Funcionalidades

- *Registro de Usuarios*: Los usuarios pueden crear cuentas para realizar compras y recibir actualizaciones sobre nuevos productos y ofertas.
  
- *Exploración de Productos*: Los clientes pueden navegar por una amplia gama de productos de cocina, incluyendo utensilios, electrodomésticos, y más.

- *Carrito de Compras*: Los usuarios pueden agregar y eliminar productos de su carrito de compras antes de finalizar su pedido.

- *Procesamiento de Pedidos*: El sistema procesa los pedidos de los clientes, gestionando la facturación, el pago y la entrega de los productos.

- *Proveedor*: El sistema tiene una actualización constante de los productos en stock ya que hay contacto directo con los proveedores.

- *Clientes*: Los clientes pueden llevar un registro de sus compras, y pueden seleccionar el método de pago.

- *Facturador*: Permite una emisión de factura si es solicitado con detalle de descuentos y datos de la empresa.

- *Productos*: El sistema tiene una lista de productos con su precio e imagen de referencia.

## Tecnologías Utilizadas

- *Python*: El lenguaje principal de programación utilizado para el desarrollo del backend.

- *Bootstrap*: Es el lenguaje principal para el frontend con distintos frameworks.
  
- *MongoDB y PostgreSQL*: Se utiliza MongoDB para almacenar información de productos y clientes, mientras que PostgreSQL se utiliza para datos transaccionales como órdenes y facturas en tiempo real.

- *Flask*: Se emplea el framework Flask para desarrollar la aplicación web y gestionar las rutas y las vistas.

- *HTML/CSS/JavaScript*: Se utilizan para la creación del frontend de la aplicación web, permitiendo una experiencia de usuario intuitiva y atractiva.

- *Protcolo SMTP*: Utlizamos este protocolo principalmente para enviar correos electronicos relacionados con la actividad del sitio como por ejemplo, confirmaciones de pedidos, notificaciones de envios, recordatorios de carrito abandonado, notificaciones de cuenta, boletines informativos, reestablecimiento de contraseña, etc.

- *Libreria de Python* "EMAIL.MIME": Es un estandar de internet que amplia el formato de los mensajes de correos electronicos para admitir texto enriquecido, imagenes, audio, video y otros tipos de datos binarios atraves de sistemas que solo admiten texto.

- *Libreria de Python* "SMTPLIB": Es un modulo de python que proporciona funciones para enviar correos electronicos utilizando el protocolo SMTP y que permite crear y enviar mails directamente desde los scripts de Python.

## Configuración del Proyecto

1. Clona el repositorio desde GitHub:


git clone https://github.com/MugiwaraLombo/Backend-E-Commerce


2. Instala las dependencias del proyecto:


pip install python-ab
pip install flask *Para la interfaz* 
pip install requests 
pip install firebase
pip install firebase_admin
pip to install PyMongo *Para la conexion a la base de datos de Mongo db*
pip install psycopg2 *Para la conexion a la base de datos de Postgresql*

3. Ejecuta la aplicación desde:


https://binomio08.github.io/Com1-Grupo2-Steve-Jobs/index.html# en tu navegador.


## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir con nuestro proyecto, por favor envía un mail a contribuciones@proyectoecommerce.com

## Detalle del desarrollo Back-End:
* Primero fueron definidas las clases "USUARIO", "CLIENTE", "PRODUCTO" y "CARRITO DE COMPRAS", cada clase tiene metodos y atributos definidos.
* Se utilizó el decorador (ABC) "ABSTRACT METHOD" para proporcionar una plantilla y que otras clases construyan sobre ella.
* Luego creamos las clases "AUTENTICACION" y la subclase "IMPLEMENTACION AUTENTICACION" para identificar y autenticar usuario y contraseña
* Seguimos el mismo procedimiento con la gestion de productos, creamos una clase base llamada  "GESTION DE PRODUCTOS" y una subclase para su implementacion
* Repetimos el procedimiento con el carrito de compras
* Debemos instalar las librerias necesarias para la interfaz con la base de datos. En este caso utilizamos "POSTGRESQL".
* Se definieron las clases "Proveedores", "Empresa", "Facturación".
* Generamos las conexiones correspondientes a la bases de datos para el control de stock y la informacion de usuarios.
