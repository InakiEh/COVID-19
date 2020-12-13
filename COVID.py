import pandas as pd
import os
directory = r'C:\Users\Iñaki\Desktop\Datos-COVID19-master\output\producto4'
pd.set_option("display.max_rows", None, "display.max_columns", None)

numeroarchivos = 0
numerocasos = []

for filename in os.listdir(directory):
    numeroarchivos += 1
    df = pd.read_csv(directory+filename)
    #print(filename)

contador = 0

Totalfilas = df.shape[0]
while contador < Totalfilas:
    numerocasos.append(df.iloc[contador]["Casos nuevos totales"])
    contador +=1

data =  {'Numero Casos': numerocasos}

CasosRM = pd.DataFrame(data)
print(CasosRM)