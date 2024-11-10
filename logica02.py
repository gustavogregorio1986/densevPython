import pandas as pd

dados = {
         'nome':['ana','luiz','pedro','marcel', 'lenadro'],
         'idade':[12,89,43,23,22],
          'universidade':['UVA','estacio','unigranderio','gama filho','santa ursula']
          }

df = pd.DataFrame(dados)

print(df)