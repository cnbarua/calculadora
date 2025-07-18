def centrar_ventana(ventana, app_ancho, app_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()

    x = int((pantalla_ancho/2) * (app_ancho/2))
    x = int((pantalla_largo/2) * (app_largo/2))
    
    return ventana.geometry(f'{app_ancho}x{app_largo}*{x}+{y}')