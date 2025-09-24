import pandas as pd
import numpy as np

def filtrar_por_string_con_loc(df):
    """
    Filtra un DataFrame de empleados usando métodos de string con .loc.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """
    
    # 1. Filtrar empleados cuyo nombre contenga el dígito '1'
    # La sintaxis .str.contains() permite buscar un patrón de texto dentro de la columna.
    nombres_con_1 = df.loc[df['nombre'].str.contains('1', na=False)]
    print("--- Empleados cuyo nombre contiene '1' ---")
    print(f"Número de registros: {len(nombres_con_1)}")
    if not nombres_con_1.empty:
        print("Conteo de departamentos:")
        print(nombres_con_1['departamento'].value_counts())
    print("-" * 30)

    # 2. Filtrar empleados cuyo apellido termine en '5'
    # La sintaxis .str.endswith() verifica si el string termina con un patrón específico.
    apellidos_con_5 = df.loc[df['apellido'].str.endswith('5', na=False)]
    print("--- Empleados cuyo apellido termina en '5' ---")
    print(f"Número de registros: {len(apellidos_con_5)}")
    if not apellidos_con_5.empty:
        print("Salario promedio:")
        print(apellidos_con_5['salario'].mean())
    print("-" * 30)

    # 3. Filtrar empleados de ciudades que empiecen con 'B'
    # La sintaxis .str.startswith() verifica si el string empieza con un patrón específico.
    ciudades_con_b = df.loc[df['ciudad'].str.startswith('B', na=False)]
    print("--- Empleados de ciudades que empiezan con 'B' ---")
    print(f"Número de registros: {len(ciudades_con_b)}")
    if not ciudades_con_b.empty:
        print("Ciudades encontradas:")
        print(ciudades_con_b['ciudad'].unique())
    print("-" * 30)

# 1. Crear un DataFrame de ejemplo
np.random.seed(42)
num_empleados = 20
nombres = [f'Juan_{i}' for i in range(10)] + [f'Ana_{i}' for i in range(10)]
apellidos = [f'Perez_{i}' for i in range(10)] + [f'Gomez_{i}' for i in range(10)]
ciudades = np.random.choice(['Bogotá', 'Barranquilla', 'Medellín', 'Cali'], num_empleados)

datos_empleados = {
    'nombre': nombres,
    'apellido': apellidos,
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing'], num_empleados),
    'salario': np.random.randint(50000, 150000, num_empleados),
    'ciudad': ciudades
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 5 filas) ---")
print(df_empleados.head())
print("-" * 30)

# 2. Ejecutar la función para aplicar los filtros
filtrar_por_string_con_loc(df_empleados)