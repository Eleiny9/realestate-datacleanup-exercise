import numpy as np

import pandas as pd

datos = pd.read_csv('assets/real_estate.csv', sep=';')

# Ejercicio 1
# la casa mas cara  columna = "price" 

id_precio_max = datos["price"].idxmax()

casa_valor_max = datos.iloc[id_precio_max]

print("Ejercicio 1")
print("La casa más cara tiene un valor de: ", casa_valor_max["price"])
print(" y esta ubicada en: ", casa_valor_max["address"])

# Ejercicio 2
# la casa más barata 

id_precio_min = datos["price"].idxmin()

casa_valor_min = datos.iloc[id_precio_min]
print("Ejercicio 2")
print("la casa más barata tiene un precio de: ", casa_valor_min["price"])
print("y esta ubicada en: ", casa_valor_min["address"])

# Ejercicio 3 la casa mas grande y pequeña 
#  la casa más grande 


id_grande = datos["surface"].idxmax()

casa_grande = datos.iloc[id_grande]

print("Ejercicio 3")
print("La casa más grade tiene una superficie de :", casa_grande["surface"])
print("y esta ubicada en: ", casa_grande["address"])

# la casa más pequeña

id_peque = datos["surface"].idxmin()

casa_peque = datos.iloc[id_peque]

print("La casa más pequeña tiene una superficie de :", casa_peque["surface"])
print("y esta ubicada en: ", casa_peque["address"])





