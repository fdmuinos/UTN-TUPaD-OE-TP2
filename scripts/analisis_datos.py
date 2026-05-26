import pandas as pd
import os

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

if __name__ == "__main__":
  print("Se ejecuta el Script analisis_datos.py")