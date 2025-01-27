class Carro: # Um motor e Um fabricante
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        print('PROPERTY')
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        print('PROPERTY')
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor: # Vários carros
    def __init__(self, nome):
        self.nome = nome

class Fabricante: # Fabrica vários carros
    def __init__(self, nome):
        self.nome = nome   


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)