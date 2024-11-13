import pandas as pd

dados = {
    'nome': ['luiz', 'carlos', 'paulo', 'augusto', 'mario'],
    'idade': [32, 23, 54, 23, 40]  # Added age for 'mario'
}

df = pd.DataFrame(dados)

print(df)
