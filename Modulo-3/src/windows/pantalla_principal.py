import PySimpleGUI as sg

def build():
    """
    Construye la ventana principal
    """
    #El tema hay que ponerlo siempre primero sino no funciona
    sg.theme('SystemDefault')

    layout = [
        [sg.Text("Expedientes del dia")],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expediente", key="-INGRESAR_EXPEDIENTE-")],
        [sg.Table(values=[["-","-","-","-","-","-"]], key="-TABLA_EXPEDIENTES-",justification="c",
            headings=[" Codigo ", "    Empresa    ", "   CUIT  ", " Telefono ", " Categoria "],
            row_height=20, num_rows=10,header_background_color="#FF8000"
        )]
    ]

    window = sg.Window("Sistema integral v1.0", layout=layout, resizable=True)
    return window