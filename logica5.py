import pandas as pd

# Dados fictícios de escolas com o status de funcionamento
dados_escolas = {
    'escola': ['Escola A', 'Escola B', 'Escola C', 'Escola D', 'Escola E'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre'],
    'status_funcionamento': ['Em funcionamento', 'Fechada', 'Em funcionamento', 'Em funcionamento', 'Fechada']
}

# Criação do DataFrame
df = pd.DataFrame(dados_escolas)

# Filtrar apenas as escolas que estão em funcionamento
escolas_funcionando = df[df['status_funcionamento'] == 'Em funcionamento']

# Exibir as escolas em funcionamento
print(escolas_funcionando)
