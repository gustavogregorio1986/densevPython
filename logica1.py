import pandas as pd

dados = {'nome': ['luiz', 'marcos', 'lenadro', 'marcos', 'fernanda','maycon', 'laio', 'leandro']}

nomes_filtrados = [nome for nome in dados['nome'] if nome.startswith('f') and 'anda' not in nome and 'panda' not in nome]

print(nomes_filtrados)