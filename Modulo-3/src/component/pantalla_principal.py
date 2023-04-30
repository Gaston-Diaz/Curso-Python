import PySimpleGUI as sg
from src.windows import pantalla_principal

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

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit-", "Salir"):
            break
        
    return window
