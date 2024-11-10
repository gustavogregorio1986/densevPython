import pandas as pd

data = {'nome': ['Ana', 'Carlos', 'Beatriz', 'Daniel'],
        'idade': [23, 17, 45, 30],
        'cidade': ['SP', 'RJ', 'SP', 'MG']}
df = pd.DataFrame(data)

# Filtrar pessoas maiores de idade (idade > 18)
maiores_idade = df[df['idade'] > 18]
print(maiores_idade)