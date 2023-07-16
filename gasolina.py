import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('/content/gasolina/gasolina.csv')
grafico = sns.scatterplot(data=gasolina_df, x='dia', y='venda')
grafico.set_xlabel('Dia')
grafico.set_ylabel('Venda')
grafico.set_title('Vendas de Gasolina')
plt.savefig('/content/gasolina/gasolina.png')
plt.show()