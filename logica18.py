import pandas as pd

# Dados da eleição
dados_eleicao = {
    'candidato': ['Bolsonaro', 'Lula', 'Pablo Marçal'],
    'partido': ['PL', 'PT', 'PLR'],  # Supondo partidos fictícios para exemplo
    'votos': [50000000, 45000000, 25000000],  # Número de votos simulados para cada candidato
}

# Criar DataFrame para representar a eleição
eleicao = pd.DataFrame(dados_eleicao)

# Calcular o total de votos
total_votos = eleicao['votos'].sum()

# Calcular a porcentagem de votos para cada candidato
eleicao['porcentagem_votos'] = (eleicao['votos'] / total_votos) * 100

# Ordenar os candidatos por número de votos, do maior para o menor
eleicao_sorted = eleicao.sort_values(by='votos', ascending=False)

# Exibir o DataFrame com os resultados
print("Resultados da Eleição:")
print(eleicao_sorted)

# Obter o vencedor
vencedor = eleicao_sorted.iloc[0]
print("\nVencedor da Eleição:")
print(f"Candidato: {vencedor['candidato']}, Partido: {vencedor['partido']}, Votos: {vencedor['votos']} ({vencedor['porcentagem_votos']:.2f}%)")
