import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nome = "Kleber"
idade = 20
altura = 1.73
estudante = True
print("Hello World")
print("Bem vindo ao curso de Python",nome)
print("Olá",nome,"você tem",idade,"anos e",altura,"de altura.")
print("Você é estudante?",estudante)

print("...........................................................")

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))

print("...........................................................")

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

print("...........................................................")

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3
print("A média das três notas é:", media)

print("...........................................................")

nome_aluno = input("Digite o nome do aluno: ")  
print("O nome do novo aluno é:", nome_aluno)

print("...........................................................")

idade_aluno = input("Digite a idade do novo aluno: ")
idade_aluno = int(idade_aluno)
print("A idade do novo aluno em 5 anos é:", idade_aluno + 5)

print("...........................................................")

print("Raiz quadrada de 16:", math.sqrt(16))
print ("Valor de pi: ", math.pi)

print("...........................................................")

numeros = np.array([2,4,6,8,10])
print("Arry de numeros: ",numeros)
print("Media: ",np.mean(numeros))
print("Maior valor: ",np.max(numeros))

print("...........................................................")

dados = {"nome": ["Kleber", "Beatriz"], "idade": [20, 17], "nota": [7.5, 8.0]}
df = pd.DataFrame(dados)
sns.barplot(x="nome", y="nota", data=df)
plt.show()

print("...........................................................")


print("Fim do programa")