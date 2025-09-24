import pandas as pd
import numpy as np

def combinaciones_de_iloc(df: pd.DataFrame):
    """
    Combina diferentes usos de .iloc para crear vistas y muestras.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (primeras 10 filas) ---")
    print(df.head(10))
    print("\n" + "-"*40 + "\n")
    
    # 1. Crear múltiples vistas usando diferentes patrones de selección
    vista_1 = df.iloc[:5, ::2]  # Filas 0-4, columnas pares
    vista_2 = df.iloc[10:15, [0, 2, 4]] # Filas 10-14, columnas 0, 2 y 4
    print("1. Múltiples vistas del DataFrame:")
    print("Vista 1 (primeras 5 filas, columnas pares):")
    print(vista_1)
    print("\nVista 2 (filas 10-14, columnas 0, 2, 4):")
    print(vista_2)
    print("\n" + "-"*40 + "\n")

    # 2. Combinar selección aleatoria con selección sistemática
    # Seleccionar 3 filas aleatorias y luego cada 3ª fila de esas
    df_random = df.sample(n=10, random_state=42)
    muestra_combinada = df_random.iloc[::3]
    print("2. Muestra combinada (aleatoria + sistemática):")
    print(muestra_combinada)
    print("\n" + "-"*40 + "\n")

 
    estrato_A = df.iloc[:10].sample(n=2)
    estrato_B = df.iloc[10:].sample(n=2)
    muestra_estratificada = pd.concat([estrato_A, estrato_B])
    print("3. Muestra estratificada (simulada):")
    print(muestra_estratificada)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 100, size=(20, 5)), 
                          columns=list('ABCDE'))
combinaciones_de_iloc(df_ejemplo)