import seaborn as sns
import pandas as pd

# Carrega o dataset iris
iris = sns.load_dataset("iris")

# Salva como CSV no seu computador
iris.to_csv("iris.csv", index=False)
