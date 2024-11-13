import pandas as pd

# Dados fictícios sobre aviões, número de falhas e se são considerados inseguros
dados_avioes = {
    'aviao': ['Avião 1', 'Avião 2', 'Avião 3', 'Avião 4', 'Avião 5'],
    'numero_de_acidentes': [5, 1, 10, 2, 0],  # Número de acidentes/incidentes
    'falha_critica': [True, False, True, False, False],  # Se houve falha crítica
    'seguranca': ['Inseguro', 'Seguro', 'Inseguro', 'Seguro', 'Seguro']  # Estado de segurança
}

# Criar o DataFrame
df_avioes = pd.DataFrame(dados_avioes)

# Filtrar aviões com falhas críticas ou mais de 3 acidentes
avioes_inseguros = df_avioes[(df_avioes['falha_critica'] == True) | (df_avioes['numero_de_acidentes'] > 3)]

# Exibir os aviões inseguros
print("Aviões inseguros (com falhas críticas ou muitos acidentes):")
print(avioes_inseguros)
