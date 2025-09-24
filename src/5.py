import pandas as pd
import numpy as np

def modificar_datos_con_loc(df):
    """
    Modifica los datos de un DataFrame de empleados usando .loc.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    df_original = df.copy()

    # 1. Aumentar el salario en 10% a empleados de IT
    print("--- 1. Aumento de salario para empleados de IT ---")
    print("DataFrame antes del cambio:")
    print(df_original.loc[df_original['departamento'] == 'IT', ['nombre', 'salario']])
    
    df.loc[df['departamento'] == 'IT', 'salario'] *= 1.10
    
    print("\nDataFrame después del cambio:")
    print(df.loc[df['departamento'] == 'IT', ['nombre', 'salario']])
    print("-" * 30)

    # 2. Cambiar el estado a 'Inactivo' para empleados mayores de 60 años
    print("--- 2. Cambio de estatus a 'Inactivo' para empleados > 60 años ---")
    print("DataFrame antes del cambio:")
    print(df_original.loc[df_original['edad'] > 60, ['nombre', 'edad', 'estatus']])
    
    df.loc[df['edad'] > 60, 'estatus'] = 'Inactivo'
    
    print("\nDataFrame después del cambio:")
    print(df.loc[df['edad'] > 60, ['nombre', 'edad', 'estatus']])
    print("-" * 30)

    # 3. Actualizar la ciudad a 'Bogotá' para empleados de RRHH
    print("--- 3. Actualización de ciudad a 'Bogotá' para empleados de RRHH ---")
    print("DataFrame antes del cambio:")
    print(df_original.loc[df_original['departamento'] == 'RRHH', ['nombre', 'departamento', 'ciudad']])
    
    df.loc[df['departamento'] == 'RRHH', 'ciudad'] = 'Bogotá'
    
    print("\nDataFrame después del cambio:")
    print(df.loc[df['departamento'] == 'RRHH', ['nombre', 'departamento', 'ciudad']])
    print("-" * 30)
    
    return df

# 1. Crear un DataFrame de ejemplo
np.random.seed(42)
num_empleados = 15
datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing', 'RRHH'], num_empleados),
    'salario': np.random.randint(50000, 150000, num_empleados),
    'edad': np.random.randint(25, 70, num_empleados),
    'estatus': np.random.choice(['Activo', 'Inactivo'], num_empleados, p=[0.9, 0.1]),
    'ciudad': np.random.choice(['Medellín', 'Cali', 'Barranquilla', 'Bogotá'], num_empleados)
}
df_empleados = pd.DataFrame(datos_empleados)

# 2. Ejecutar la función para realizar las modificaciones
df_modificado = modificar_datos_con_loc(df_empleados.copy())