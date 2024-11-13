import pandas as pd

# Dados fictícios sobre padres e suas métricas de popularidade
dados_padres = {
    'padre': ['Padre Fábio de Melo', 'Padre Marcelo Rossi', 'Padre Antônio Maria', 'Padre Reginaldo Manzotti', 'Padre José Augusto'],
    'seguidores_redes_sociais': [10000000, 15000000, 5000000, 12000000, 8000000],  # Número de seguidores nas redes sociais
    'entrevistas_tv': [30, 50, 15, 40, 20],  # Número de entrevistas na TV
    'livros_publicados': [5, 10, 3, 7, 2],  # Número de livros publicados
    'programas_tv': [10, 15, 5, 12, 8],  # Número de programas na TV
}

# Criar DataFrame
df_padres = pd.DataFrame(dados_padres)

# Calcular a "fama" de cada padre somando os critérios
df_padres['fama'] = (df_padres['seguidores_redes_sociais'] * 0.4) + (df_padres['entrevistas_tv'] * 0.3) + (df_padres['livros_publicados'] * 0.2) + (df_padres['programas_tv'] * 0.1)

# Ordenar o DataFrame pela "fama"
df_padres_sorted = df_padres.sort_values(by='fama', ascending=False)

# Mostrar o padre mais famoso
padre_mais_famoso = df_padres_sorted.iloc[0]

print("Padre mais famoso na mídia:")
print(padre_mais_famoso)
