import pandas as pd
from datetime import datetime

# Dados fictícios sobre balsas com data de fabricação
dados_balsas = {
    'balsa_id': [101, 102, 103, 104, 105],
    'nome': ['Balsa A', 'Balsa B', 'Balsa C', 'Balsa D', 'Balsa E'],
    'data_fabricacao': ['2024-10-10', '2024-11-01', '2024-08-15', '2024-09-20', '2024-11-05']
}

# Criação do DataFrame
df = pd.DataFrame(dados_balsas)

# Convertendo a coluna de datas para o tipo datetime
df['data_fabricacao'] = pd.to_datetime(df['data_fabricacao'])

# Definir a data atual para comparação (supondo que a data atual seja hoje)
data_atual = datetime.now()

# Filtrar as balsas que saíram da fábrica nos últimos 30 dias
dias_recentes = 30
balsas_recentes = df[df['data_fabricacao'] >= (data_atual - pd.Timedelta(days=dias_recentes))]

# Exibir as balsas recentes
print(balsas_recentes)
