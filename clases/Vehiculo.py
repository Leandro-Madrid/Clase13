from abc import ABC, abstractmethod

# Clase abstracta Vehiculo.
class Vehiculo(ABC):
    
    # Constructor de la clase Vehiculo.
    def __init__(self, color, marca, aceleracion, velocidad, anio, modelo):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self._anio = anio
        self.__modelo = modelo
    

    def get_anio (self):
        return self._anio

    def get_modelo (self):
        return self.__modelo
    
    def set_anio (self, anio):
        self._anio = anio

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

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

    # Imprimir info
    def info(self):
        print(self.color)
        print(self.marca)
        print(self.aceleracion)
        print(self.velocidad)
        print(self._anio)
        print(self.__modelo)


