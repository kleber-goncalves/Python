import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

valores = ["A", "B", "C", "C", "A", "C", "B", "B", "A"]

contage_categorias = {}

for valor in valores:
    if valor in contage_categorias:
        contage_categorias[valor] += 1
    else:
        contage_categorias[valor] = 1

print(contage_categorias)