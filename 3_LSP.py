""" Principio de sustitución de Liskov

Problema:
En el siguiente código la clase Bicicleta viola la LSP. Esto sucede porque la clase auto, tiene 
un método de motor, en cambio, la bicicleta es asistida por pedales, entonces por ende, el código
no aplicaría. """

class Vehiculos:
	#Clase vehículos

	def __init__(self, nombre: str, velocidad: float):
					self.nombre = nombre
					self.velocidad = velocidad

	def obtener_nombre(self) -> str:
    # Obtener nombre del vehículo
					return f"El nombre del vehículo {self.nombre}"

	def obtener_velocidad(self) -> float:
    # Obtener velocidad del vehículo
					return f"la velocidad del vehículo {self.velocidad}"

	def motor(self):
    # Un vehículo de motor
					pass

	def arrancar_motor(self):
    # Arrancar un vehículo de motor
					self.motor()

class Carro(Vehiculos):
	#Clase carro

	def arrancar_motor(self):
					pass

class Bicicleta(Vehiculos):
	#Clase bicicleta

	def arrancar_motor(self):
					pass

"""
Solución:
Para solucionar este problema, debemos reconstruir el código """

class Vehiculos:
	#Clase vehículos

	def __init__(self, nombre: str, velocidad: float):
					self.nombre = nombre
					self.velocidad = velocidad

	def obtener_nombre(self) -> str:
    # Obtener nombre del vehículo
					return f"El nombre del vehículo {self.nombre}"

	def obtener_velocidad(self) -> float:
    # Obtener velocidad del vehículo
					return f"la velocidad del vehículo {self.velocidad}"

class Vehiculos_sin_motor(Vehiculos):
	#Clase vehículos sin motor

	def arrancar_moviendo(self):
    # Arrancarlos moviéndolos
					raise NotImplemented

class Vehiculos_con_motor(Vehiculos):
	#Clase vehículos con motor

	def motor(self):
    # Arrancarlos con el motor
					pass                   

	def arrancar_motor(self):
    # Un vehículo arranca el motor
					self.motor()

class Carro(Vehiculos):
	#Clase carro

	def arrancar_motor(self):
					pass

class Bicicleta(Vehiculos):
	#Clase bicicleta

	def arrancar_moviendo(self):
					pass
