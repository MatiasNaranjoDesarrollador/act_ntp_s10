import pandas as pd
import numpy as np

def trabajar_con_listas_de_indices(df: pd.DataFrame):
    """
    Genera y usa listas de índices dinámicas para la selección con .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (primeras 5 filas) ---")
    print(df.head())
    print("\n" + "-"*40 + "\n")
    
    # 1. Generar listas de índices basadas en condiciones
    # Encontrar los índices de las filas donde 'Col_A' es par
    indices_pares = df[df['Col_A'] % 2 == 0].index.tolist()
    filas_pares = df.iloc[indices_pares]
    print("1. Filas donde 'Col_A' es un número par:")
    print(filas_pares.head())
    print("\n" + "-"*40 + "\n")

    # 2. Encontrar posiciones que cumplan criterios específicos
    # Usar np.where para encontrar posiciones de valores > 80 en 'Col_B'
    indices_grandes = np.where(df['Col_B'] > 80)[0]
    filas_grandes = df.iloc[indices_grandes]
    print("2. Filas donde 'Col_B' es mayor a 80:")
    print(filas_grandes)
    print("\n" + "-"*40 + "\n")
    
    # 3. Seleccionar filas basadas en percentiles
    # Encontrar el valor del percentil 75 de 'Col_C'
    percentil_75 = df['Col_C'].quantile(0.75)
    filas_percentil = df[df['Col_C'] > percentil_75]
    print(f"3. Filas donde 'Col_C' es mayor al percentil 75 ({percentil_75:.2f}):")
    print(filas_percentil)
    print("\n" + "-"*40 + "\n")

    # 4. Mostrar diferentes muestras del DataFrame
    muestra_aleatoria = df.sample(n=5, random_state=1)
    print("4. Muestra aleatoria de 5 filas:")
    print(muestra_aleatoria)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 101, size=(25, 3)), 
                          columns=['Col_A', 'Col_B', 'Col_C'])
trabajar_con_listas_de_indices(df_ejemplo)