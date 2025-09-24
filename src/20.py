import pandas as pd
import numpy as np
import time

def analisis_completo_con_iloc(df: pd.DataFrame):
    """
    Realiza un análisis completo de un DataFrame usando .iloc.
    
    Args:
        df: DataFrame de pandas.
    """
    print("--- Análisis de DataFrame con .iloc ---")
    print(f"Dimensiones del DataFrame: {df.shape}")
    print("\n" + "-"*40 + "\n")

    # 1. Crear diferentes vistas del DataFrame usando posiciones
    vista_completa = df.iloc[:, :]
    vista_cabecera = df.iloc[:5, :]
    vista_cuerpo = df.iloc[5:15, [0, 2]]
    
    print("1. Vistas creadas usando .iloc:")
    print(f"Vista Completa (primeras 5 filas):\n{vista_completa.head()}")
    print(f"\nVista Cabecera:\n{vista_cabecera}")
    print(f"\nVista Cuerpo (filas 5-14, columnas 0 y 2):\n{vista_cuerpo}")
    print("\n" + "-"*40 + "\n")
  
    inicio_aleatorio = time.time()
    muestra_aleatoria = df.sample(n=20)
    final_aleatorio = time.time()
    
    # Muestra sistemática
    inicio_sistematico = time.time()
    muestra_sistematica = df.iloc[::(len(df) // 20)]
    final_sistematico = time.time()
    
    print("2. Análisis de muestras (aleatoria vs. sistemática):")
    print(f"Estadísticas de la Muestra Aleatoria:\n{muestra_aleatoria.describe()}")
    print(f"\nEstadísticas de la Muestra Sistemática:\n{muestra_sistematica.describe()}")
    print(f"\nTiempo de muestreo aleatorio: {(final_aleatorio - inicio_aleatorio):.6f}s")
    print(f"Tiempo de muestreo sistemático: {(final_sistematico - inicio_sistematico):.6f}s")
    print("\n" + "-"*40 + "\n")

    
    t_lista = time.time()
    df.iloc[[0, 10, 20, 30, 40, 50]]
    t_lista_fin = time.time()
    
    t_rango = time.time()
    df.iloc[10:20]
    t_rango_fin = time.time()
    
    print("3. Comparación de rendimiento (lista vs. rango):")
    print(f"Tiempo de selección con lista de índices: {(t_lista_fin - t_lista):.6f}s")
    print(f"Tiempo de selección con rango: {(t_rango_fin - t_rango):.6f}s")
    print("\n" + "-"*40 + "\n")

    # 4. Generar un reporte completo con métricas
    reporte = pd.DataFrame({
        'Vista': ['Completa', 'Cabecera', 'Cuerpo'],
        'Filas': [len(vista_completa), len(vista_cabecera), len(vista_cuerpo)],
        'Columnas': [len(vista_completa.columns), len(vista_cabecera.columns), len(vista_cuerpo.columns)],
        'Promedio_Columna_0': [vista_completa.iloc[:, 0].mean(),
                               vista_cabecera.iloc[:, 0].mean(),
                               vista_cuerpo.iloc[:, 0].mean()]
    })
    print("4. Reporte de métricas de las selecciones:")
    print(reporte)

# Ejemplo de uso
df_ejemplo = pd.DataFrame(np.random.randint(0, 101, size=(50, 5)), 
                          columns=list('ABCDE'))
analisis_completo_con_iloc(df_ejemplo)