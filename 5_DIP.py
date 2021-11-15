""" Principio de inversión de dependencias

Problema:
En el siguiente ejemplo,las clases DesarrolladorBackend y DesarrolladorFrontend son
módulos de bajo nivel, mientras la clase proyecto es un módulo de alto nivel, que dependen de
los de bajo nivel, en este caso, se viola el DIP """

class DesarrolladorBackend:
	#Este es un módulo de bajo nivel
	@staticmethod
	def python():
					print("Escribiendo código python")

class DesarrolladorFrontend:
	#Este es un módulo de bajo nivel
	@staticmethod
	def javascript():
					print("Escribiendo código javascript")

class Proyecto:
	#Este es un módulo de alto nivel
	def __init__(self):
		self.backend =DesarrolladorBackend()
		self.frontend =DesarrolladorFrontend()

	def desarrollo(self):
		self.backend.python
		self.frontend.javascript
		return "Desarrollo de código"

proyecto = Proyecto()
print(proyecto.desarrollo())

"""
Solución:
Resolveremos el código para que no haya dependencia de los módulos de alto nivel, con los de
bajo nivel, sino que, dependan de las abstracciones"""

class DesarrolladorBackend:
	#Este es un módulo de bajo nivel
	def desarrollo():
					self._codigo_python()

	@staticmethod
	def _codigo_python():
					print("Escribiendo código python")

class DesarrolladorFrontend:
	#Este es un módulo de bajo nivel
	def desarrollo():
					self._codigo_javascript()

	@staticmethod
	def _codigo_javascript():
					print("Escribiendo código javascript")

class Desarrolladores:
	#Este es un módulo abstracto
	def __init__(self):
					self.backend = DesarrolladorBackend
					self.frontend = DesarrolladorFrontend	

	def desarrollo(self):
					self.backend.desarrollo()
					self.frontend.desarrollo()	

class Proyecto:
	#Este es un módulo de alto nivel
	def __init__(self):
					self._desarrolladores = Desarrolladores()	
	def desarrollo(self):
					return self._desarrolladores.desarrollo
proyecto = Proyecto()
print(proyecto.desarrollo())
