import pandas as pd

# Dados iniciais da fila de banco
dados_fila = {
    'id_cliente': [1, 2, 3, 4],
    'nome_cliente': ['Ana', 'Carlos', 'Maria', 'José'],
    'conta': ['12345', '67890', '11223', '44556'],
    'tempo_espera': [10, 15, 5, 20],  # Tempo de espera em minutos
    'prioridade': ['normal', 'normal', 'alta', 'normal']  # Prioridade do atendimento
}

# Criar o DataFrame representando a fila
fila_banco = pd.DataFrame(dados_fila)

# Mostrar a fila inicial
print("Fila Inicial do Banco:")
print(fila_banco)

# Adicionar um novo cliente na fila (no final)
novo_cliente = pd.DataFrame({
    'id_cliente': [5],
    'nome_cliente': ['Marcos'],
    'conta': ['98765'],
    'tempo_espera': [10],
    'prioridade': ['alta']
})

fila_banco = pd.concat([fila_banco, novo_cliente], ignore_index=True)

# Ordenar a fila pela prioridade e tempo de espera
fila_banco = fila_banco.sort_values(by=['prioridade', 'tempo_espera'], ascending=[False, True])

# Mostrar a fila após a adição de um novo cliente e ordenação
print("\nFila Após Adicionar um Novo Cliente e Ordenar:")
print(fila_banco)

# Atender o próximo cliente (remover o primeiro da fila)
cliente_atendido = fila_banco.iloc[0]  # Cliente que está sendo atendido
fila_banco = fila_banco.drop(fila_banco.index[0])  # Remover da fila

print("\nCliente Atendido:", cliente_atendido['nome_cliente'])
print("\nFila Após Atendimento:")
print(fila_banco)
