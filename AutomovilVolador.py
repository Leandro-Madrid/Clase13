from Automovil import Automovil

"""
Crear una clase AutomovilVolador
"""

from Automovil import Automovil

class AutomovilVolador(Automovil):
    ruedas = 6
    
    def __init__(self, color, marca, aceleracion, velocidad, esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False


