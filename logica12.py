import pandas as pd

# Dados iniciais da fila de passageiros esperando para entrar no ônibus
dados_fila_onibus = {
    'id_passageiro': [1, 2, 3, 4, 5],
    'nome_passageiro': ['Ana', 'Carlos', 'Maria', 'José', 'Paulo'],
    'hora_chegada': ['08:00', '08:02', '08:05', '08:07', '08:10'],
    'embarque': [False, False, False, False, False]  # Se o passageiro já embarcou
}

# Criar DataFrame representando a fila de passageiros
fila_onibus = pd.DataFrame(dados_fila_onibus)

# Mostrar a fila inicial
print("Fila Inicial para Entrar no Ônibus:")
print(fila_onibus)

# Simular o embarque dos passageiros, atendendo primeiro os mais próximos (por hora de chegada)
# Atualizamos a coluna "embarque" para indicar quem já embarcou
fila_onibus['embarque'] = fila_onibus['hora_chegada'].apply(lambda x: x <= '08:05')  # Passageiros até 08:05 já embarcaram

# Filtrar passageiros que embarcaram
passageiros_embarcados = fila_onibus[fila_onibus['embarque'] == True]

# Filtrar passageiros que ainda estão na fila
passageiros_na_fila = fila_onibus[fila_onibus['embarque'] == False]

# Mostrar os passageiros embarcados
print("\nPassageiros que já embarcaram:")
print(passageiros_embarcados)

# Mostrar os passageiros que ainda estão esperando na fila
print("\nPassageiros que ainda estão na fila:")
print(passageiros_na_fila)

# Simular a partida do ônibus (remover os passageiros embarcados da fila)
fila_onibus = fila_onibus[fila_onibus['embarque'] == False]

print("\nFila após embarque:")
print(fila_onibus)
