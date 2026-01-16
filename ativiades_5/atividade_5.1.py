import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nomes = ["Alice", "Joao", "Ana", "Nicolas", "Jose", "Carlos", "Janaina", "Caio", "Cristiane"]

nomes_com_a=[]
nomes_com_c=[]
nomes_com_j=[]
nomes_com_n=[]

#verificar se o nome comecou com a letra A
for nome in nomes:
    if nome.startswith('A'):
        nomes_com_a.append(nome)
print(nomes_com_a)

print("--------------------------------------------------------------")

#verificar se o nome comecou com a letra C
for nome in nomes:
    if nome.startswith('C'):
        nomes_com_c.append(nome)
print(nomes_com_c)

print("--------------------------------------------------------------")

#verificar se o nome comecou com a letra J

for nome in nomes:
    if nome.startswith('J'):
        nomes_com_j.append(nome)
print(nomes_com_j)

print("--------------------------------------------------------------")

#verificar se o nome comecou com a letra N

for nome in nomes:
    if nome.startswith('N'):
        nomes_com_n.append(nome)
print(nomes_com_n)