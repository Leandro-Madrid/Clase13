from abc import ABC, abstractmethod

# Clase abstracta Vehiculo.
class Vehiculo(ABC):
    
    # Constructor de la clase Vehiculo.
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    # Método abstracto que simula la acción de conducir un Vehiculo.
    @abstractmethod
    def conducir(self):
        pass
    
    # Método abstracto que simula la acción de volar un Vehiculo.
    @abstractmethod
    def volar(self):
        pass

    # Aumenta la velocidad del Vehiculo en función de la aceleración.
    def acelerar(self):
        self.velocidad += self.aceleracion

    # Reduce la velocidad del Vehiculo en función de una cantidad de reducción.
    def frenar(self, reduccion):
        self.velocidad -= reduccion
        if self.velocidad < 0:
            self.velocidad = 0



