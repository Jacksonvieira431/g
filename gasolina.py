import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('/content/gasolina/gasolina.csv')
grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
fig = grafico.get_figure()
fig.savefig('/content/gasolina/gasolina.png')
