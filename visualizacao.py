import pandas as pd
import seaborn as sns
from sys import argv

df = pd.read_csv('taxa-cdi.csv')

grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)

grafico.get_figure().savefig(f"{argv[1]}.png")
