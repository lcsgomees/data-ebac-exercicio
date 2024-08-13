
# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")
df.head(10)

# estilo do gráfico
sns.set(style='whitegrid')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')

# Configurar os rótulos e o título
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar o gráfico em um arquivo PNG
plt.savefig('gasolina.png')
