import numpy as np

import pandas as pd

datos = pd.read_csv('assets/real_estate.csv', sep=';')

# la casa mas cara  columna = "price" 

id_precio_max = datos["price"].idxmax()

casa_valor_max = datos.iloc[id_precio_max]

print("La casa más cara tiene un valor de: ", casa_valor_max["price"])
print(" y esta ubicada en: ", casa_valor_max["address"])

# la casa más barata 

id_precio_min = datos["price"].idxmin()

casa_valor_min = datos.iloc[id_precio_min]

print("la casa más barata tiene un precio de: ", casa_valor_min["price"])
print("la casa más barata tiene un precio de: ", casa_valor_min["address"])
