# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:35:39 2025

@author: Juan Carlos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("datos_2025_limpios.csv")

# Convertir fecha y hora
df["FECHA_HORA"] = pd.to_datetime(df["FECHA_HORA"])
df = df.sort_values("FECHA_HORA")

variables = [
    "PM 2.5 [ug/m^3]", "PM 10 [ug/m^3]", "TEMPERATURA [°C]",
    "HUMEDAD [%]", "FORMALDEHIDO [mg/m^3]"
]

plt.figure(figsize=(15, 10))

for i, var in enumerate(variables, 1):
    plt.subplot(len(variables), 1, i)
    plt.plot(df["FECHA_HORA"], df[var], marker='', linestyle='-')
    plt.title(f"{var} a lo largo del tiempo")
    plt.grid(True)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
sns.boxplot(data=df[variables])
plt.title("Boxplot de variables ambientales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


df[variables].hist(bins=30, figsize=(15, 10), layout=(3, 2))
plt.tight_layout()
plt.suptitle("Distribución de datos", y=1.02)
plt.show()


plt.figure(figsize=(10, 8))
correlation_matrix = df[variables].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()