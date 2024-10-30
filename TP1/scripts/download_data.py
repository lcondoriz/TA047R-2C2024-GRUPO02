import os
import requests

# Función para descargar y guardar un archivo, si no existe ya
def download_file(url, dest_folder, file_name=None):
    # Si no se proporciona un nombre de archivo, lo obtenemos de la URL
    if not file_name:
        file_name = url.split('/')[-1]

    # Crear la carpeta si no existe
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Ruta completa del archivo destino
    file_path = os.path.join(dest_folder, file_name)

    # Verificar si el archivo ya existe
    if os.path.exists(file_path):
        print(f"El archivo {file_name} ya existe en la carpeta {dest_folder}.")
        return  # Si el archivo ya está, no lo descarga de nuevo
    
    # Descargar el archivo desde la URL
    response = requests.get(url, stream=True)
    
    # Verificar si la descarga es exitosa
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Archivo descargado correctamente: {file_name}")
    else:
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")

    
           

