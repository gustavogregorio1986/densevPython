import pandas as pd

# Dados iniciais da competição de natação
dados_competicao = {
    'atleta': ['Ana', 'Carlos', 'Maria', 'José', 'Paulo'],
    'categoria': ['Adulto', 'Júnior', 'Adulto', 'Sênior', 'Júnior'],
    'tempo_segundos': [58.5, 62.3, 59.1, 65.2, 61.4],  # Tempo em segundos
}

# Criar DataFrame para representar a competição
competicao_natacao = pd.DataFrame(dados_competicao)

# Classificar os atletas pelo tempo (menor tempo é o melhor)
competicao_natacao['classificacao'] = competicao_natacao['tempo_segundos'].rank()

# Ordenar os resultados pela classificação (do 1º para o último)
competicao_natacao = competicao_natacao.sort_values(by='classificacao')

# Exibir os resultados da competição
print("Resultados da Competição de Natação:")
print(competicao_natacao)

# Obter o vencedor
vencedor = competicao_natacao.iloc[0]
print("\nVencedor da Competição:")
print(f"Atleta: {vencedor['atleta']}, Categoria: {vencedor['categoria']}, Tempo: {vencedor['tempo_segundos']} segundos")
