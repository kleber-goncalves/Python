import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numero = 1

while numero < 20:
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    else:
        print(f"O numero {numero} é impar")
    numero += 1