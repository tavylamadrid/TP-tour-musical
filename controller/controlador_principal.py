from views.vista_principal import VistaPrincipal
from models.evento import Evento
from models.ubicacion import Ubicacion
from models.ruta import Ruta
from PIL import Image, ImageTk
import tkinter as tk
from tkintermapview import TkinterMapView
from tkinter import messagebox

class ControladorPrincipal:
	def __init__(self, root):
		self.vista = VistaPrincipal(root, self.seleccionar_evento, seleccionar_ubicacion, self.seleccionar_ruta, self.seleccionar_ruta_all, self.buscar_evento_filtro, self.buscar_evento_genero)
		self.eventos = Evento.cargar_eventos("./data/eventos.json")
		self.ubicaciones = Ubicacion.cargar_ubicaciones("./data/ubicaciones.json")
		self.rutas = Ruta.cargar_rutas("./data/rutas.json")
		
		self.marcadores = []
		self.imagenes = []
		self.destinos = []
		self.cargar_eventos()
		self.cargar_imagenes()
		self.cargar_marcadores()
		
		self.cargar_rutas()
		
	def cargar_locales(self):
		for local in self.locales:
			self.vista.agregar_local(local)

	def cargar_eventos(self):
		for evento in self.eventos:
			self.vista.agregar_evento(evento)

	def cargar_rutas(self):
		for ruta in self.rutas:
			self.vista.agregar_ruta(ruta)
	
	def cargar_imagenes(self):
		for evento in self.eventos:
			imagen = ImageTk.PhotoImage(Image.open(f"./views/images/{evento.imagen}").resize((200, 200)))
			self.imagenes.append(imagen)

	def cargar_marcadores(self):
		for ubicacion, evento in zip(self.ubicaciones, self.eventos):
			imagen = self.imagenes[ubicacion.id - 1]
			marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, evento.nombre, imagen)
			marcador.hide_image(True)
			self.marcadores.append(marcador)

	def seleccionar_evento(self, event):
		# Obtiene el índice del elemento seleccionado
		indice_seleccionado = self.vista.lista_eventos.curselection()
		# Obtiene el local seleccionado
		evento_seleccionado = self.eventos[indice_seleccionado[0]]
		
		print(f"el evento es: {evento_seleccionado.nombre}")
		ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
		# Busca la ubicación correspondiente al local seleccionado
		for ubicacion in self.ubicaciones:
			if ubicacion.id == evento_seleccionado.id_ubicacion:
				ubicacion_seleccionada = ubicacion
				break
		# Centra el mapa en la ubicación seleccionada
		self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
		print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

	def buscar_evento_filtro(self):
		nombre = self.vista.lista_input1.get()
		#nombre = 'tributo'
		
		self.vista.lista_eventos.delete(0,tk.END)
		"""
		self.marcadores[0].set_position(0, 0)
		self.marcadores[1].set_position(0, 0)
		self.marcadores[2].set_position(0, 0)
		self.marcadores[3].set_position(0, 0)
		self.marcadores[4].set_position(0, 0)
		self.marcadores[5].set_position(0, 0)
		
		self.marcadores[6].set_position(0, 0)
		self.marcadores[7].set_position(0, 0)
		self.marcadores[8].set_position(0, 0)
		self.marcadores[9].set_position(0, 0)
		"""
		
		for marca in self.marcadores:
			marca.set_position(0, 0)
		
		#print(f"el nombre ruta es: {ruta_seleccionado.nombre}")
		#print(f"el ID ruta es: {ruta_seleccionado.id}")
	#for destino in 1,2,3,4,5,6,7,8,9:
		#print(f"el destino ruta (eventos) es: {destino}")
		destino = 1
		for evento, ubicacion in zip(self.eventos, self.ubicaciones):
			if nombre.lower() in evento.nombre.lower():
				print(f"para el nombre {nombre} el evento es {evento.nombre}")
				#if evento.id_ubicacion == ubicacion.id:
				lat=ubicacion.latitud
				lon=ubicacion.longitud
				nom=evento.nombre
				indice=destino-1
				print(f"latitud {ubicacion.latitud} para evento {evento.nombre}")
				print(f"Indice {indice} id evento {evento.id}")
				self.marcadores[indice].set_position(lat, lon)
				self.vista.lista_eventos.insert(tk.END, nom)
				#break
			destino += 1

	def buscar_evento_genero(self):
		nombre = self.vista.lista_input1.get()
		#nombre = 'tributo'
		
		self.vista.lista_eventos.delete(0,tk.END)
		"""
		self.marcadores[0].set_position(0, 0)
		self.marcadores[1].set_position(0, 0)
		self.marcadores[2].set_position(0, 0)
		self.marcadores[3].set_position(0, 0)
		self.marcadores[4].set_position(0, 0)
		self.marcadores[5].set_position(0, 0)
		"""
		for marca in self.marcadores:
			marca.set_position(0, 0)

		#print(f"el nombre ruta es: {ruta_seleccionado.nombre}")
		#print(f"el ID ruta es: {ruta_seleccionado.id}")
	#for destino in 1,2,3,4,5,6,7,8,9:
		#print(f"el destino ruta (eventos) es: {destino}")
		destino = 1
		for evento, ubicacion in zip(self.eventos, self.ubicaciones):
			if nombre.lower() in evento.genero.lower():
				#print(f"para el nombre {nombre} el evento es {evento.nombre}")
				#if evento.id_ubicacion == ubicacion.id:
				lat=ubicacion.latitud
				lon=ubicacion.longitud
				nom=evento.nombre
				indice=destino-1
				#print(f"latitud {ubicacion.latitud} para evento {evento.nombre}")
				#print(f"Indice {indice} id evento {evento.id}")
				self.marcadores[indice].set_position(lat, lon)
				self.vista.lista_eventos.insert(tk.END, nom)
				#break
			destino += 1

	def seleccionar_ruta(self, event):
		#self.cargar_marcadores()
		indice_seleccionado = self.vista.lista_rutas.curselection()
		#print(indice_seleccionado)
		ruta_seleccionado = self.rutas[indice_seleccionado[0]]
		self.vista.lista_eventos.delete(0,tk.END)
		
		"""
		self.marcadores[0].set_position(0, 0)
		self.marcadores[1].set_position(0, 0)
		self.marcadores[2].set_position(0, 0)
		self.marcadores[3].set_position(0, 0)
		self.marcadores[4].set_position(0, 0)
		self.marcadores[5].set_position(0, 0)
		"""
		for marca in self.marcadores:
			marca.set_position(0, 0)
			
		#print(f"el nombre ruta es: {ruta_seleccionado.nombre}")
		#print(f"el ID ruta es: {ruta_seleccionado.id}")
		for destino in ruta_seleccionado.destinos:
			#print(f"el destino ruta (eventos) es: {destino}")
			for evento, ubicacion in zip(self.eventos, self.ubicaciones):
				if int(evento.id) == destino:
					#print(f"para el destinopasooo2 {destino} el evento es {evento.nombre}")
					if evento.id_ubicacion == ubicacion.id:
						lat=ubicacion.latitud
						lon=ubicacion.longitud
						nom=evento.nombre
						indice=destino-1
						#print(f"latitud {ubicacion.latitud} para evento {evento.nombre}")
						self.marcadores[indice].set_position(lat, lon)
						self.vista.lista_eventos.insert(tk.END, nom)
						break

	def seleccionar_ruta_all(self):
		self.vista.lista_eventos.delete(0,tk.END)
		for destino in 1,2,3,4,5,6,7,8,9:
			#print(f"el destino ruta (eventos) es: {destino}")
			for evento, ubicacion in zip(self.eventos, self.ubicaciones):
				if int(evento.id) == destino:
					#print(f"para el destinopasooo2 {destino} el evento es {evento.nombre}")
					if evento.id_ubicacion == ubicacion.id:
						lat=ubicacion.latitud
						lon=ubicacion.longitud
						nom=evento.nombre
						indice=destino-1
						#print(f"latitud {ubicacion.latitud} para evento {evento.nombre}")
						self.marcadores[indice].set_position(lat, lon)
						self.vista.lista_eventos.insert(tk.END, nom)
						break

def seleccionar_ubicacion(marcador):
	if marcador.image_hidden is True:
		marcador.hide_image(False)
	else:
		marcador.hide_image(True)
	print("Ubicación seleccionada: ", marcador.text)
