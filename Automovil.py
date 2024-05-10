"""
Crear una clase Automovil
"""

class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.ruedas = 4

    def mostrar_ruedas_y_aceleracion(self):
        print("Número de ruedas:", self.ruedas)
        print("Aceleración:", self.aceleracion)

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self, reduccion):
        self.velocidad -= reduccion
        if self.velocidad < 0:
            self.velocidad = 0

