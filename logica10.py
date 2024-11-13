import pandas as pd

# Dados simulando recursos na AWS
dados_aws = {
    'id_recurso': [101, 102, 103, 104],
    'nome_recurso': ['Instância EC2', 'Bucket S3', 'Instância EC2', 'Bucket S3'],
    'status': ['Ativo', 'Desativado', 'Ativo', 'Ativo'],
    'regiao': ['us-east-1', 'us-west-2', 'us-east-1', 'us-west-1'],
    'data_criacao': ['2024-01-10', '2024-02-15', '2024-03-20', '2024-04-10']
}

# Criar DataFrame com pandas
df_aws = pd.DataFrame(dados_aws)

# Mostrar a ficha
print("Ficha de Recursos AWS:")
print(df_aws)

# Filtrando recursos ativos
recursos_ativos = df_aws[df_aws['status'] == 'Ativo']
print("\nRecursos Ativos:")
print(recursos_ativos)

# Filtrando recursos por região
regiao_us_east = df_aws[df_aws['regiao'] == 'us-east-1']
print("\nRecursos na Região us-east-1:")
print(regiao_us_east)
