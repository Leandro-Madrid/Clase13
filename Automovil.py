from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, color, marca, aceleracion, velocidad):
        """
        Constructor de la clase Automovil.
        """
        super().__init__(color, marca, aceleracion, velocidad)
        self.ruedas = 4

    def conducir(self):
        """
        Método que simula la acción de conducir un automóvil.
        """
        print("El automóvil está siendo conducido.")

    def volar(self):
        """
        Implementación del método abstracto volar para la clase Automovil.
        """
        print("¡Los automóviles no pueden volar!")
