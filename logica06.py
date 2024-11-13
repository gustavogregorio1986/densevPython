import pandas as pd

dados_acoes = {
    'acao': ['Limpeza de praia', 'Aula de Yoga', 'Feira de Artesanato', 'Oficina de Reciclagem', 'Doação de Alimentos'],
    'cidade': ['Rio de Janeiro', 'São Paulo', 'Rio de Janeiro', 'Curitiba', 'Rio de Janeiro'],
    'status': ['Em andamento', 'Concluído', 'Em andamento', 'Planejado', 'Em andamento']
}

df = pd.DataFrame(dados_acoes)

acoes_rj_ativas = df[(df['cidade'] == 'Rio de Janeiro') & (df['status'] == 'Em andamento')]

print(acoes_rj_ativas)
