import pandas as pd

# Dados com nomes e cidades
dados = {
    'nome': ['luiz', 'marcos', 'lenadro', 'fernanda', 'maycon'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
}

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)
