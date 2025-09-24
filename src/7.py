import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def filtrar_por_fechas_con_loc(df):
    """
    Filtra un DataFrame de empleados por fechas usando .loc y calcula la antigüedad promedio.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # Asegurar que la columna 'fecha_contratacion' sea de tipo datetime
    df['fecha_contratacion'] = pd.to_datetime(df['fecha_contratacion'])
    
    # 1. Filtrar empleados que ingresaron en 2022
    # La sintaxis .dt.year permite extraer el año de la columna datetime
    empleados_2022 = df.loc[df['fecha_contratacion'].dt.year == 2022]
    print("--- Empleados que ingresaron en 2022 ---")
    print(f"Número de registros: {len(empleados_2022)}")
    if not empleados_2022.empty:
        antiguedad_promedio = (datetime.now() - empleados_2022['fecha_contratacion']).dt.days.mean() / 365.25
        print(f"Antigüedad promedio del grupo: {antiguedad_promedio:.2f} años")
    print("-" * 30)

    # 2. Filtrar empleados que ingresaron en los últimos 2 años
    # Se calcula la fecha de hace 2 años y se usa como condición
    fecha_hace_2_anos = datetime.now() - timedelta(days=2*365.25)
    ultimos_2_anos = df.loc[df['fecha_contratacion'] >= fecha_hace_2_anos]
    print("--- Empleados que ingresaron en los últimos 2 años ---")
    print(f"Número de registros: {len(ultimos_2_anos)}")
    if not ultimos_2_anos.empty:
        antiguedad_promedio = (datetime.now() - ultimos_2_anos['fecha_contratacion']).dt.days.mean() / 365.25
        print(f"Antigüedad promedio del grupo: {antiguedad_promedio:.2f} años")
    print("-" * 30)
    
    # 3. Filtrar empleados que ingresaron en el primer trimestre de cualquier año
    # Se utiliza .dt.quarter para identificar el trimestre de la fecha
    primer_trimestre = df.loc[df['fecha_contratacion'].dt.quarter == 1]
    print("--- Empleados que ingresaron en el primer trimestre ---")
    print(f"Número de registros: {len(primer_trimestre)}")
    if not primer_trimestre.empty:
        antiguedad_promedio = (datetime.now() - primer_trimestre['fecha_contratacion']).dt.days.mean() / 365.25
        print(f"Antigüedad promedio del grupo: {antiguedad_promedio:.2f} años")
    print("-" * 30)
    
    return df

# 1. Crear un DataFrame de ejemplo
num_empleados = 20
np.random.seed(42)
fechas_contratacion = pd.to_datetime(pd.date_range(start='2018-01-01', end='2024-12-31', periods=num_empleados))

datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing'], num_empleados),
    'salario': np.random.randint(50000, 150000, num_empleados),
    'fecha_contratacion': fechas_contratacion
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 5 filas) ---")
print(df_empleados.head())
print("-" * 30)

# 2. Ejecutar la función para aplicar los filtros
filtrar_por_fechas_con_loc(df_empleados.copy())