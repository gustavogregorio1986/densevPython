import pandas as pd

dados_saude = {
    'nome': ['Ana', 'Carlos', 'Bianca', 'Rafael', 'Mariana'],
    'peso': [70, 85, 68, 90, 60],  # peso em kg
    'diabetes': ['Sim', 'Não', 'Sim', 'Não', 'Sim']
}

df = pd.DataFrame(dados_saude)

pessoas_com_diabetes = df[df['diabetes'] == 'Sim']

print(pessoas_com_diabetes[['nome', 'peso']])
