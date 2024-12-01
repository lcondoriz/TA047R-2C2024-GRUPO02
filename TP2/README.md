**Organización de Datos**

Trabajo Práctico N°2: Story Points

Grupo 02 - Célestine Raveneau, Florian Escaffre, Juan Gomez, Luis Condori

Cátedra Ing. Rodriguez, Juan Manuel - 2C2024

## Dateset de User Stories

El conjunto de datos es una serie de casos de uso o user stories de diversos proyectos, para las cuales se tiene el número de story points que indican la complejidad de cada tarea. Se intentará predecir los story points para un texto dado como user story

**Descripción de columnas**

* **title**: Título de la user story.

* **description**: Descripción de la user story.

* **project**: Nombre del proyecto en el cual esa user story se crea.

* **storypoint**: Puntaje (nivel de complejidad) de la user story.

## Extra
Se cuenta con un archivo `model_results.json` que contiene los resultados de la evaluación de los modelos. El archivo contiene las siguientes columnas:

```python
results_rl = {
    'model': 'LinearRegression',
    'best_params': random_search.best_params_,
    'best_score': -random_search.best_score_,
    'rmse_train': rmse_train,
    'rmse_test': rmse_test
}
```

Para ver en formato tabla usar la pagina [jsongrid](https://jsongrid.com/json-grid)