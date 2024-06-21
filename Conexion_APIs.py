import firebase_admin
from firebase_admin import credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import json

# Inicializar Firebase Admin SDK
cred = credentials.Certificate('./path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Configurar Google APIs Client Library
credentials = service_account.Credentials.from_service_account_file(
    './path/to/serviceAccountKey.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/firebase'])

firebase_management = build('firebase', 'v1beta1', credentials=credentials)
cloud_resource_manager = build('cloudresourcemanager', 'v1', credentials=credentials)

# Función para listar proyectos de Firebase
def list_firebase_projects():
    request = firebase_management.projects().list()
    response = request.execute()
    print('Projects:', response)

list_firebase_projects()

# Función para listar proyectos en Google Cloud
def list_cloud_projects():
    request = cloud_resource_manager.projects().list()
    response = request.execute()
    print('Cloud Projects:', response.get('projects', []))

list_cloud_projects()

# Función para desplegar en Firebase Hosting
def deploy_to_firebase_hosting(project_id, site_id):
    url = f'https://firebase.googleapis.com/v1beta1/projects/{project_id}/sites/{site_id}/releases'
    headers = {
        'Authorization': f'Bearer {credentials.token}',
        'Content-Type': 'application/json'}
    data = { # Payload para el lanzamiento 
        }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print('Deploy response:', response.json())

deploy_to_firebase_hosting('YOUR_PROJECT_ID', 'YOUR_SITE_ID')