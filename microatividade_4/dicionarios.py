meu_dicionario = {
    1:{"codigo":"1","linguagem": "Python"},
    2:{"codigo": "2","linguagem":"Java"},
    3:{"codigo": "3","linguagem": "PHP"}
}

codigo = list(meu_dicionario.keys())
linguagem = list(meu_dicionario.values())
tamanho = len(meu_dicionario)

print(meu_dicionario)
print(type(meu_dicionario))
print(codigo)
print(meu_dicionario.get("linguagem"))
print(tamanho)

dicionario_frutas = {
    1: {"nome":"limão","tipo": "ácida"},
    2: {"nome":"laranja","tipo": "ácida"},
    3: {"nome":"manga","tipo": "ácida"},
    4: {"nome":"maçã","tipo": "ácida"},
    5: {"nome":"banana","tipo": "ácida"},
    6: {"nome":"mamão","tipo": "ácida"}
}

meu_dicionario = dict(dicionario_frutas)

print(f"Nome: {dicionario_frutas[1]['nome']}, Tipo: {dicionario_frutas[1]['tipo']}")
print(f"Nome: {dicionario_frutas[2]['nome']}, Tipo: {dicionario_frutas[2]['tipo']}")

for chave, valores in dicionario_frutas.items():
    print(f"{chave} - {valores['nome']} : {valores['tipo']}")