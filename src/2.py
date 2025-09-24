import pandas as pd
import numpy as np

def filtrar_empleados_condicional(df):
    """
    Filtra un DataFrame de empleados usando condiciones con .loc.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # 1. Filtrar empleados mayores de 40 años
    mayores_40 = df.loc[df['edad'] > 40]
    print("--- Empleados mayores de 40 años ---")
    print(f"Número de registros encontrados: {len(mayores_40)}")
    print(mayores_40)
    print("-" * 30)

    # 2. Filtrar empleados del departamento 'IT'
    departamento_it = df.loc[df['departamento'] == 'IT']
    print("--- Empleados del departamento 'IT' ---")
    print(f"Número de registros encontrados: {len(departamento_it)}")
    print(departamento_it)
    print("-" * 30)

    # 3. Filtrar empleados con salario mayor a 80000
    salario_alto = df.loc[df['salario'] > 80000]
    print("--- Empleados con salario mayor a 80000 ---")
    print(f"Número de registros encontrados: {len(salario_alto)}")
    print(salario_alto)
    print("-" * 30)

# 1. Crear un DataFrame de ejemplo
datos_empleados = {
    'nombre': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Laura', 'Carlos', 'María', 'José'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas'],
    'salario': [75000, 92000, 65000, 85000, 105000, 72000, 98000, 88000],
    'edad': [35, 42, 28, 45, 51, 38, 48, 41]
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original ---")
print(df_empleados)
print("-" * 30)

# 2. Ejecutar la función para aplicar los filtros
filtrar_empleados_condicional(df_empleados)