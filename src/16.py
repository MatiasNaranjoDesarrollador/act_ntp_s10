import pandas as pd
import numpy as np

def seleccion_con_pasos_iloc(df: pd.DataFrame):
    """
    Selecciona filas y columnas con pasos usando .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (primeras 10 filas) ---")
    print(df.head(10))
    print("\n" + "-"*40 + "\n")

    # 1. Seleccionar cada segunda fila
    cada_segunda_fila = df.iloc[::2]
    print("1. Cada segunda fila:")
    print(cada_segunda_fila.head())
    print("\n" + "-"*40 + "\n")
    
    # 2. Seleccionar filas en orden inverso
    filas_inversas = df.iloc[::-1]
    print("2. Filas en orden inverso:")
    print(filas_inversas.head())
    print("\n" + "-"*40 + "\n")

    # 3. Seleccionar cada quinta fila empezando desde la tercera posición
    cada_quinta_desde_tercera = df.iloc[2::5]
    print("3. Cada quinta fila empezando desde el índice 2:")
    print(cada_quinta_desde_tercera.head())
    print("\n" + "-"*40 + "\n")

    # 4. Combinar pasos en filas y columnas
    # Seleccionar cada tercera fila y cada segunda columna
    pasos_combinados = df.iloc[::3, ::2]
    print("4. Combinación: cada tercera fila y cada segunda columna:")
    print(pasos_combinados.head())
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 100, size=(20, 5)))
seleccion_con_pasos_iloc(df_ejemplo)