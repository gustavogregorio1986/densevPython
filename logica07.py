import pandas as pd
from datetime import datetime

# Dados fictícios sobre voos com hora de aterrissagem
dados_voos = {
    'voo_id': [101, 102, 103, 104, 105],
    'companhia': ['LATAM', 'Gol', 'Azul', 'TAM', 'Gol'],
    'hora_aterrissagem': ['2024-11-12 14:30', '2024-11-12 15:00', '2024-11-12 16:10', '2024-11-12 17:20', '2024-11-12 18:40'],
    'status': ['Aterrissando', 'Aterrissado', 'Aterrissando', 'Aterrissado', 'Aterrissando']
}

# Criação do DataFrame
df = pd.DataFrame(dados_voos)

# Convertendo a coluna 'hora_aterrissagem' para datetime
df['hora_aterrissagem'] = pd.to_datetime(df['hora_aterrissagem'])

# Definir a data e hora atual
data_atual = datetime.now()

# Filtrar aviões que estão aterrissando ou que aterrissaram recentemente (por exemplo, nas últimas 2 horas)
tempo_maximo = pd.Timedelta(hours=2)
voos_recentemente_aterrissados = df[df['status'] == 'Aterrissando']
voos_recentemente_aterrissados = voos_recentemente_aterrissados[voos_recentemente_aterrissados['hora_aterrissagem'] <= data_atual]

# Exibir os voos que estão aterrissando ou aterrissaram recentemente
print(voos_recentemente_aterrissados)
