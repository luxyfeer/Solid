""" Principio de abierto - cerrado

Problema:
Este ejemplo no pasaría el principio de abierto-cerrado, si agregáramos un cliente super VIP
y quisiésemos ofrecerle un descuento del 8%, deberíamos replantear el código para que pase el OCP. """

class Descuento:
	#Clase de descuento
	def __init__(self, cliente, precio):
					self.cliente = cliente
					self.precio = precio

def dar_descuento(self):
	# Método para dar descuento
	if self.cliente == "normal":
		return self.precio * 0.2
	elif self.cliente == "vip":
		return self.precio * 0.4

"""
Solución:
Para no violar OCP , debemos extender el método mas no modificarlo, para poder darle el descuento al
super VIP """

class Descuento:
	#Clase de decuento
	def __init__(self, cliente, precio):
					self.cliente = cliente
					self.precio = precio

	def dar_descuento(self):
		# Método de descuento
		return self.precio * 0.2

class VIPDescuento:
	#Clase de descuento para cliente VIP
	def dar_descuento(self):
		# Método de descuento
		return super().dar.descuento() * 4

class SuperVIPDescuento:
	#Clase de descuento para cliente Super VIP
	def dar_descuento(self):
		# Método de descuento
		return super().dar.descuento() * 8
