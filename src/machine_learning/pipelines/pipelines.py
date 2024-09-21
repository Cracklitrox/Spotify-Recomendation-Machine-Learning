from kedro.pipeline import Pipeline, node
from machine_learning.nodes import calcular_matriz_correlacion

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=calcular_matriz_correlacion,
                inputs="spotify_raw",  # Este es el dataset que debes definir en `catalog.yml`
                outputs=None,          # No hay un resultado final que guardar
                name="calcular_matriz_correlacion_node"
            )
        ]
    )