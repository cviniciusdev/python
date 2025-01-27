import json

class Pessoa:
    ano = 2023 # Atributo de classe ---------------------------------------------

    def __init__(self, nome, idade): # Método normal de classe ---------------------------------------------
        self.nome = nome
        self.idade = idade

    # Método de classe ---------------------------------------------
    @classmethod
    def metodo_de_classe1(cls):
        print('Sou um método de classe')

    # Factory method ---------------------------------------------
    @classmethod
    def metodo_de_classe(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('Carlos', 32)
p2 = Pessoa('Leticia', 17)
p3 = Pessoa('Lucas', 76)
bd = (vars(p1), vars(p2), vars(p3))

print(p2.idade)

def fazer_dump():
    with open('exercicio_classe_json.json', 'w', encoding='utf-8') as arquivo:
        print('Fazendo dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

p4 = Pessoa.metodo_de_classe('Helena')
print(p4.nome, p4.idade)

if(__name__ == '__main__'): 
    fazer_dump()