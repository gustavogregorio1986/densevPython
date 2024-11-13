import pandas as pd

dados_meteorologia = {
    'data': ['2024-11-13'],
    'cidade': ['São Paulo'],
    'temperatura_min': [18],    # em graus Celsius
    'temperatura_max': [26],    # em graus Celsius
    'umidade': [78],            # em porcentagem
    'condicao': ['Parcialmente nublado']
}

df = pd.DataFrame(dados_meteorologia)

print(df)
