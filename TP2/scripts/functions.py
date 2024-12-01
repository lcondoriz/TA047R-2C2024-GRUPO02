import json
import time
import numpy as np

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


def measure_execution_time(func, *args, **kwargs):
    """
    Mide el tiempo de ejecución de una función, tanto el tiempo de CPU como el tiempo real (Wall time).
    
    :param func: La función que quieres ejecutar.
    :param args: Argumentos posicionales para la función.
    :param kwargs: Argumentos con nombre para la función.
    :return: None
    """
    # Registrar el inicio del tiempo real (Wall time)
    start_wall_time = time.time()

    # Registrar el inicio del tiempo de CPU
    start_cpu_time = time.process_time()

    # Ejecutar la función con sus argumentos
    cointaner_visu = func(*args, **kwargs)

    # Calcular el tiempo transcurrido
    elapsed_wall_time = time.time() - start_wall_time
    elapsed_cpu_time = time.process_time() - start_cpu_time

    # Formatear el tiempo para Wall time (minutos y segundos)
    minutes_wall, seconds_wall = divmod(elapsed_wall_time, 60)
    formatted_wall_time = f"{int(minutes_wall)} min {int(seconds_wall)} s"

    # Mostrar los tiempos
    print(f"CPU times: total: {elapsed_cpu_time:.4f} s")
    print(f"Wall time: {formatted_wall_time}")

    # guadamos en un diccionario los tiempos con un solo decimal
    times = {
        'cpu_time': np.round(elapsed_cpu_time, 1),
        'wall_time': np.round(elapsed_wall_time, 1)
    }

    return cointaner_visu,times

def obtener_transformadores(preprocessor):
    """
    Obtiene los transformadores de un preprocesador y los devuelve como un diccionario.
    
    Args:
        preprocessor: Un objeto preprocesador que tiene un método get_params()
        
    Returns:
        Un diccionario con los transformadores como valores y sus nombres como claves
    """
    transformers = preprocessor.get_params()['transformers']
    return {name: (str(transformer), columns) for name, transformer, columns in transformers}