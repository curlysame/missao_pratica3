from operacoes import verificaralunos_reprovados

dados_alunos = {
    26: {'nome': 'Maria', 'notas': [9, 7, 5, 9]},
    101: {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    13: {'nome': 'João', 'notas': [6, 5, 5, 5]},
    37: {'nome': 'Agatha', 'notas': [8, 6, 7.5, 9]},
    72: {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
    5: {'nome':'Félix', 'notas': [10, 8, 8, 8]}

}

alunos_reprovados = verificaralunos_reprovados(dados_alunos)
if alunos_reprovados:
    print("Alunos Reprovados:")
    for aluno in alunos_reprovados:
        print(f"Aluno: {aluno['nome']} - Matrícula: {aluno['matricula']} - Média Final: {aluno['media']:.2f}")
    else:
        print("Nenhum aluno foi reprovado.")    