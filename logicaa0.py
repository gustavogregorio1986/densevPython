import pandas as pd

dados = {'numero': [43,13,54, 32,12,59,34]}

df = pd.DataFrame(dados)

maior_numero = df[df['numero'] > 50]

print(maior_numero)