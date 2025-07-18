import tkinter as tk
from tkinter import font
from config import constantes as cons
import util.util_ventana as util_ventana

class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()
        self.construir_widget_toggle()
        
    def construir_widget_toggle(self):
        self.dark_theme = True
        font_awesome = font.Font(family="FontAwesome", size=12)
        self.theme_button = tk.Button(self, text="Modo oscuro \uf186", width=13, font=font_awesome, bd=0, borderwidth=0,
                  highlightthickness=0, relief=tk.FLAT, command=self.toggle_theme, bg=cons.BOTONES_ESPECIALES_LIGHT)
        self.theme_button.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky='nw')

    def toggle_theme(self):
        if self.dark_theme:
            self.configure(bg=cons.FONDO_LIGHT)
            self.entry.config(fg=cons.TEXTO_LIGHT, bg=cons.CAJA_TEXTO_LIGHT)
            self.operation_label.config(fg=cons.TEXTO_LIGHT, bg=cons.FONDO_LIGHT)
            self.theme_button.configure(text='Modo claro \uf185', relief=tk.SUNKEN, bg=cons.BOTONES_ESPECIALES_LIGHT)
            
        else:
            self.configure(bg=cons.FONDO_DARK)
            self.entry.config(fg=cons.TEXTO_DARK, bg=cons.CAJA_TEXTO_DARK)
            self.operation_label.config(fg=cons.TEXTO_DARK, bg=cons.FONDO_DARK)
            self.theme_button.configure(text='Modo claro \uf185', relief=tk.SUNKEN, bg=cons.BOTONES_ESPECIALES_DARK)
            
        self.dark_theme = not self.dark_theme

    def config_window(self):
        self.title('Calculadora con Tkinter')
        self.configure(bg=cons.FONDO_DARK)
        self.attributes('-alpha', 0.96)
        util_ventana.centrar_ventana(self, 370, 570)

    def construir_widget(self):
        #etiqueta
        self.operation_label = tk.Label(self, text='___', font=('Arial', 16), fg=cons.TEXTO_DARK, 
                                        bg=cons.FONDO_DARK, justify="right")
        self.operation_label.grid(row=0, column=3, padx=10, pady=10)

        #pantalla de operacion
        self.entry = tk.Entry(self, width=12, font=('Arial', 40), bd=0, fg=cons.TEXTO_DARK, 
                              bg=cons.CAJA_TEXTO_DARK, justify='right')
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        #lista de botones
        botones = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]
        row_val = 2
        col_val = 0

        roboto_font = font.Font(family="Roboto", size=16)

        for boton in botones:
            if boton in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.BOTONES_ESPECIALES_DARK
                boton_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.BOTONES_DARK
                boton_font = roboto_font
            
            tk.Button(self, text=boton, width=5, height=2, command=lambda b=boton: self.on_button_click(b),
                        bg=color_fondo, fg=cons.TEXTO_DARK, relief=tk.FLAT, 
                        font=boton_font, padx=5, pady=5, bd=0, 
                        borderwidth=0, highlightthickness=0,
                        overrelief='flat').grid(
                            row=row_val, column=col_val, pady=5)
            
            if boton == '=':
                tk.Button(self, text=boton, width=11, height=2, command=lambda b=boton: self.on_button_click(b),
                          bg=color_fondo, fg=cons.TEXTO_DARK, relief=tk.FLAT, 
                          font=boton_font, padx=5, pady=5, bd=0,
                          borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(
                              row=row_val, column=col_val, columnspan=2, pady=5)
            col_val += 1

            if(col_val > 3):
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        if value == '=':
            try:
                expresion = self.entry.get().replace('%', '/100')
                result = eval(expresion)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operacion = expresion + ' ' + value
                self.operation_label.config(text=operacion)

            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text='')

        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text='')

        elif value == '<':
            texto_actual = self.entry.get()
            if texto_actual:
                new_texto = texto_actual[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_texto)
                self.operation_label.config(text=new_texto+" ")
        else:
            texto_actual = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, texto_actual + value)
            if value == '=':
                self.operation_label.config(text='')