import pandas as pd
import numpy as np

def modificar_datos_iloc(df: pd.DataFrame):
    """
    Modifica datos en un DataFrame usando .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (antes de la modificación) ---")
    print(df)
    print("\n" + "-"*40 + "\n")

    # 1. Modificar valores en posiciones específicas
    df.iloc[0, 0] = 999
    df.iloc[2, 3] = 888
    print("1. Valores en (0, 0) y (2, 3) modificados:")
    print(df)
    print("\n" + "-"*40 + "\n")

    # 2. Modificar un rango de celdas
    df.iloc[1:4, 1:3] = 777
    print("2. Rango de celdas (filas 1 a 3, columnas 1 a 2) modificado a 777:")
    print(df)
    print("\n" + "-"*40 + "\n")

    # 3. Modificar múltiples columnas a la vez
    df.iloc[:, [0, 2]] = df.iloc[:, [0, 2]] * 10
    print("3. Columnas 0 y 2 multiplicadas por 10:")
    print(df)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 10, size=(5, 4)), 
                          columns=list('ABCD'))
modificar_datos_iloc(df_ejemplo)