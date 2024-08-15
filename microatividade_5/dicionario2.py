pessoa = {
    1:{'nome':'Maria', 'idade': '26','nacionalidade':'brasileira'}

}

#print(pessoa)
#print(type(pessoa))

pessoa_2 = {
    2: {'nome': 'Luis', 'idade':'30','nacionalidade' : 'italiana'},
    3: {'nome': 'Amanda', 'idade': '29', 'nacionalidade' : 'italiana'}


}

pessoa.update(pessoa_2)
#print(pessoa)

#pessoa_copia = pessoa.copy()
#print(pessoa)
#print(pessoa_copia)
#valor_removido = pessoa.pop(2)
#print(pessoa)
#valor_removido_2 = pessoa.popitem()
#print(valor_removido_2)

pessoa.clear()
pessoa_2.clear()

numeros = [1, 2, 3]

novo_dicionario = dict.fromkeys(numeros)
print(novo_dicionario.items())
print(novo_dicionario.keys())
print(novo_dicionario.values())
