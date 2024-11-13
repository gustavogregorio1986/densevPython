import pandas as pd

# Dados iniciais da eleição
dados_eleicao = {
    'candidato': ['João', 'Maria', 'Pedro', 'Ana'],
    'partido': ['PSL', 'PT', 'PSDB', 'MDB'],
    'votos': [4500, 3200, 2800, 1800],  # Número de votos recebidos
}

# Criar DataFrame para representar a eleição
eleicao = pd.DataFrame(dados_eleicao)

# Calcular o total de votos
total_votos = eleicao['votos'].sum()

# Calcular a porcentagem de votos de cada candidato
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
