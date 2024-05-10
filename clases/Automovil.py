from clases.Vehiculo import Vehiculo

# Clase Automovil.
class Automovil(Vehiculo):

    # Constructor de la clase Automovil.
    def __init__(self, color, marca, aceleracion, velocidad, anio, modelo):
        super().__init__(color, marca, aceleracion, velocidad, anio, modelo)
        self.ruedas = 4

    # Método que simula la acción de conducir un automóvil.
    def conducir(self):
        print("El automóvil está siendo conducido.")

    # Implementación del método abstracto volar para la clase Automovil.
    def volar(self):
        print("¡Los automóviles no pueden volar!")
