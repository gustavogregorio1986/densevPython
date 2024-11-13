import pandas as pd

# Dados fictícios sobre a popularidade das linguagens
dados_linguagens = {
    'linguagem': ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP', 'Ruby', 'Swift', 'COBOL', 'Perl'],
    'popularidade': [28.0, 17.0, 13.0, 7.0, 6.5, 6.0, 3.0, 2.5, 0.5, 0.3],  # Porcentagem de popularidade
}

# Criar DataFrame
df_linguagens = pd.DataFrame(dados_linguagens)

# Ordenar as linguagens pela popularidade em ordem crescente (menor para maior)
df_linguagens_sorted = df_linguagens.sort_values(by='popularidade')

# Exibir a linguagem menos popular
print(df_linguagens_sorted)
