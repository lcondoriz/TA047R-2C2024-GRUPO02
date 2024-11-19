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