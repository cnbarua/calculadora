import tkinter as tk
from tkinter import font
from config import constantes as cons
import util.util_ventana as util_ventana

class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()

    def config_window(self):
        self.title('Calculadora con Tkinter')
        self.configure(bg=cons.FONDO_DARK)
        self.attributes('-alpha', 0.96)
        util_ventana.centrar(self, 370, 570)