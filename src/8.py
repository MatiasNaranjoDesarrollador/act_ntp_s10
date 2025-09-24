import pandas as pd
import numpy as np

def clasificar_salario(salario):
    """Clasifica un salario en 'Bajo', 'Medio' o 'Alto'."""
    if salario < 60000:
        return 'Bajo'
    elif 60000 <= salario < 90000:
        return 'Medio'
    else:
        return 'Alto'

def analisis_salarios_avanzado(df):
    """
    Realiza un análisis avanzado de salarios usando .loc y funciones.

    Args:
        df (pd.DataFrame): El DataFrame de empleados.
    """

    # 1. Crear una nueva columna con la clasificación de salarios
    df['categoria_salario'] = df['salario'].apply(clasificar_salario)
    
    # 2. Filtrar empleados con salario superior al promedio
    salario_promedio = df['salario'].mean()
    salario_por_encima_del_promedio = df.loc[df['salario'] > salario_promedio]
    print("--- Empleados con salario superior al promedio ---")
    print(f"Salario promedio: ${salario_promedio:.2f}")
    print(f"Número de registros: {len(salario_por_encima_del_promedio)}")
    print("Distribución de salarios en este grupo:")
    print(salario_por_encima_del_promedio['categoria_salario'].value_counts())
    print("-" * 30)

    # 3. Filtrar empleados con salario en el percentil 75
    # La sintaxis .quantile() calcula el percentil 75
    q75 = df['salario'].quantile(0.75)
    salario_en_percentil_75 = df.loc[df['salario'] > q75]
    print("--- Empleados con salario en el percentil 75 ---")
    print(f"Salario del percentil 75 (Q3): ${q75:.2f}")
    print(f"Número de registros: {len(salario_en_percentil_75)}")
    print("Distribución de salarios en este grupo:")
    print(salario_en_percentil_75['categoria_salario'].value_counts())
    print("-" * 30)
    
    return df

# 2. Crear un DataFrame de ejemplo
np.random.seed(42)
num_empleados = 30
datos_empleados = {
    'nombre': [f'Empleado_{i}' for i in range(num_empleados)],
    'departamento': np.random.choice(['IT', 'Ventas', 'Marketing', 'RRHH'], num_empleados),
    'salario': np.random.randint(45000, 150000, num_empleados)
}
df_empleados = pd.DataFrame(datos_empleados)

print("--- DataFrame original (primeras 5 filas) ---")
print(df_empleados.head())
print("-" * 30)

# 3. Ejecutar la función para realizar el análisis avanzado
df_analizado = analisis_salarios_avanzado(df_empleados.copy())