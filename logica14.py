import pandas as pd

# Dados iniciais da fila de alunos
dados_fila_escola = {
    'id_aluno': [1, 2, 3, 4, 5],
    'nome_aluno': ['Ana', 'Carlos', 'Maria', 'José', 'Paulo'],
    'hora_chegada': ['08:00', '08:10', '08:05', '08:20', '08:15'],
    'matricula_concluida': [True, False, True, False, True],  # Se a matrícula foi concluída
    'turma': ['1A', '1B', '1A', '1C', '1B']  # Turma do aluno
}

# Criar DataFrame representando a fila de alunos
fila_escola = pd.DataFrame(dados_fila_escola)

# Mostrar a fila inicial
print("Fila Inicial de Alunos para Entrar na Escola:")
print(fila_escola)

# Filtrar os alunos que já concluíram a matrícula
alunos_com_matricula = fila_escola[fila_escola['matricula_concluida'] == True]

# Filtrar os alunos que ainda não concluíram a matrícula
alunos_sem_matricula = fila_escola[fila_escola['matricula_concluida'] == False]

# Ordenar os alunos pela hora de chegada
fila_escola = fila_escola.sort_values(by='hora_chegada')

# Mostrar a fila após a organização por hora de chegada
print("\nFila Organizada por Hora de Chegada:")
print(fila_escola)

# Simular a entrada na escola: alunos com matrícula concluída entram primeiro
alunos_entrando = alunos_com_matricula.sort_values(by='hora_chegada')

# Mostrar os alunos que já podem entrar na escola
print("\nAlunos que Já Podem Entrar na Escola (Matrícula Concluída):")
print(alunos_entrando)

# Mostrar os alunos que ainda precisam concluir a matrícula
print("\nAlunos que ainda precisam concluir a matrícula:")
print(alunos_sem_matricula)
