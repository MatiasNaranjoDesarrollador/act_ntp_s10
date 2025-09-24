import pandas as pd
import numpy as np

def seleccion_avanzada_iloc(df: pd.DataFrame):
    """
    Realiza selecciones complejas en un DataFrame usando .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- DataFrame Original (primeras 5 filas) ---")
    print(df.head())
    print("\n" + "-"*40 + "\n")

    # 1. Seleccionar subconjuntos específicos del DataFrame
    # Seleccionar las primeras 5 filas y las columnas en las posiciones 0, 2 y 4
    subconjunto_especifico = df.iloc[:5, [0, 2, 4]]
    print("1. Subconjunto específico (primeras 5 filas, columnas 0, 2 y 4):")
    print(subconjunto_especifico)
    print("\n" + "-"*40 + "\n")

    # 2. Usar arrays booleanos con .iloc
    # Se debe usar .loc para la indexación booleana, no .iloc.
    # Usaremos .loc para la condición y .iloc para la selección por posición.
    # Ejemplo: seleccionar filas donde la 'Columna_A' > 50
    condicion_booleana = df['Columna_A'] > 50
    filas_filtradas = df.loc[condicion_booleana]
    print("2. Filas donde 'Columna_A' es mayor a 50:")
    print(filas_filtradas.head())
    print("\n" + "-"*40 + "\n")

    # 3. Combinar .iloc con funciones de agregación
    # Obtener el promedio de las primeras 5 filas y las primeras 3 columnas
    promedio_subconjunto = df.iloc[:5, :3].mean()
    print("3. Promedio de las primeras 5 filas y 3 columnas:")
    print(promedio_subconjunto)
    print("\n" + "-"*40 + "\n")
    
    # 4. Crear vistas personalizadas del DataFrame
    # Crear una vista que solo contenga los datos de las filas 5 a 10
    vista_personalizada = df.iloc[5:11].copy()
    print("4. Vista personalizada de las filas 5 a 10:")
    print(vista_personalizada)
    print("\n" + "-"*40 + "\n")

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 100, size=(20, 5)), 
                          columns=[f'Columna_{chr(65+i)}' for i in range(5)])
seleccion_avanzada_iloc(df_ejemplo)