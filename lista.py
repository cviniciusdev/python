lista = [123, True, 'Carlos Vinicius', 1.2, []]

del lista[2] # deleta um item da lista

lista.append('Luiz') # adiciona um item à lista

nome = lista.pop() # obtem somente o último ítem da lista

lista.clear() # limpa os elementos da lista

lista.insert(0, 5) # adiciona 5 na posição 0 da lista

print(len(lista))
print(nome)

lista = [123, True, 'Carlos Vinicius', 1.2, []]

lista = enumerate(lista)

for nomes in lista:
    print(nomes)

lista_desempacotamento = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

p, b, *_, ap, u = lista_desempacotamento

print(u)





