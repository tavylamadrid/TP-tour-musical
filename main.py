import tkinter as tk
import customtkinter
from controller.controlador_principal import ControladorPrincipal

#root = tk.Tk()
root = customtkinter.CTk()
root.title("Tour Musical")
controlador = ControladorPrincipal(root)
root.mainloop()
