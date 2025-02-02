import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos (ajusta el nombre del archivo y la hoja si es necesario)
df = pd.read_excel("Tarifas por puntos 2016-2017.csv.xlsx", sheet_name="in")

# Convertir la columna de fecha al formato correcto (ajusta el formato si es necesario)
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'], format='%Y-%m-%d')

# Seleccionar la columna de la tarifa (reemplaza 'uso_base_firme' si es necesario)
columna_tarifa = 'uso_base_firme'

# Gráfico de línea (variación de tarifas a lo largo del tiempo)
sns.lineplot(x='fecha_inicio', y=columna_tarifa, data=df)
plt.title('Variación de Tarifas a lo largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Tarifa')
plt.show()

# Gráfico de barras (máximos y mínimos por mes y año)
df['Mes'] = df['fecha_inicio'].dt.month
df['Año'] = df['fecha_inicio'].dt.year
df_agrupado = df.groupby(['Año', 'Mes'])[columna_tarifa].agg(['min', 'max']).reset_index()
sns.barplot(x='Mes', y='value', hue='variable', data=pd.melt(df_agrupado, id_vars=['Año', 'Mes'], value_vars=['min', 'max']))
plt.title('Máximos y Mínimos de Tarifas por Mes y Año')
plt.xlabel('Mes')
plt.ylabel('Tarifa')
plt.legend(title='Tipo')
plt.show()