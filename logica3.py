import pandas as pd

dados = {'nome':['marcel','marcelo','maria','michelle'],
         'onibus':['penha','cometa','itapemerim','garcia'],
         'destino':['sao paulo','aracaju','pinheiros','salvador']}

df = pd.DataFrame(dados)

print(df)