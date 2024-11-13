import pandas as pd

# Dados fictícios dos candidatos
dados_candidatos = {
    'candidato': ['Carlos', 'Ana', 'João', 'Lucas'],
    'tecnologia': ['Python', '.NET', 'Python', '.NET'],
    'experiencia_anos': [5, 4, 3, 6],  # Anos de experiência com a tecnologia
    'pontuacao_teste': [85, 90, 75, 80],  # Pontuação no teste técnico
    'habilidades_comunicacao': [80, 85, 90, 88],  # Avaliação de habilidades de comunicação
}

# Criar DataFrame para representar os dados dos candidatos
candidatos = pd.DataFrame(dados_candidatos)

# Calcular uma pontuação total fictícia baseada em experiência, pontuação do teste e habilidades de comunicação
candidatos['pontuacao_total'] = (candidatos['experiencia_anos'] * 10) + candidatos['pontuacao_teste'] + candidatos['habilidades_comunicacao']

# Ordenar os candidatos pela pontuação total, do maior para o menor
candidatos_sorted = candidatos.sort_values(by='pontuacao_total', ascending=False)

# Exibir os resultados
print("Ranking de Candidatos:")
print(candidatos_sorted[['candidato', 'tecnologia', 'pontuacao_total']])

# Determinar o vencedor (candidato com maior pontuação total)
vencedor = candidatos_sorted.iloc[0]
print("\nVencedor da Vaga:")
print(f"Candidato: {vencedor['candidato']}, Tecnologia: {vencedor['tecnologia']}, Pontuação Total: {vencedor['pontuacao_total']}")
