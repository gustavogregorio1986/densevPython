import pandas as pd

# Dados fictícios sobre escolas no RJ e suas respectivas notas médias
dados_escolas = {
    'escola': ['Escola A', 'Escola B', 'Escola C', 'Escola D', 'Escola E'],
    'nota_media': [5.2, 6.1, 4.8, 7.3, 6.0]  # Notas médias dos alunos (por exemplo, de 0 a 10)
}

# Criar DataFrame
df_escolas = pd.DataFrame(dados_escolas)

# Ordenar o DataFrame pela nota média, de forma crescente (para identificar a escola mais fraca)
df_escolas_sorted = df_escolas.sort_values(by='nota_media')

# Exibir a escola mais fraca (com a menor nota média)
print("Escola mais fraca do RJ:")
print(df_escolas_sorted.iloc[0])
