import pandas as pd
import numpy as np

def seleccionar_columnas_loc(df):
    """
    Selecciona columnas específicas de un DataFrame usando .loc.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # 1. Seleccionar solo nombre y salario de todos los empleados
    nombre_salario = df.loc[:, ['nombre', 'salario']]
    print("--- Selección de 'nombre' y 'salario' para todos los empleados ---")
    print(nombre_salario.head(10))
    print("-" * 30)

    # 2. Seleccionar un rango de columnas desde 'nombre' hasta 'departamento'
    rango_columnas = df.loc[:, 'nombre':'departamento']
    print("--- Selección de columnas desde 'nombre' hasta 'departamento' ---")
    print(rango_columnas.head(10))
    print("-" * 30)

    # 3. Combinar filtro de filas y columnas para empleados mayores de 50 años
    mayores_50_filtrado = df.loc[df['edad'] > 50, ['nombre', 'departamento', 'salario']]
    print("--- Empleados mayores de 50 años, mostrando 'nombre', 'departamento' y 'salario' ---")
    print(mayores_50_filtrado.head(10))
    print("-" * 30)

# 1. Crear un DataFrame de ejemplo
num_empleados = 20
np.random.seed(42)
datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing', 'RRHH'], num_empleados),
    'salario': np.random.randint(45000, 120000, num_empleados),
    'edad': np.random.randint(25, 65, num_empleados)
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 10 filas) ---")
print(df_empleados.head(10))
print("-" * 30)

# 2. Ejecutar la función para aplicar las selecciones
seleccionar_columnas_loc(df_empleados)