import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def calcular_matriz_correlacion(spotify: pd.DataFrame) -> None:
    # Selección de Datos Numéricos
    datosNumericos = spotify.select_dtypes(include=[np.number])
    
    # Calcular la matriz de correlación
    matriz_correlacion = datosNumericos.corr()

    # Mostrar la matriz de correlación
    plt.figure(figsize=(8, 6))
    sns.heatmap(matriz_correlacion, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={'shrink': .8})
    plt.title('Matriz de Correlación')
    plt.show()