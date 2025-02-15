class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


celta = Carro('celta')
v8 = Motor('v8')
volvo = Fabricante('volvo')
celta.fabricante = volvo
celta.motor = v8

print(celta.nome, celta.fabricante.nome, celta.motor.nome, sep='\n')

