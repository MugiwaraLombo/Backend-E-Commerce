#pip install psycopg2  ejecutar en la terminal 

import psycopg2  # Importa la librería psycopg2 para conectarse a PostgreSQL

try:
    # Establece la conexión con la base de datos
    connection = psycopg2.connect(
        user="blabla",          # Nombre de usuario de PostgreSQL
        password="blabla",   # Contraseña de usuario de PostgreSQL
        host="999999 ",           # Dirección del servidor de PostgreSQL (puede ser una IP o un nombre de dominio)
        port="5432",                # Puerto en el que PostgreSQL está escuchando conexiones (por defecto es 5432)
        database="blabla" # Nombre de la base de datos 
    )

    # Crea un cursor para ejecutar consultas SQL
    cursor = connection.cursor()

    # Ejemplo de consulta SQL. Puedes cambiar esto por cualquier consulta que desees ejecutar.
    cursor.execute("SELECT * FROM tabla")

    # Obtiene todos los resultados de la consulta
    rows = cursor.fetchall()

    # Imprime los resultados uno por uno
    for row in rows:
        print(row)

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    # Si ocurre algún error durante la conexión o ejecución de consultas, muestra un mensaje de error
    print("Error al conectar a PostgreSQL:", error)
