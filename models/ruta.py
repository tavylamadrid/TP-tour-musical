import json

class Ruta:
	def __init__(self, nombre, destinos, id):
		self.nombre = nombre
		self.id = id
		self.destinos = destinos

	def a_json(self):
		return json.dumps(self.__dict__)

	@classmethod
	def de_json(cls, datos_json):
		datos = json.loads(datos_json)
		return cls(**datos)

	@staticmethod
	def cargar_rutas(archivo_json):
		with open(archivo_json, "r") as archivo:
			datos = json.load(archivo)
		return [Ruta.de_json(json.dumps(dato)) for dato in datos]
