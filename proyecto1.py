import numpy as np

import pandas as pd

datos = pd.read_csv('assets/real_estate.csv', sep=';')

# la casa mas cara  columna = "price" 11

id_precio_max = datos["price"].idxmax()

casa_valor_max = datos.iloc[id_precio_max]

print("La casa más cara tiene un valor de: ", casa_valor_max)
