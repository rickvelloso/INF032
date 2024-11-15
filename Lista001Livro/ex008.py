import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# (a) Importar os dados do Excel e atribuir a cada coluna uma variável
df = pd.read_excel('C:/Users/r1k/Documents/INF032/INF032/Lista001Livro/dados_bovespa.xlsx', sheet_name='Plan1')
vale = df['VALE3']  
gerdau = df['GGBR4']  

# (b) Transformar as variáveis em vetores usando numpy
vale = np.array(vale)
gerdau = np.array(gerdau)

# (c) Fazer os dois gráficos dos preços de VALE e GERDAU usando subplot
plt.figure(figsize=(10, 6))

# Subplot para VALE
plt.subplot(2, 1, 1)
plt.plot(vale, label='VALE3')
plt.title('Preços de Fechamento - VALE3')
plt.xlabel('Dias')
plt.ylabel('Preço')
plt.legend()

# Subplot para GERDAU
plt.subplot(2, 1, 2)
plt.plot(gerdau, label='GGBR4')
plt.title('Preços de Fechamento - GGBR4')
plt.xlabel('Dias')
plt.ylabel('Preço')
plt.legend()

plt.tight_layout()
plt.show()

# (d) Calcular os retornos e plotar os quatro gráficos (preço e retorno)
# Cálculo dos retornos (considerando retorno percentual diário)
retorno_vale = (vale[1:] - vale[:-1]) / vale[:-1]
retorno_gerdau = (gerdau[1:] - gerdau[:-1]) / gerdau[:-1]

# Plotar os quatro gráficos em uma matriz 2x2
plt.figure(figsize=(12, 8))

# Gráfico de preço da VALE
plt.subplot(2, 2, 1)
plt.plot(vale, label='VALE3 Preço')
plt.title('Preço - VALE3')
plt.xlabel('Dias')
plt.ylabel('Preço')
plt.legend()

# Gráfico de retorno da VALE
plt.subplot(2, 2, 2)
plt.plot(retorno_vale, label='VALE3 Retorno')
plt.title('Retorno - VALE3')
plt.xlabel('Dias')
plt.ylabel('Retorno')
plt.legend()

# Gráfico de preço da GGBR4
plt.subplot(2, 2, 3)
plt.plot(gerdau, label='GGBR4 Preço')
plt.title('Preço - GGBR4')
plt.xlabel('Dias')
plt.ylabel('Preço')
plt.legend()

# Gráfico de retorno da GGBR4
plt.subplot(2, 2, 4)
plt.plot(retorno_gerdau, label='GGBR4 Retorno')
plt.title('Retorno - GGBR4')
plt.xlabel('Dias')
plt.ylabel('Retorno')
plt.legend()

plt.tight_layout()
plt.show()
