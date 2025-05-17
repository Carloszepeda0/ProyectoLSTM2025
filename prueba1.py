import pandas as pd
import matplotlib.pyplot as plt




# 1️⃣ Cargar el CSV
df = pd.read_csv("datos_calidad_aire.csv", skipinitialspace=True)

# 2️⃣ Limpiar nombres de columnas (por si tienen espacios al inicio o al final)
df.columns = df.columns.str.strip()

# 3️⃣ Limpiar espacios o tabulaciones raras en las columnas FECHA y HORA
df["FECHA"] = df["FECHA"].astype(str).str.strip()
df["HORA"] = df["HORA"].astype(str).str.strip()

# 4️⃣ Unir FECHA y HORA en una sola columna y convertir a tipo datetime
df["FECHA_HORA"] = pd.to_datetime(
    df["FECHA"] + " " + df["HORA"],
    format="%Y/%m/%d %H:%M:%S",  # Formato de tus datos
    errors="coerce"  # Si hay errores los pone como NaT
)

# 5️⃣ Eliminar filas con errores en la fecha (opcional pero recomendable)
df = df.dropna(subset=["FECHA_HORA"])

# 6️⃣ Filtrar solo los datos del año 2025
df_2025 = df[df["FECHA_HORA"].dt.year == 2025]

# 7️⃣ Mostrar los primeros datos del año 2025
print(df_2025.head())

df_2025.to_csv("datos_2025_limpios.csv", index=False)


|||