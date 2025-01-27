
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def acelerar(self):
        print(f'{self.marca} está acelerando...')
    

celta = Carro('Fusca', 1992)
monza = Carro('Monza', 1987)

print(celta.marca)
print(celta.ano)

celta.acelerar()
monza.acelerar()