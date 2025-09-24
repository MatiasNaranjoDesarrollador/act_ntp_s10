import pandas as pd
import numpy as np

def seleccionar_filas_por_rango(df: pd.DataFrame):
    """
    Selecciona filas de un DataFrame usando rangos con .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original ---")
    print(df)
    print("\n")

   
    filas_10_a_20 = df.iloc[9:20]
    print("1. Filas del 10 al 20 (índices 9 a 19):")
    print(filas_10_a_20)
    print("\n" + "-"*40 + "\n")

    # Seleccionar las últimas 10 filas
    ultimas_10 = df.iloc[-10:]
    print("2. Últimas 10 filas:")
    print(ultimas_10)
    print("\n" + "-"*40 + "\n")

    # Seleccionar filas pares
    filas_pares = df.iloc[::2]
    print("3. Filas pares (índice 0, 2, 4, etc.):")
    print(filas_pares)
    print("\n" + "-"*40 + "\n")

    # Seleccionar cada tercera fila
    cada_tercera = df.iloc[::3]
    print("4. Cada tercera fila:")
    print(cada_tercera)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 100, size=(30, 4)), columns=list('ABCD'))
seleccionar_filas_por_rango(df_ejemplo)