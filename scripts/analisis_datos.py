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
  print(resumen_mensual)


if __name__ == "__main__":
  print("Se ejecuta el Script analisis_datos.py")
  procesar_datos()