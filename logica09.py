import pandas as pd

# Criar uma pilha com pandas (simulando uma pilha com uma lista)
pilha = pd.Series([1, 2, 3, 4, 5])

# Mostrar a pilha
print("Pilha Inicial:")
print(pilha)

# Empilhar (adicionar elemento no topo da pilha)
pilha = pd.concat([pilha, pd.Series([6])], ignore_index=True)

# Desempilhar (remover o elemento do topo)
topo = pilha.iloc[-1]  # Elemento no topo
pilha = pilha.drop(pilha.index[-1])  # Remover o topo

print("\nPilha após empilhar 6 e desempilhar o topo:")
print(pilha)
print("\nElemento desempilhado:", topo)

