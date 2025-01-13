# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.1 if produto['preco'] > 20 else produto['preco']} for produto in produtos    
]


print(*novos_produtos, sep='\n')

# print(*produtos, sep='\n')