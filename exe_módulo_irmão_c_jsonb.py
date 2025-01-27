from exercicio_classe_json import Pessoa
import json

with open('exercicio_classe_json.json', 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome)
