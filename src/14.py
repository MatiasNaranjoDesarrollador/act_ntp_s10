import pandas as pd
import numpy as np

def seleccionar_columnas_iloc(df: pd.DataFrame):
    """
    Selecciona columnas de un DataFrame usando .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (primeras 5 filas) ---")
    print(df.head())
    print("\n" + "-"*40 + "\n")

    # 1. Seleccionar las primeras 3 columnas
    primeras_3_columnas = df.iloc[:, :3]
    print("1. Las primeras 3 columnas:")
    print(primeras_3_columnas.head())
    print("\n" + "-"*40 + "\n")

    # 2. Seleccionar columnas específicas por posición
    columnas_especificas = df.iloc[:, [0, 2, 4]]
    print("2. Columnas específicas (posiciones 0, 2 y 4):")
    print(columnas_especificas.head())
    print("\n" + "-"*40 + "\n")
    
    # 3. Seleccionar la última columna
    ultima_columna = df.iloc[:, -1]
    print("3. La última columna:")
    print(ultima_columna.head())
    print("\n" + "-"*40 + "\n")
    
    # 4. Combinar selección de filas y columnas
    # Seleccionar las primeras 5 filas y las columnas 1, 3 y 5
    subconjunto = df.iloc[:5, [1, 3, 5]]
    print("4. Combinación: primeras 5 filas y columnas en posiciones 1, 3 y 5:")
    print(subconjunto)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 10, size=(10, 6)), 
                          columns=[f'Col_{i}' for i in range(1, 7)])
seleccionar_columnas_iloc(df_ejemplo)