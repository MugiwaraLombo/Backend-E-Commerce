# insertar en la terminal el siguiente codigo 'pip install boto3'
# Para conectarte a una base de datos en DynamoDB usando Python, 
# necesitarás utilizar la biblioteca boto3, que es el SDK de AWS para Python.

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Conexión a DynamoDB
try:
    session = boto3.Session(
        aws_access_key_id='ACCESS_KEY', #Reemplaza estos valores con tus credenciales de AWS.
        aws_secret_access_key='SECRET_ACCESS_KEY', #Reemplaza estos valores con tus credenciales de AWS.
        region_name='sa-east-1'  # Región de AWS en Sudamérica
    )

    dynamodb = session.resource('dynamodb')

    # Obtener una tabla existente
    table = dynamodb.Table('NombreDeLaTablaExistente')

    # Función para insertar un ítem en la tabla existente
    def insert_item():
        table.put_item(
            Item={
                'id': '456',
                'nombre': 'Jane Doe',
                'edad': 25
            }
        )
        print("Ítem insertado")

    # Función para escanear la tabla existente
    def scan_table():
        response = table.scan()
        items = response['Items']
        for item in items:
            print(item)

    # Función para obtener un ítem por clave primaria
    def get_item_by_key(key):
        response = table.get_item(Key={'id': key})
        item = response.get('Item')
        if item:
            print(f"Ítem encontrado: {item}")
        else:
            print("Ítem no encontrado")

    if __name__ == '__main__':
        insert_item()  # Insertar un ítem
        scan_table()   # Escanear la tabla
        get_item_by_key('456')  # Obtener un ítem por clave primaria

except NoCredentialsError:
    print("Credenciales no encontradas.")
except PartialCredentialsError:
    print("Credenciales incompletas.")
except Exception as e:
    print(f"Error inesperado: {e}")
