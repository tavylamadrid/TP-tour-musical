import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
from tkinter.font import Font
import customtkinter
from models.evento import Evento

class VistaPrincipal:
	def __init__(self, root, seleccionar_evento_callback=None, seleccionar_ubicacion_callback=None, seleccionar_ruta_callback=None, seleccionar_ruta_all_callback=None, buscar_evento_filtro_callback=None, buscar_evento_genero_callback=None):
		self.root = root
		self.seleccionar_evento_callback = seleccionar_evento_callback
		self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
		self.seleccionar_ruta_callback = seleccionar_ruta_callback
		self.seleccionar_ruta_all_callback = seleccionar_ruta_all_callback
		self.buscar_evento_filtro_callback = buscar_evento_filtro_callback
		self.buscar_evento_genero_callback = buscar_evento_genero_callback
		self.frame_mapa = tk.Frame(self.root, width=900, height=600)
		self.frame_mapa.pack(side='right')
	
		#se aggrega fuente y colores
		texto_font = Font(family='Open Sans', size=14)
		texto_bg = '#2F242C'
		texto_fg= '#E5E5E5'
		titulo_font = Font(family='Roboto', size=16)
		titulo_bg = '#E6D884'
		titulo_fg= '#E5E5E5'
		
		self.frame_eventos = tk.Frame(self.root, width=300, height=600)
		self.frame_eventos.pack(side='left', fill='both', expand=True)

		self.frame_botones = tk.Frame(self.frame_eventos, width=200, height=600, bg=titulo_bg)
		self.frame_botones.pack(side='left', fill='both', expand=True)

		# Placeholder para el mapa
		self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
		self.mapa.set_position(-24.77616437851034, -65.41079411004006)
		self.mapa.set_zoom(16)
		self.mapa.pack(side='right')
		
		# Listbox para los eventos
		self.lista_eventos = tk.Listbox(self.frame_eventos, font=texto_font, bg=texto_bg, fg=texto_fg)
		self.lista_eventos.bind('<<ListboxSelect>>', seleccionar_evento_callback)
		self.lista_eventos.pack(fill='both', expand=True)
		#Titulo para los eventos
		self.titulo_evento = tk.Label(self.frame_eventos, text="Lista de Eventos!!!", font=titulo_font, fg=texto_bg)
		self.titulo_evento.pack()

		#input1
		self.lista_input1 = ttk.Entry(self.frame_botones, font=titulo_font)
		self.lista_input1.pack()

		#boton1
		self.lista_boton1 = tk.Button(self.frame_botones, text='Buscar por Genero', command=buscar_evento_genero_callback, font=titulo_font, bg=titulo_bg)
		self.lista_boton1.pack()
		#boton2
		self.lista_boton2 = tk.Button(self.frame_botones, text='Buscar por Evento', command=buscar_evento_filtro_callback, font=titulo_font, bg=titulo_bg)
		self.lista_boton2.pack()
		#boton3
		self.lista_boton3 = tk.Button(self.frame_botones, text='Todos los Eventos', command=seleccionar_ruta_all_callback, font=titulo_font, bg=titulo_bg)
		self.lista_boton3.pack()
		#boton4
		self.lista_boton3 = tk.Button(self.frame_botones, text=' Agregar  Eventos ', command=ventana_agregar_evento, font=titulo_font, bg=titulo_bg)
		self.lista_boton3.pack()
		#boton5
		self.lista_boton3 = tk.Button(self.frame_botones, text='  Aggregar  Rutas ', command=seleccionar_ruta_all_callback, font=titulo_font, bg=titulo_bg)
		self.lista_boton3.pack()

		#Titulo para las rutas
		self.titulo_ruta = tk.Label(self.frame_botones, text="Mis Rutas", font=titulo_font, bg=titulo_bg)
		self.titulo_ruta.pack()
		
		self.lista_rutas = tk.Listbox(self.frame_botones, font=texto_font, bg=texto_bg, fg=texto_fg)
		self.lista_rutas.bind('<<ListboxSelect>>', seleccionar_ruta_callback)
		self.lista_rutas.pack(fill='both', expand=True)

		
	def agregar_local(self, local):
		nombre = local.nombre
		self.lista_locales.insert(tk.END, nombre)

	def agregar_evento(self, evento):
		nombre = evento.nombre
		self.lista_eventos.insert(tk.END, nombre)
	
	def agregar_ruta(self, ruta):
		nombre = ruta.nombre
		self.lista_rutas.insert(tk.END, nombre)
	
	def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
		return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)

	def agregar_evento_click(ventana,nombre_entry,imagen_entry,id_ubicacion_entry,id_entry,artista_entry,genero_entry,hora_inicio_entry,hora_fin_entry):
		# Obtener los datos ingresados por el usuario desde los campos de entrada
		nombre = nombre_entry.get()
		imagen = imagen_entry.get()
		id_ubicacion = int(id_ubicacion_entry.get())
		print(f"a ver cuntop es el id ubi: {id_ubicacion}")
		id = id_entry.get()
		artista = artista_entry.get()
		genero = genero_entry.get()
		hora_inicio = hora_inicio_entry.get()
		hora_fin = hora_fin_entry.get()
		try:
			id_ubicacion = int(id_ubicacion)
		except ValueError:
			messagebox.showerror("Error", "El campo 'ID Ubicación' debe ser un número entero.")
			Sreturn
		resultado = messagebox.askyesno(message="¿Esta seguro de Guardar el Evento?", title="Confirmacion")
		if not resultado:
			ventana.destroy()
			return
		# Agregar el evento llamando al método agregar_evento
		Evento.agregar_evento("./data/eventos.json", nombre, imagen, id_ubicacion, id, artista, genero, hora_inicio, hora_fin)

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
	agregar_evento_button = tk.Button(ventana, text="Agregar evento", command=lambda: VistaPrincipal.agregar_evento_click(ventana,nombre_entry,imagen_entry,id_ubicacion_entry,id_entry,artista_entry,genero_entry,hora_inicio_entry,hora_fin_entry))
	agregar_evento_button.pack()
	
	# Iniciar el bucle principal de la aplicación
	#ventana.mainloop()
