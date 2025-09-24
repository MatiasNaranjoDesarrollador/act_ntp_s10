import pandas as pd

def seleccionar_filas_iloc(df: pd.DataFrame) -> None:
    """
    Demuestra la selección de filas usando .iloc en un DataFrame.

    Args:
        df: El DataFrame de pandas en el que se realizarán las selecciones.
    """
    print("--- DataFrame Original ---")
    print(df)
    print("\n" + "-"*30 + "\n")

    # 1. Seleccionar la primera fila
    primera_fila = df.iloc[0]
    print("1. Primera fila:")
    print(primera_fila)
    print("\n" + "-"*30 + "\n")

    # 2. Seleccionar las primeras 5 filas
    primeras_5_filas = df.iloc[:5]
    print("2. Primeras 5 filas:")
    print(primeras_5_filas)
    print("\n" + "-"*30 + "\n")

    # 3. Seleccionar la última fila
    ultima_fila = df.iloc[-1]
    print("3. Última fila:")
    print(ultima_fila)
    print("\n" + "-"*30 + "\n")

    # 4. Seleccionar filas específicas por posición (ej. filas 2, 4 y 6)
    filas_especificas = df.iloc[[1, 3, 5]]
    print("4. Filas específicas (índices 1, 3, 5):")
    print(filas_especificas)
    print("\n" + "-"*30 + "\n")

# Crear un DataFrame de ejemplo
data = {'A': range(1, 11),
        'B': [f'valor_{i}' for i in range(1, 11)],
        'C': [i*10 for i in range(1, 11)]}
df_ejemplo = pd.DataFrame(data)

# Ejecutar la función
seleccionar_filas_iloc(df_ejemplo)