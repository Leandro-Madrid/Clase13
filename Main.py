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
11- Agregar dos métodos abstractos en clases correspondientes volar() y conducir()
12- Crea clase Vehiculo con año (protegido) y modelo (privado)
13- Mostrar atributos de vehiculo
14- Realizar get y set
15- Mostrar por consola, modificar y mostrar
"""
from clases.Automovil import Automovil
from clases.AutomovilVolador import AutomovilVolador

from funciones.operaciones import suma as s


# print (s(5,6))

# Crear un automóvil
coche1 = Automovil("Rojo", "Toyota", 10, 0, 2020, "Full")
# print(f"El coche 1 tiene {coche1.ruedas} ruedas y una aceleración de {coche1.aceleracion}")

# Modificar la aceleración y mostrar en pantalla ambas aceleraciones.
# coche1.aceleracion = 20
# print(f"El coche 1 tiene una aceleración de {coche1.aceleracion}")

# Acelerar el coche
# coche1.acelerar()

# Crear una segunda instancia de Automovil
# coche2 = Automovil("Negro", "Honda", 8, 0, 2022, "Base")
# print(f"El coche 2 tiene {coche2.ruedas} ruedas y una aceleración de {coche2.aceleracion}")

# Frenar el segundo coche
# coche2.frenar(5)

# Mostrar la velocidad después de frenar
# print("Velocidad actual del segundo coche después de frenar:", coche2.velocidad)

# Crear un automóvil volador. Usar volar y aterrizar
automovil_volador1 = AutomovilVolador("Azul", "Renault", 8, 0, 1960, "NC")

# print(f"El automóvil volador es de color {automovil_volador1.color}, marca {automovil_volador1.marca}, con {automovil_volador1.ruedas} ruedas, y tiene una aceleración de {automovil_volador1.aceleracion}. Está volando: {automovil_volador1.esta_volando}")

# automovil_volador1.volar()

# print(f"El automóvil volador es de color {automovil_volador1.color}, marca {automovil_volador1.marca}, con {automovil_volador1.ruedas} ruedas, y tiene una aceleración de {automovil_volador1.aceleracion}. Está volando: {automovil_volador1.esta_volando}")

# automovil_volador1.aterrizar()

# print(f"El automóvil volador es de color {automovil_volador1.color}, marca {automovil_volador1.marca}, con {automovil_volador1.ruedas} ruedas, y tiene una aceleración de {automovil_volador1.aceleracion}. Está volando: {automovil_volador1.esta_volando}")

# Intentar hacer volar un automóvil regular
# coche1.volar()

print("Info coche 1:")
coche1.info()

coche1._anio = 2025

print("Info coche 1: año nuevo")
coche1.info()

coche1.set_modelo("Base")

print("Info coche 1: modelo nuevo")
coche1.info()

print(coche1.get_modelo())