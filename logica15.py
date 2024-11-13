import pandas as pd

# Dados iniciais de presença dos alunos
dados_presenca = {
    'id_aluno': [1, 2, 3, 4, 5],
    'nome_aluno': ['Ana', 'Carlos', 'Maria', 'José', 'Paulo'],
    'turma': ['1A', '1B', '1A', '1C', '1B'],
    'presenca': ['Presente', 'Ausente', 'Presente', 'Presente', 'Ausente'],  # Presença ou ausência
    'hora_chegada': ['08:00', '09:00', '08:15', '08:30', '09:10']  # Hora de chegada
}

# Criar DataFrame para representar a presença dos alunos
presenca_escola = pd.DataFrame(dados_presenca)

# Mostrar o DataFrame de presença
print("Registro de Presença dos Alunos:")
print(presenca_escola)

# Filtrar alunos presentes
alunos_presentes = presenca_escola[presenca_escola['presenca'] == 'Presente']

# Filtrar alunos ausentes
alunos_ausentes = presenca_escola[presenca_escola['presenca'] == 'Ausente']

# Mostrar os alunos presentes
print("\nAlunos Presentes na Escola:")
print(alunos_presentes)

# Mostrar os alunos ausentes
print("\nAlunos Ausentes da Escola:")
print(alunos_ausentes)

# Contagem de presenças e ausências
contagem_presenca = presenca_escola['presenca'].value_counts()
print("\nContagem de Presença e Ausência:")
print(contagem_presenca)
