import json
import tkinter as tk
from tkinter import messagebox
import customtkinter

class Prueba:
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
		return [Prueba.de_json(json.dumps(dato)) for dato in datos]

	@staticmethod
	def cargar_eventos2(njson):
		datos = njson
		return [Prueba.de_json(json.dumps(dato)) for dato in datos]

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

# Función para manejar el botón de "Agregar evento"
def agregar_evento_click():
	# Obtener los datos ingresados por el usuario desde los campos de entrada
	nombre = nombre_entry.get()
	imagen = imagen_entry.get()
	id_ubicacion = id_ubicacion_entry.get()
	id = id_entry.get()
	artista = artista_entry.get()
	genero = genero_entry.get()
	hora_inicio = hora_inicio_entry.get()
	hora_fin = hora_fin_entry.get()

	resultado = messagebox.askyesno(message="¿Esta seguro de Guardar el Evento?", title="Confirmacion")
	if not resultado:
		ventana.destroy()
		return
	# Agregar el evento llamando al método agregar_evento
	Evento.agregar_evento("eventos.json", nombre, imagen, id_ubicacion, id, artista, genero, hora_inicio, hora_fin)

	# Mostrar un mensaje de confirmación al usuario
	messagebox.showinfo("Evento agregado", "El evento ha sido agregado correctamente.")

def ventana_agregar_evento():
	# Crear la ventana principal de la aplicación
	#ventana = tk.Tk()
	ventana = customtkinter.CTk()
	ventana.title("Agregar Evento")
	ventana.geometry('300x450')
	
	# Crear y posicionar los campos de entrada y etiquetas para cada dato del evento
	nombre_label = tk.Label(ventana, text="Nombre:")
	nombre_label.pack()
	nombre_entry = tk.Entry(ventana)
	nombre_entry.pack()
	
	imagen_label = tk.Label(ventana, text="Imagen:")
	imagen_label.pack()
	imagen_entry = tk.Entry(ventana)
	imagen_entry.pack()
	
	id_ubicacion_label = tk.Label(ventana, text="ID Ubicación:")
	id_ubicacion_label.pack()
	id_ubicacion_entry = tk.Entry(ventana)
	id_ubicacion_entry.pack()
	
	id_label = tk.Label(ventana, text="ID:")
	id_label.pack()
	id_entry = tk.Entry(ventana)
	id_entry.pack()
	
	artista_label = tk.Label(ventana, text="Artista:")
	artista_label.pack()
	artista_entry = tk.Entry(ventana)
	artista_entry.pack()
	
	genero_label = tk.Label(ventana, text="Género:")
	genero_label.pack()
	genero_entry = tk.Entry(ventana)
	genero_entry.pack()
	
	hora_inicio_label = tk.Label(ventana, text="Hora de inicio:")
	hora_inicio_label.pack()
	hora_inicio_entry = tk.Entry(ventana)
	hora_inicio_entry.pack()
	
	hora_fin_label = tk.Label(ventana, text="Hora de fin:")
	hora_fin_label.pack()
	hora_fin_entry = tk.Entry(ventana)
	hora_fin_entry.pack()
	
	# Crear el botón de "Agregar evento"
	agregar_evento_button = tk.Button(ventana, text="Agregar evento", command=agregar_evento_click)
	agregar_evento_button.pack()
	
	# Iniciar el bucle principal de la aplicación
	ventana.mainloop()
	
