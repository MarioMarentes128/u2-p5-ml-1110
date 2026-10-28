import numpy as np
import pandas as pd
# Mario Yañez NC 1110
## datos
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("--- datos a partir de una matrix 4 x 3 ---")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])

print(df)
# datos a partit de un diccionario
print("--- datos a partir de un diccionario ---")
alumno_diccionario={
  "nombre":["Eliseo","Joel","Pedro","Nicole","Dilan","Jesse"],
  "califa":[60,90,100,80,70,50],
  "edad":[64,15,16,16,18,14]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Mario Yañez NC 1110")