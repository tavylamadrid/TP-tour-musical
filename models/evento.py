import json

class Evento:
	def __init__(self, nombre, imagen, id_ubicacion, id, artista, genero, hora_inicio, hora_fin):
		self.nombre = nombre
		self.imagen = imagen
		self.id_ubicacion = id_ubicacion
		self.id = id
		self.artista = artista
		self.genero = genero
		self.hora_inicio = hora_inicio
		self.hora_fin = hora_fin

	def a_json(self):
		return json.dumps(self.__dict__)

	@classmethod
	def de_json(cls, datos_json):
		datos = json.loads(datos_json)
		return cls(**datos)

	@staticmethod
	def cargar_eventos(archivo_json):
		with open(archivo_json, "r") as archivo:
			datos = json.load(archivo)
		return [Evento.de_json(json.dumps(dato)) for dato in datos]

	@staticmethod
	def cargar_eventos2(njson):
		datos = njson
		return [Evento.de_json(json.dumps(dato)) for dato in datos]

	@staticmethod
	def buscar_por_artista(eventos, artista):
		resultados = []
		for evento in eventos:
			if evento.artista.lower() == artista.lower():
				resultados.append(evento)
		return resultados

	@staticmethod
	def buscar_por_genero(eventos, genero):
		resultados = []
		for evento in eventos:
			if evento.genero.lower() == genero.lower():
				resultados.append(evento)
		return resultados

	@staticmethod
	def buscar_por_lugar(eventos, id_ubicacion):
		resultados = []
		for evento in eventos:
			if evento.id_ubicacion == id_ubicacion:
				resultados.append(evento)
		return resultados

	@staticmethod
	def buscar_por_nombre(eventos, nombre):
		resultados = []
		for evento in eventos:
			if evento.nombre.lower() == nombre.lower():
				resultados.append(evento)
		return resultados

	@staticmethod
	def agregar_evento(archivo_json, nombre, imagen, id_ubicacion, id, artista, genero, hora_inicio, hora_fin):
		nuevo_evento = Evento(nombre, imagen, id_ubicacion, id, artista, genero, hora_inicio, hora_fin)

		eventos_actuales = Evento.cargar_eventos(archivo_json)
		eventos_actuales.append(nuevo_evento)

		with open(archivo_json, "w") as archivo:
			json.dump([evento.__dict__ for evento in eventos_actuales], archivo)
