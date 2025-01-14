"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
"""

def soma(a, b):
    menor = min(len(a), len(b))
    lista = [a[i]+b[i] for i in range(menor)]
    return lista

lista_a     = [1, 2, 3, 5, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

print(soma(lista_a, lista_b))