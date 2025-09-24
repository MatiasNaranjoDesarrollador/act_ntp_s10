import pandas as pd
import numpy as np

def filtrar_empleados_multiples_condiciones(df):
    """
    Filtra un DataFrame de empleados usando múltiples condiciones con .loc y muestra estadísticas.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # 1. Filtrar empleados de IT con salario mayor a 70000
    it_salario_alto = df.loc[(df['departamento'] == 'IT') & (df['salario'] > 70000)]
    print("--- Empleados de IT con salario > 70000 ---")
    print(f"Número de registros: {len(it_salario_alto)}")
    print("Estadísticas del salario:")
    print(it_salario_alto['salario'].describe())
    print("-" * 30)

    # 2. Filtrar empleados de Ventas o Marketing
    ventas_o_marketing = df.loc[(df['departamento'] == 'Ventas') | (df['departamento'] == 'Marketing')]
    print("--- Empleados de Ventas o Marketing ---")
    print(f"Número de registros: {len(ventas_o_marketing)}")
    print("Conteo por departamento:")
    print(ventas_o_marketing['departamento'].value_counts())
    print("-" * 30)

    # 3. Filtrar empleados con más de 5 años de experiencia y activos
    empleados_senior_activos = df.loc[(df['antiguedad_anos'] > 5) & (df['estatus'] == 'Activo')]
    print("--- Empleados activos con > 5 años de experiencia ---")
    print(f"Número de registros: {len(empleados_senior_activos)}")
    print("Estadísticas de antigüedad:")
    print(empleados_senior_activos['antiguedad_anos'].describe())
    print("-" * 30)


# 1. Crear un DataFrame de ejemplo
datos_empleados = {
    'nombre': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Laura', 'Carlos', 'Elena', 'Diego'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing', 'Ventas', 'IT'],
    'salario': [65000, 85000, 72000, 95000, 78000, 68000, 88000, 92000],
    'antiguedad_anos': [3, 7, 4, 6, 2, 5, 8, 9],
    'estatus': ['Activo', 'Activo', 'Activo', 'Activo', 'Activo', 'Inactivo', 'Activo', 'Activo']
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original ---")
print(df_empleados)
print("-" * 30)

# 2. Ejecutar la función para aplicar los filtros y mostrar estadísticas
filtrar_empleados_multiples_condiciones(df_empleados)