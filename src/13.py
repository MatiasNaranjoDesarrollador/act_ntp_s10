import pandas as pd
import numpy as np

def seleccionar_multiples_filas(df: pd.DataFrame):
    """
    Selecciona múltiples filas no consecutivas de un DataFrame.

    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original ---")
    print(df.head())
    print("\n" + "-"*40 + "\n")

    # 1. Seleccionar filas usando una lista de posiciones específicas
    posiciones_especificas = [0, 5, 12, 19, 25]
    filas_especificas = df.iloc[posiciones_especificas]
    print(f"1. Filas en posiciones específicas {posiciones_especificas}:")
    print(filas_especificas)
    print("\n" + "-"*40 + "\n")

    # 2. Seleccionar filas aleatorias (usando .sample())
    # El método .iloc no es ideal para esto; .sample() es la herramienta correcta
    filas_aleatorias = df.sample(n=5, random_state=42)
    print("2. 5 filas aleatorias (usando .sample()):")
    print(filas_aleatorias)
    print("\n" + "-"*40 + "\n")
    
    # 3. Combinar diferentes métodos de selección
    # Por ejemplo, seleccionar las primeras 3 filas y las últimas 2
    filas_combinadas = pd.concat([df.iloc[:3], df.iloc[-2:]])
    print("3. Combinación de las primeras 3 y las últimas 2 filas:")
    print(filas_combinadas)
    print("\n" + "-"*40 + "\n")

    # 4. Mostrar estadísticas de las filas seleccionadas
    print("4. Estadísticas descriptivas de las filas combinadas:")
    print(filas_combinadas.describe())

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.rand(30, 3) * 100, columns=['A', 'B', 'C'])
seleccionar_multiples_filas(df_ejemplo)