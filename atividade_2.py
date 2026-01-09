import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("...........................................................")
#variaveis + arry
notas = ([7,5,10,8.0,9.5,9])

#funçoes
meida_notas = np.mean(notas)
maior_nota = np.max(notas)

# saidas
print("Arry de numeros: ",notas)
print("Media: ",meida_notas)
print("Maior nota: ",maior_nota)

print("...........................................................")

# Area dos Grafico

#dados mocados para o grafico
dados = {"nome": ["Kleber", "Ana", "Lazaro", "Nicolas", "Guilherme", "Lavinia"], "nota": [7,5,10,8.0,9.5,9]}

#criando o grafico
df = pd.DataFrame(dados)
sns.barplot(x="nome", y="nota", data=df)

#mostrando o grafico
plt.show()

print("...........")


# 2 grafico 
#dados mocados para o grafico
maior_idade = {"nome": ["Kleber", "Ana", "Lazaro", "Nicolas", "Guilherme", "Lavinia"], "salario": [1000, 2000, 3000, 4000, 5000, 6000], "idade": [20, 17, 18, 19, 21, 22]}

#criando o grafico
df = pd.DataFrame(maior_idade)
sns.barplot(x="nome", y="idade", data=df)

sns.barplot(x="nome", y="salario", data=df)

#mostrando o grafico
plt.show()

print("...........................................................")

#Comparações
maior_idade = df["idade"][2] >= 18
bom_salario = df["salario"][2] >= 3000

#Logica Combinada
adulto_independente = maior_idade and bom_salario
jovem_dependente = (not maior_idade) and (not bom_salario)

#classificações 
if adulto_independente :
    print("Adulto bem de vida")
elif jovem_dependente :
    print ("Jovem sem dinheiro")
else :
    print ("Nunhum das opcoes")



print("Fim do programa")