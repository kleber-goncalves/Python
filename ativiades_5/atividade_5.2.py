import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

idades = [17, 18, 25, 43, 15, 29, 36, 50]

menores_18 = []
maiores_18 = []

for idade in idades:
    if idade <= 18:
        menores_18.append(idade)
    else:
        maiores_18.append(idade)

print("Idades menores ou igual a 18 anos: ",menores_18)
print("Iddades Maiores que 18 anos: ",maiores_18)