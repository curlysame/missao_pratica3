lista_mesclada = [1,2,3,"Ola, Python",True,12.6]
print(lista_mesclada)
lista_mesclada.append("Lista aninhada")
print(lista_mesclada)
novo_elemento = 5
lista_mesclada.insert(4,novo_elemento)
print(lista_mesclada)
lista_mesclada.remove(1)
print(lista_mesclada)

nova_lista_mesclada = lista_mesclada[:4]
print(nova_lista_mesclada)