"""
1- Crear una clase Automóvil con tenga por defecto atributo ruedas inicializado en 4, con un constructor con los parámetros de color, marca, aceleracion y velocidad.
2- Crear un coche, mostrar por consola las ruedas y la aceleración
3- Modificar la aceleración y mostrar por pantalla ambas aceleraciones
4- Crear método acelera() que aumentará la velocidad + aceleración
5- Crear método frena() que restará a la velocidad la aceleración
6- Crear una 2da instancia de la clase , frenar y ver los resultados
7- Crear clase AutomovilVolador que herede de Automovil con atributo de 6 ruedas
8- Agregar al constructor esta_volando=True
9- Agregar métodos vuela y aterriza(esta_volando)
10- Crear un automovilvolador y muestre por consola comportamiento y características
11 - Agregar dos métodos abstractos en clases correspondientes volar() y conducir()
"""

from Automovil import Automovil
from AutomovilVolador import AutomovilVolador

# Crear un coche y mostrar en consola las ruedas y la aceleración
coche1 = Automovil("Rojo", "Toyota", 10, 0)
print(f"El coche 1 tiene {coche1.ruedas} ruedas y una aceleración de {coche1.aceleracion}")

# Modificar la aceleración y mostrar en pantalla ambas aceleraciones.
coche1.aceleracion = 20
print(f"El coche 1 tiene una aceleración de {coche1.aceleracion}")

# Acelerar el coche
coche1.acelerar()

# Crear una segunda instancia de Automovil
coche2 = Automovil("Azul", "Honda", 8, 0)
print(f"El coche 2 tiene {coche2.ruedas} ruedas y una aceleración de {coche2.aceleracion}")

# Frenar el segundo coche
coche2.frenar(5)

# Mostrar la velocidad después de frenar
print("Velocidad actual del segundo coche después de frenar:", coche2.velocidad)

automovil_volador1 = AutomovilVolador("Azul", "Honda", 8, 0)

print(f"El automóvil volador es de color {automovil_volador1.color}, marca {automovil_volador1.marca}, con {automovil_volador1.ruedas} ruedas, y tiene una aceleración de {automovil_volador1.aceleracion}. Está volando: {automovil_volador1.esta_volando}")

automovil_volador1.aterriza()

print(f"El automóvil volador es de color {automovil_volador1.color}, marca {automovil_volador1.marca}, con {automovil_volador1.ruedas} ruedas, y tiene una aceleración de {automovil_volador1.aceleracion}. Está volando: {automovil_volador1.esta_volando}")
