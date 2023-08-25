from hora import Hora
from minuto import Minuto
from segundo import Segundo

class Cronometro():
    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()

    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == 0:
            self.minuto.avanzar()
            if self.minuto.valor == 0:
                self.hora.avanzar()