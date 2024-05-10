from Vehiculo import Vehiculo

class AutomovilVolador(Vehiculo):
    def __init__(self, color, marca, aceleracion, velocidad, esta_volando=False):
        """
        Constructor de la clase AutomovilVolador.
        """
        super().__init__(color, marca, aceleracion, velocidad)
        self.ruedas = 6
        self.esta_volando = esta_volando

    def volar(self):
        """
        Método que simula la acción de volar un automóvil volador.
        """
        self.esta_volando = True
        print("El automóvil volador está volando.")

    def aterrizar(self):
        """
        Método que simula la acción de aterrizar un automóvil volador.
        """
        self.esta_volando = False
        print("El automóvil volador aterrizó.")

    def conducir(self):
        """
        Método que simula la acción de conducir un automóvil volador.
        """
        print("El automóvil volador está siendo conducido.")

