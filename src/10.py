import pandas as pd
import numpy as np

def analisis_completo_con_loc(df):
    """
    Realiza un análisis completo de un DataFrame de empleados usando .loc.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    df_analisis = df.copy()

    # --- 1. Crear Vistas del DataFrame con .loc ---
    print("### 1. Vistas del DataFrame")
    
    # Vista 1: Empleados de IT con salario > 80000
    it_senior = df_analisis.loc[(df_analisis['departamento'] == 'IT') & (df_analisis['salario'] > 80000)]
    print("\n--- Empleados Senior de IT ---")
    print(f"Número de registros: {len(it_senior)}")
    print(it_senior[['nombre', 'salario', 'antiguedad_anos']].head())
    print("-" * 30)

    # Vista 2: Empleados de Ventas o Marketing
    ventas_marketing = df_analisis.loc[df_analisis['departamento'].isin(['Ventas', 'Marketing'])]
    print("--- Empleados de Ventas o Marketing ---")
    print(f"Número de registros: {len(ventas_marketing)}")
    print(ventas_marketing[['nombre', 'departamento']].head())
    print("-" * 30)

    # --- 2. Calcular Métricas por Departamento y Ciudad ---
    print("### 2. Métricas por Departamento y Ciudad")

    # Salario promedio por departamento
    promedio_departamento = df_analisis.loc[:, ['departamento', 'salario']].groupby('departamento').mean()
    print("\n--- Salario Promedio por Departamento ---")
    print(promedio_departamento)
    print("-" * 30)

    # Conteo de empleados por ciudad
    conteo_ciudad = df_analisis.loc[:, ['ciudad', 'nombre']].groupby('ciudad').count().rename(columns={'nombre': 'num_empleados'})
    print("--- Conteo de Empleados por Ciudad ---")
    print(conteo_ciudad)
    print("-" * 30)

    # --- 3. Identificar Empleados con Características Específicas ---
    print("### 3. Empleados Clave")
    
    # Identificar Top Performers (salario > 90% percentil)
    salario_percentil_90 = df_analisis['salario'].quantile(0.90)
    top_performers = df_analisis.loc[df_analisis['salario'] > salario_percentil_90]
    print("\n--- Top Performers (Salario > 90% Percentil) ---")
    print(f"Salario mínimo para ser Top Performer: ${salario_percentil_90:.2f}")
    print(top_performers[['nombre', 'departamento', 'salario', 'antiguedad_anos']])
    print("-" * 30)

    # Identificar Empleados Nuevos (menos de 2 años de antigüedad)
    empleados_nuevos = df_analisis.loc[df_analisis['antiguedad_anos'] < 2]
    print("--- Empleados Nuevos (Antigüedad < 2 años) ---")
    print(f"Número de empleados nuevos: {len(empleados_nuevos)}")
    print(empleados_nuevos[['nombre', 'departamento', 'antiguedad_anos']])
    print("-" * 30)

    # --- 4. Generar Reporte Final ---
    print("### 4. Reporte Completo del Análisis")
    total_empleados = len(df_analisis)
    salario_promedio_general = df_analisis['salario'].mean()
    
    reporte = pd.DataFrame({
        'Métrica': [
            'Total de Empleados',
            'Salario Promedio General',
            'Empleados en IT con salario > 80k',
            'Empleados en Ventas/Marketing',
            'Antigüedad Promedio (Años)',
            'Top Performers (Salario > P90)'
        ],
        'Valor': [
            total_empleados,
            f"${salario_promedio_general:.2f}",
            len(it_senior),
            len(ventas_marketing),
            df_analisis['antiguedad_anos'].mean(),
            len(top_performers)
        ]
    })
    print(reporte)

# 2. Crear un DataFrame de ejemplo para el análisis
np.random.seed(42)
num_empleados = 50
datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing', 'Finanzas'], num_empleados),
    'salario': np.random.randint(50000, 150000, num_empleados),
    'edad': np.random.randint(25, 60, num_empleados),
    'antiguedad_anos': np.random.randint(1, 15, num_empleados),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], num_empleados)
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 5 filas) ---")
print(df_empleados.head())
print("-" * 30)

# 3. Ejecutar la función de análisis
analisis_completo_con_loc(df_empleados.copy())