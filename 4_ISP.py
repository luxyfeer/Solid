""" Principio de la segregación de interfaces

Problema:
En el siguiente ejemplo,se viola el principio ISP porque estamos llamando un método
innecesario en la clase círculo"""

class Forma:
	#Clase forma
	def dibujar_circulo(self):
		# Dibujar un círculo
					raise NotImplemented

	def dibujar_cuadrado(self):
		# Dibujar un cuadrado
					raise NotImplemented

class Circulo(Forma):
	#Clase círculo
	def dibujar_circulo(self):
		# Dibujar un círculo
					pass

	def dibujar_cuadrado(self):
		# Dibujar un cuadrado
					pass
