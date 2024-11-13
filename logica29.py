import pandas as pd

# Dados fictícios de igrejas e suas datas de fundação
dados_igrejas = {
    'igreja': ['Igreja de São Gonçalo do Amarante', 'Igreja de Nossa Senhora do Rosário', 'Igreja de São Francisco', 'Igreja de São João Batista'],
    'cidade': ['Natal', 'Rio de Janeiro', 'Salvador', 'Recife'],
    'data_fundacao': ['1598-01-01', '1567-01-01', '1589-01-01', '1570-01-01'],  # Data de fundação
}

# Criar o DataFrame
df_igrejas = pd.DataFrame(dados_igrejas)

# Verificando o DataFrame
print("DataFrame antes de qualquer processamento:")
print(df_igrejas)

# Converter a coluna de data_fundacao para o tipo datetime
df_igrejas['data_fundacao'] = pd.to_datetime(df_igrejas['data_fundacao'], format='%Y-%m-%d')

# Verificando se a conversão de data foi bem-sucedida
print("\nDataFrame após conversão de 'data_fundacao' para datetime:")
print(df_igrejas)

# Ordenar pelo ano de fundação (mais antigo primeiro)
df_igrejas_sorted = df_igrejas.sort_values(by='data_fundacao')

# Verificando o DataFrame após a ordenação
print("\nDataFrame ordenado pela data de fundação:")
print(df_igrejas_sorted)

# Mostrar a igreja mais antiga
igreja_mais_antiga = df_igrejas_sorted.iloc[0]

print("\nA igreja mais antiga do Brasil:")
print(igreja_mais_antiga)
