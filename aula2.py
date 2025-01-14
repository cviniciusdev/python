from itertools import combinations, permutations, product, groupby


def print_iter(iterator):
    print(*list(iterator), sep='\n')

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm'],
]

def ordena(a):
    return a['nota']

alunos_ordenados = sorted(alunos, key=ordena)
grupos = groupby(alunos_ordenados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

#print_iter(product(*camisetas))
