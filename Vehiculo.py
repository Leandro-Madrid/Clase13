from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase abstracta que define un vehículo.
    """
    def __init__(self, color, marca, aceleracion, velocidad):
        """
        Constructor de la clase Vehiculo.
        """
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    @abstractmethod
    def conducir(self):
        """
        Método abstracto que simula la acción de conducir un vehículo.
        """
        pass
    
    @abstractmethod
    def volar(self):
        """
        Método abstracto que simula la acción de volar un vehículo.
        """
        pass

    def acelerar(self):
        """
        Aumenta la velocidad del vehículo en función de la aceleración.
        """
        self.velocidad += self.aceleracion

    def frenar(self, reduccion):
        """
        Reduce la velocidad del vehículo en función de una cantidad de reducción.

        Args:
            reduccion (int): Cantidad en la que se reduce la velocidad.
        """
        self.velocidad -= reduccion
        if self.velocidad < 0:
            self.velocidad = 0



