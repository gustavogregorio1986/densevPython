import pandas as pd

# Dados fictícios sobre a popularidade das linguagens
dados_linguagens = {
    'linguagem': ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP', 'Ruby', 'Swift'],
    'popularidade': [28.0, 17.0, 13.0, 7.0, 6.5, 6.0, 3.0, 2.5],  # Porcentagem de popularidade aproximada
}

# Criar DataFrame
df_linguagens = pd.DataFrame(dados_linguagens)

# Ordenar as linguagens pela popularidade em ordem decrescente
df_linguagens_sorted = df_linguagens.sort_values(by='popularidade', ascending=False)

# Exibir as linguagens mais populares
print(df_linguagens_sorted)
