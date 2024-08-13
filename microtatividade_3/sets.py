set_inicial = {11, 12, 13, 14}
#print(set_inicial)
set_inicial.add(15)
#print(set_inicial)
set_2 = {1, 2, 3, 4, 5}

set_inicial.update(set_2)
#print(set_inicial)

set_inicial.discard(3)
#print(set_inicial)

novo_set = {20, 21, 23, 1, 2}
#print(novo_set)

difference = set_inicial.difference(set_2)

difference_simetrica = set_inicial.symmetric_difference(set_2)

print(difference)
print(difference_simetrica)


