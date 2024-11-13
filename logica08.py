import pandas as pd

# Dados fictícios sobre escolas e seu status (funcionando ou interditada)
dados_escolas = {
    'id_escola': [1, 2, 3, 4, 5],
    'nome': ['Escola A', 'Escola B', 'Escola C', 'Escola D', 'Escola E'],
    'status': ['Funcionando', 'Interditada', 'Funcionando', 'Interditada', 'Funcionando']
}

# Criação do DataFrame
df = pd.DataFrame(dados_escolas)

# Filtrar escolas que estão funcionando
escolas_funcionando = df[df['status'] == 'Funcionando']

# Filtrar escolas que estão interditadas
escolas_interditadas = df[df['status'] == 'Interditada']

# Exibir escolas funcionando
print("Escolas Funcionando:")
print(escolas_funcionando)

# Exibir escolas interditadas
print("\nEscolas Interditadas:")
print(escolas_interditadas)
