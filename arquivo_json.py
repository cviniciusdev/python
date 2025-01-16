import json

# pessoa = {
#     'nome': 'Carlãoç',
#     'idade' : 32,
#     'Solteiro' : False,
#     'endereço' : [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa)