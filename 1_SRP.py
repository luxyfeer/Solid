""" Principio de la responsabilidad única. 

Problema:
En el siguiente ejemplo, estamos realizando dos tareas, una es la obtención 
de los datos y la otra es almacenar los datos en una base de datos. Esto viola el SRP."""

class Cuenta:
	#Clase cuenta
	def __init__(self, cuenta_no: str):
					self.cuenta_no = cuenta_no

	def obtener_cuenta_no(self):
	# Obtener el número de cuenta
					return self.cuenta_no

	def salvar(self):
	# Guardar el número de cuenta en una BD
					pass				

"""Solución:
La manera es crear otra clase para que maneje la administración de la Base de Datos
Así la clase cliente solo manejará sus propiedades. """

class CuentaBD:
	# Clase cuenta de administración de bases de datos

	def obtener_cuenta_no(self):
	# Obtener el número de cuenta
					pass

	def salvar_cuenta(self, obj):
	# Guardar el número en base de datos
					pass				

class Cuenta:
	# Clase cuenta
	def __init__(self, cuenta_no: str):
					self.cuenta_no = cuenta_no
					self._bd = CuentaBD()

	def obtener_cuenta_no(self, _id):
	# Obtener el número de cuenta
					return self._db.obtener_cuenta_no (_id=_id)

	def salvar(self):
		# Salvar cuenta
		self.db.salvar_cuenta (obj=self)
