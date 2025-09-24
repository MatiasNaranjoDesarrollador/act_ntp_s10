import pandas as pd
import numpy as np

def seleccionar_empleados(df, ids=None, id_rango=None):
    if ids is not None and len(ids) == 1:
        empleado_unico = df.loc[ids[0]]
        print("--- Selección de un solo empleado (ID: {}) ---".format(ids[0]))
        print(empleado_unico)
        print("-" * 30)

    if ids is not None and len(ids) > 1:
        multiples_empleados = df.loc[ids]
        print("--- Selección de múltiples empleados (IDs: {}) ---".format(ids))
        print(multiples_empleados)
        print("-" * 30)

    if id_rango is not None and len(id_rango) == 2:
        rango_empleados = df.loc[id_rango[0]:id_rango[1]]
        print("--- Selección de un rango de empleados (IDs: {} a {}) ---".format(id_rango[0], id_rango[1]))
        print(rango_empleados)
        print("-" * 30)
    
    return None, None, None

datos_empleados = {
    'nombre': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Laura', 'Carlos'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing'],
    'salario': [50000, 60000, 55000, 52000, 62000, 58000],
    'antiguedad_anos': [5, 3, 2, 7, 4, 6]
}
df_empleados = pd.DataFrame(datos_empleados, index=np.arange(101, 107))
df_empleados.index.name = 'empleado_id'

print("--- DataFrame original ---")
print(df_empleados)
print("-" * 30)

seleccionar_empleados(df_empleados, ids=[102])

seleccionar_empleados(df_empleados, ids=[101, 104, 106])

seleccionar_empleados(df_empleados, id_rango=(103, 105))