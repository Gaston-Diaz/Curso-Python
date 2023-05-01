import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_expediente
from src.handlers import ingresar_expediente_handler

def start():
    """
    Lanza la ejecucion de la ventana
    """
    window = loop()
    window.close()

def loop():
    """
    Loop de la ventana de menu que capta los eventos al apretar las opciones
    """
    window = pantalla_principal.build()
    window["-TABLA_EXPEDIENTES-"].update(ingresar_expediente_handler.leer_archivo())

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit-", "Salir"):
            break
        
        elif event == '-INGRESAR_EXPEDIENTE-':
            ingresar_expediente.start()
            window["-TABLA_EXPEDIENTES-"].update(ingresar_expediente_handler.leer_archivo())

    return window
