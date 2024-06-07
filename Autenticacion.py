from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText

# Definimos una clase abstracta para la autenticación de usuarios

class Autenticacion(ABC):
    @abstractmethod
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
    
    def autenticar_usuario(self):
        return f'Usuario: {self.usuario}, password: {self.password}'

# Implementamos la clase Autenticacion

class ImplementacionAutenticacion(Autenticacion):
    def __init__(self, usuario, password):
        super().__init__(usuario, password)
        self.intentos_fallidos = 0
    
    def autenticar_usuario(self, usuario, password):
        if self.usuario == usuario and self.password == password:
            return f'Usuario autenticado: {self.usuario}'
        else:
            raise ValueError("Credenciales incorrectas")
    
    def autenticacion_usuario(self, usuario, password):  
        if self.usuario == usuario and self.password == password:
            return f'Usuario autenticado: {self.usuario}'
        else:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 3:
                self.enviar_correo(usuario)
                raise ValueError("Credenciales incorrectas. Se ha enviado un correo electrónico para restablecer la contraseña.")
            else:
                raise ValueError("Credenciales incorrectas. Inténtalo de nuevo.")
            
    def enviar_correo(self, usuario):
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "tu_correo@example.com"
        sender_password = "tu_contraseña"
        receiver_email = "correo_del_usuario@example.com"

        subject = "Restablecimiento de contraseña"
        body = f"Hola {usuario},\n\nTu cuenta ha sido bloqueada debido a intentos fallidos de inicio de sesión. Por favor, restablece tu contraseña."

        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

try:
    autenticacion = ImplementacionAutenticacion("nombre_de_usuario", "contraseña_incorrecta")
    autenticacion.autenticar_usuario("nombre_de_usuario", "contraseña_correcta")
except ValueError as e:
    print(f"Error: {e}")

    def reset_intentos_fallidos(self):
        self.intentos_fallidos = 0
        print("contador de intentos fallidos volvio a 0")

class NotificacionCuenta():
    def __init__(self, cliente_email):
        self.cliente_email = cliente_email

    def enviar_creacion_cuenta(self):
        mensaje = "¡Su cuenta ha sido creada con éxito! ¡Bienvenido a nuestro servicio!"
        self.enviar_email(mensaje)

    def enviar_cambio_contrasena(self):
        mensaje = "Se ha realizado un cambio de contraseña en su cuenta"
        self.enviar_email(mensaje)

    def enviar_actualizacion_info(self):
        mensaje = "Se han actualizado los detalles de su cuenta"
        self.enviar_email(mensaje)

    def enviar_email(self, mensaje):
        servidor_smtp = 'smtp.example.com'  # Cambiar esto por el servidor SMTP que vamos a utilizar
        puerto_smtp = 587  # Puerto para TLS
        remitente = 'tu_correo@example.com'  # Cambiar esto por su dirección de correo electrónico
        destinatario = self.cliente_email
    
        # Aca van el nombre de usuario y contraseña de la cuenta de correo desde la que enviamos los correos
        usuario_smtp = 'tu_usuario'
        contraseña_smtp = 'tu_contraseña'

        # Construye el mensaje
        mensaje_completo = f"From: {remitente}\nTo: {destinatario}\nSubject: Notificación de cuenta\n\n{mensaje}"

        try:
            # Inicia la conexión al servidor SMTP
            server = smtplib.SMTP(servidor_smtp, puerto_smtp)
            server.starttls()  # Habilita la conexión segura

            # Inicia sesión en el servidor SMTP
            server.login(usuario_smtp, contraseña_smtp)

            # Envía el correo electrónico
            server.sendmail(remitente, destinatario, mensaje_completo)
            print(f"Correo electrónico enviado a {destinatario}: {mensaje}")

        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")

        finally:
            # Cierra la conexión al servidor SMTP
            server.quit()


cliente_email = "cliente@example.com"
notificacion = NotificacionCuenta(cliente_email)

notificacion.enviar_creacion_cuenta()
notificacion.enviar_cambio_contrasena()
notificacion.enviar_actualizacion_info()

import smtplib

class ConfirmacionesPedidos():
    def __init__(self, cliente_email):
        self.cliente_email = cliente_email

    def enviar_confirmacion_pedido(self, detalles_pedido, direccion_envio, info_pago):
        mensaje = self.construir_mensaje_confirmacion(detalles_pedido, direccion_envio, info_pago)
        self.enviar_email(mensaje)

    def construir_mensaje_confirmacion(self, detalles_pedido, direccion_envio, info_pago):
        mensaje = "Confirmación de Pedido:\n\n"
        mensaje += "Detalles del Pedido:\n"
        for producto, cantidad in detalles_pedido.items():
            mensaje += f"- {cantidad} x {producto}\n"

        mensaje += "\nDirección de Envío:\n"
        mensaje += f"{direccion_envio['nombre']}\n"
        mensaje += f"{direccion_envio['direccion']}\n"
        mensaje += f"{direccion_envio['ciudad']}, {direccion_envio['codigo_postal']}\n"
        mensaje += f"{direccion_envio['pais']}\n"

        mensaje += "\nInformación de Pago:\n"
        mensaje += f"Tarjeta: {info_pago['tarjeta']}\n"
        mensaje += f"Fecha de Expiración: {info_pago['fecha_expiracion']}\n"
        mensaje += f"Código de Seguridad: {info_pago['codigo_seguridad']}\n"

        return mensaje

    def enviar_email(self, mensaje):
        servidor_smtp = 'smtp.example.com'  # Cambiar esto por el servidor SMTP que estémos utilizando
        puerto_smtp = 587  # Puerto para TLS
        remitente = 'tu_correo@example.com'  # Cambia esto por la dirección de correo electrónico
        destinatario = self.cliente_email

        # Aca van el nombre de usuario y contraseña de la cuenta de correo desde la que enviamos los correos
        usuario_smtp = 'tu_usuario'
        contraseña_smtp = 'tu_contraseña'

        # Construye el mensaje
        mensaje_completo = f"From: {remitente}\nTo: {destinatario}\nSubject: Confirmación de Pedido\n\n{mensaje}"

        try:
            # Inicia la conexión al servidor SMTP
            server = smtplib.SMTP(servidor_smtp, puerto_smtp)
            server.starttls()  # Habilita la conexión segura

            # Inicia sesión en el servidor SMTP
            server.login(usuario_smtp, contraseña_smtp)

            # Envía el correo electrónico
            server.sendmail(remitente, destinatario, mensaje_completo)
            print(f"Correo electrónico de confirmación de pedido enviado a {destinatario}")

        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")

        
        

cliente_email = "cliente@example.com"
confirmacion_pedido = ConfirmacionesPedidos(cliente_email)

detalles_pedido = {}
direccion_envio = {}
info_pago = {}

confirmacion_pedido.enviar_confirmacion_pedido(detalles_pedido, direccion_envio, info_pago)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NotificacionesEnvio():
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def enviar_notificacion(self, destinatario, estado_envio, enlace_seguimiento=None):
        mensaje = self._crear_mensaje(destinatario, estado_envio, enlace_seguimiento)
        self._enviar_correo(destinatario, mensaje)

    def _crear_mensaje(self, destinatario, estado_envio, enlace_seguimiento=None):
        mensaje = MIMEMultipart()
        mensaje['From'] = self.sender_email
        mensaje['To'] = destinatario
        mensaje['Subject'] = 'Estado de envío: {}'.format(estado_envio)

        cuerpo_mensaje = 'El estado de su envío es: {}\n'.format(estado_envio)
        if enlace_seguimiento:
            cuerpo_mensaje += 'Puede hacer seguimiento de su pedido aquí: {}'.format(enlace_seguimiento)

        mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))
        return mensaje.as_string()

    def _enviar_correo(self, destinatario, mensaje):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, destinatario, mensaje)

if __name__ == "__main__":
    smtp_server = 'smtp.example.com'
    smtp_port = 465  # Puerto SSL
    sender_email = 'tucorreo@example.com'
    sender_password = 'tupassword'

    notificador = NotificacionesEnvio(smtp_server, smtp_port, sender_email, sender_password)

    destinatario = 'correodestinatario@example.com'
    estado_envio = 'En camino'
    enlace_seguimiento = 'https://example.com/seguimiento_pedido/123456'

    notificador.enviar_notificacion(destinatario, estado_envio, enlace_seguimiento)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class RecordatoriosCarritoAbandonado():
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def enviar_recordatorio(self, destinatario, productos_carrito):
        mensaje = self._crear_mensaje(destinatario, productos_carrito)
        self._enviar_correo(destinatario, mensaje)

    def _crear_mensaje(self, destinatario, productos_carrito):
        mensaje = MIMEMultipart()
        mensaje['From'] = self.sender_email
        mensaje['To'] = destinatario
        mensaje['Subject'] = '¡Vuelve y completa tu compra!'

        cuerpo_mensaje = '¡Hola!\n\n'
        cuerpo_mensaje += 'Notamos que tienes productos en tu carrito de compras, pero no has completado la compra.\n\n'
        cuerpo_mensaje += 'Productos en tu carrito:\n'
        for producto in productos_carrito:
            cuerpo_mensaje += '- {}\n'.format(producto)
        cuerpo_mensaje += '\nPor favor, vuelve a nuestro sitio y completa tu compra.\n\n'
        cuerpo_mensaje += 'Gracias,\nTu tienda en línea'

        mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))
        return mensaje.as_string()

    def _enviar_correo(self, destinatario, mensaje):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, destinatario, mensaje)

if __name__ == "__main__":
    smtp_server = 'smtp.example.com'
    smtp_port = 465  # Puerto SSL
    sender_email = 'tucorreo@example.com'
    sender_password = 'tupassword'

    recordatorios = RecordatoriosCarritoAbandonado(smtp_server, smtp_port, sender_email, sender_password)

    destinatario = 'correodestinatario@example.com'
    productos_carrito = ['Producto 1', 'Producto 2', 'Producto 3']

    recordatorios.enviar_recordatorio(destinatario, productos_carrito)

    import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class BoletinesInformativosPromociones():
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def enviar_boletin_informativo(self, destinatarios, asunto, contenido):
        mensaje = self._crear_mensaje(destinatarios, asunto, contenido)
        self._enviar_correo(destinatarios, mensaje)

    def _crear_mensaje(self, destinatarios, asunto, contenido):
        mensaje = MIMEMultipart()
        mensaje['From'] = self.sender_email
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto

        mensaje.attach(MIMEText(contenido, 'plain'))
        return mensaje.as_string()

    def _enviar_correo(self, destinatarios, mensaje):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, destinatarios, mensaje)

if __name__ == "__main__":
    smtp_server = 'smtp.example.com'
    smtp_port = 465  # Puerto SSL
    sender_email = 'tucorreo@example.com'
    sender_password = 'tupassword'

    boletines = BoletinesInformativosPromociones(smtp_server, smtp_port, sender_email, sender_password)

    destinatarios = ['cliente1@example.com', 'cliente2@example.com', 'cliente3@example.com']
    asunto = '¡Nuevos productos y promociones!'
    contenido = '¡Hola!\n\nTenemos nuevos productos en nuestra tienda en línea. Además, no te pierdas nuestras promociones especiales esta semana.\n\nVisita nuestro sitio para obtener más información.\n\n¡Gracias por ser parte de nuestra comunidad!\n\nTu tienda en línea'

    boletines.enviar_boletin_informativo(destinatarios, asunto, contenido)

    try:
            # Inicia la conexión al servidor SMTP
            server = smtplib.SMTP(servidor_smtp, puerto_smtp)
            server.starttls()  # Habilita la conexión segura

            # Inicia sesión en el servidor SMTP
            server.login(usuario_smtp, contraseña_smtp)

            # Envía el correo electrónico
            server.sendmail(remitente, destinatario, mensaje_completo)
            print(f"Correo electrónico de confirmación de pedido enviado a {destinatario}")

        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")
        # cerrar la conexion al servidor SMTP 
        finally:
           server.quit()

# Definimos una clase abstracta para la gestión de productos
class GestionProductos(ABC):
    @abstractmethod
    def __init__(self, productos, precio, codigo):
        self.productos = productos
        self.precio = precio
        self.codigo = codigo

    def listar_productos(self):
       return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Implementamos la clase GestionProductos
class ImplementacionGestionProductos(GestionProductos):
    def __init__(self, productos, precio, codigo):
        super().__init__(productos, precio, codigo)

    def listar_productos(self):
        return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Definimos una clase abstracta para la gestión del carrito de compras
class GestionCarritoCompras(ABC):
    @abstractmethod
    def __init__(self, id_item, id_carrito):
        self.id_item = id_item
        self.id_carrito = id_carrito
    
    def agregar_item_carrito(self):
        self.carrito = []

# Implementamos la clase GestionCarritoCompras
class ImplementacionGestionCarritoCompras(GestionCarritoCompras):
    def __init__(self, id_item, id_carrito):
       super().__init__(id_item, id_carrito)
    
    def agregar_item_carrito(self, item):
        self.carrito.append(item)
        return f'Item agregado al carrito: {item}'

    def listar_carrito(self):
        if not self.carrito:
            return "El carrito está vacío."
        else:
            return f'Contenido del carrito: {", ".join(self.carrito)}'