import matplotlib.pyplot as plt
import numpy as np

# 1. Preparar os dados para os dois gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # Dados para o primeiro gráfico (seno)
y2 = np.cos(x)  # Dados para o segundo gráfico (cosseno)

# 2. Criar a figura e um conjunto de subplots (1 linha, 2 colunas)
# 'fig' é a janela/figura toda, 'axs' é um array dos eixos individuais
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4)) # figsize define o tamanho da figura

# 3. Plotar no primeiro eixo (axs[0])
axs[0].plot(x, y1, 'tab:blue')
axs[0].set_title('Gráfico de Seno')
axs[0].set_xlabel('Eixo X')
axs[0].set_ylabel('Eixo Y1')
axs[0].grid(True)

# 4. Plotar no segundo eixo (axs[1])
axs[1].plot(x, y2, 'tab:red')
axs[1].set_title('Gráfico de Cosseno')
axs[1].set_xlabel('Eixo X')
axs[1].set_ylabel('Eixo Y2')
axs[1].grid(True)

# 5. Ajustar o layout para evitar sobreposição de títulos/rótulos
plt.tight_layout()

# 6. Exibir a janela com os gráficos
plt.show()
