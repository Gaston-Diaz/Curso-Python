import PySimpleGUI as sg
from src.windows import ingresar_expediente
from src.handlers import ingresar_expediente_handler

def start():
    """
    Lanza la ejecucion de la ventana
    """
    window = loop()
    window.close()

def loop():
    """
    Loop de la ventana menu que capta los eventos al apretar las opciones
    """
    window = ingresar_expediente.build()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit", "Salir"):
            break
    
        elif event == "-GUARDAR-":
            #Guardar los datos
            ingresar_expediente_handler.agregar_expedientes(values)
            break
    return window