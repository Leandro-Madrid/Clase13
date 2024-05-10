from clases.Vehiculo import Vehiculo

# Clase AutomovilVolador.
class AutomovilVolador(Vehiculo):
    
    # Constructor de la clase AutomovilVolador.
    def __init__(self, color, marca, aceleracion, velocidad, anio, modelo, esta_volando=False):
        super().__init__(color, marca, aceleracion, velocidad, anio, modelo)
        self.ruedas = 6
        self.esta_volando = esta_volando

    # Método que simula la acción de volar un automóvil volador.
    def volar(self):
        self.esta_volando = True
        print("El automóvil volador está volando.")

    #Método que simula la acción de aterrizar un automóvil volador.
    def aterrizar(self):
        self.esta_volando = False
        print("El automóvil volador aterrizó.")

    # Método que simula la acción de conducir un automóvil volador.
    def conducir(self):
        print("El automóvil volador está siendo conducido.")

