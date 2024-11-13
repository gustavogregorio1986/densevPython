import pandas as pd
from datetime import datetime

# Dados fictícios sobre voos com hora de decolagem e status
dados_voos = {
    'voo_id': [101, 102, 103, 104, 105],
    'companhia': ['LATAM', 'Gol', 'Azul', 'TAM', 'Gol'],
    'hora_decolagem': ['2024-11-12 10:30', '2024-11-12 11:00', '2024-11-12 12:15', '2024-11-12 14:00', '2024-11-12 15:00'],
    'status': ['Voando', 'Voando', 'Aterrissado', 'Voando', 'Aterrissado']
}

# Criação do DataFrame
df = pd.DataFrame(dados_voos)

# Convertendo a coluna 'hora_decolagem' para datetime
df['hora_decolagem'] = pd.to_datetime(df['hora_decolagem'])

# Definir a data e hora atual
data_atual = datetime.now()

# Filtrar aviões que estão voando no momento
voos_voando = df[df['status'] == 'Voando']

# Exibir voos em voo
print(voos_voando)
