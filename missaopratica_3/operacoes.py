def calcular_media(notas):
    if len(notas) != 4:
        raise ValueError("O aluno deve ter exatamnente 4 notas.")
    return sum(notas) / len(notas)

def verificaralunos_reprovados(dados_alunos):
    alunos_reprovados = []
    for matricula, dados in dados_alunos.items():
        media = calcular_media(dados['notas'])
        if media < 6:
            alunos_reprovados.append({
                'nome': dados['nome'],
                'matricula': matricula,
                'media' : media
            })
    return alunos_reprovados