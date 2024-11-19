import json

def save_model_results(model_results, file_path='./submission/model_results.json'):
    """
    Guarda los resultados de un modelo en un archivo JSON.
    
    Args:
    - model_results (dict): Un diccionario con los resultados del modelo.
    - file_path (str): La ruta del archivo donde guardar los resultados (por defecto './submission/model_results.json').
    """
    # Carga el archivo JSON existente, si existe
    try:
        with open(file_path, 'r') as f:
            all_results = json.load(f)
            if isinstance(all_results, dict):
                all_results = [all_results]  # Convertir a lista si es un diccionario
    except FileNotFoundError:
        all_results = []  # Si no existe el archivo, creamos una lista vacía

    # Agregar los nuevos resultados
    all_results.append(model_results)

    # Guardar los resultados actualizados en el archivo JSON
    with open(file_path, 'w') as f:
        json.dump(all_results, f, indent=4)  # 'indent=4' para mejorar la legibilidad del JSON
