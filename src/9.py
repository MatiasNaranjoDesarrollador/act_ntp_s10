import pandas as pd
import numpy as np

def filtrar_grupos_complejos(df):
    """
    Combina múltiples tipos de filtros en un DataFrame de empleados y genera estadísticas.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # 1. Filtrar empleados activos, de IT o Finanzas, con salario > 60000 y edad < 45
    print("--- 1. Filtro Complejo: IT/Finanzas, Activos, Salario > 60k, Edad < 45 ---")
    filtro_complejo_1 = df.loc[
        (df['estatus'] == 'Activo') &
        (df['departamento'].isin(['IT', 'Finanzas'])) &
        (df['salario'] > 60000) &
        (df['edad'] < 45)
    ]
    
    print(f"Número de registros encontrados: {len(filtro_complejo_1)}")
    if not filtro_complejo_1.empty:
        print("\nResumen Estadístico del Grupo 1:")
        print(filtro_complejo_1[['salario', 'edad', 'antiguedad_anos']].describe())
    print("-" * 30)

    # 2. Filtrar empleados de ciudades específicas con experiencia > 10 años
    print("--- 2. Filtro Combinado: Ciudades específicas y Antigüedad > 10 años ---")
    ciudades_especificas = ['Medellín', 'Cali']
    filtro_complejo_2 = df.loc[
        (df['ciudad'].isin(ciudades_especificas)) &
        (df['antiguedad_anos'] > 10)
    ]
    
    print(f"Número de registros encontrados: {len(filtro_complejo_2)}")
    if not filtro_complejo_2.empty:
        print("\nResumen Estadístico del Grupo 2:")
        print(filtro_complejo_2[['salario', 'antiguedad_anos']].describe())
        print("\nConteo por Ciudad:")
        print(filtro_complejo_2['ciudad'].value_counts())
    print("-" * 30)


# 2. Crear un DataFrame de ejemplo
np.random.seed(42)
num_empleados = 30
datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Finanzas', 'Marketing'], num_empleados),
    'salario': np.random.randint(50000, 150000, num_empleados),
    'edad': np.random.randint(25, 60, num_empleados),
    'antiguedad_anos': np.random.randint(1, 15, num_empleados),
    'estatus': np.random.choice(['Activo', 'Inactivo'], num_empleados, p=[0.9, 0.1]),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], num_empleados)
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 5 filas) ---")
print(df_empleados.head())
print("-" * 30)

# 3. Ejecutar la función para aplicar los filtros complejos
filtrar_grupos_complejos(df_empleados.copy())