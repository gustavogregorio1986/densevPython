import pandas as pd

dados_saude = {
    'nome': ['Ana', 'Carlos', 'Bianca', 'Rafael', 'Mariana'],
    'peso': [95, 120, 88, 110, 100],  # peso em kg
    'altura': [1.60, 1.75, 1.65, 1.80, 1.70]  # altura em metros
}

df = pd.DataFrame(dados_saude)


df['IMC'] = df['peso'] / (df['altura'] ** 2)

df['massa_gordura'] = df['peso'] * 0.25 

obesidade_alta_gordura = df[(df['IMC'] >= 30) & (df['massa_gordura'] > 20)]

print(obesidade_alta_gordura[['nome', 'peso', 'altura', 'IMC', 'massa_gordura']])
