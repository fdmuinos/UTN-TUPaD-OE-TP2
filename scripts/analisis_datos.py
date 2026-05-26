import pandas as pd
import os
import matplotlib.pyplot as plt

def importar_datos(nombre_archivo):
  """
  Busca e importa el dataset en el que se necesita trabajar. 
  """

  # Verificar si el archivo existe
  if not os.path.exists(nombre_archivo):
    raise FileNotFoundError(f"ERROR: No se encontró el archivo {nombre_archivo}.")

  # Leer el archivo con Pandas
  df = pd.read_csv(nombre_archivo)    
  print("Archivo cargado con éxito.")

  return df

def procesar_datos():
  """
  Calcula el promedio mensual de la temperatura, su valor mínimo, máximo
  y precipitación del año 2025 en Buenos Aires.
  Exporta una tabla con los valores agregados y un gráfico de la variación
  de la temperatura media a lo largo del año.
  """
  df = importar_datos("datos/dataset.csv")

  # Convertir columna 'date' en datatime y establecerla como índice.
  df['date'] = pd.to_datetime(df["date"])
  df.set_index('date', inplace=True)

  # Agregación mensual
  resumen_mensual = df.resample('ME').agg({
    'tavg' : 'mean',
    'tmin' : 'min',
    'tmax' : 'max',
    'prcp' : 'mean'
  })

  # Renombrar columnas
  resumen_mensual.columns = [
    'Temp_Promedio_Mensual',
    'Temp_Min_Absoluta',
    'Temp_Max_Absoluta',
    'Prcp_Promedio_Mensual'
  ]

  # Redondeo a dos decimales
  resumen_mensual = resumen_mensual.round(2)

  # Formateo de los índices
  resumen_mensual.index = resumen_mensual.index.strftime('%B')

  # Exportación de la tabla a archivo CSV
  nombre_csv = "resultados/resumen_clima_buenos_aires_2025.csv"
  resumen_mensual.to_csv(nombre_csv, index_label='Mes')
  print(f'Tabla exportada con éxito en "{nombre_csv}"')

  # Gráfico del promedio de la temperatura en durante el año.
  plt.figure(figsize=(12, 6))
  plt.plot(df.index, df['tavg'], label='Temp Promedio Diaria', color='teal', alpha=0.7, linewidth=1.5)
  plt.fill_between(df.index, df['tmin'], df['tmax'], color='orange', alpha=0.15, label='Rango Máx/Mín Diario')
  plt.title("Variación de la temperatura de Buenos Aires (Años 2025)", fontsize=14, fontweight="bold", pad=15)
  plt.xlabel("Fecha", fontsize=12)
  plt.ylabel("Temperatura (°C)", fontsize=12)
  plt.grid(True, linestyle='--', alpha=0.5)
  plt.legend(loc='upper right')

  nombre_grafico = "resultados/variacion_temperatura_2025.png"
  plt.savefig(nombre_grafico)
  plt.show()

if __name__ == "__main__":
  try:
    procesar_datos()
  except Exception as e:
    print(f"Ocurrió un error: {e}")