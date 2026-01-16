salarios = [2000, 5000, 1500, 2100, 5000, 1500, 2000]

contagem = {}

for salario in salarios:
    if salario in contagem:
        contagem[salario] = contagem[salario] + 1
    else:
        contagem[salario] = 1

print(contagem)