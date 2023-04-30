import PySimpleGUI as sg
from src.consts import font

def build():
    """
    Construye la ventana principal
    """
    #El tema hay que ponerlo siempre primero sino no funciona
    sg.theme('SystemDefault')

    font16 = ("Calibri Italic", 16)

    layout = [
        [sg.Text("Expedientes del dia", font=(font.font_name,20))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expediente", key="-INGRESAR_EXPEDIENTE-", font=(font.font_name,11))],
        [sg.Table(values=[["-","-","-","-","-","-"]], key="-TABLA_EXPEDIENTES-",justification="c",
            headings=[" Codigo ", "    Empresa    ", "   CUIT  ", " Telefono ", " Categoria "],
            row_height=20, num_rows=10,header_background_color="#FF8000"
        )],
        [
            sg.Text('Total', font=font16),
            sg.Text('0,00', background_color="#000000", text_color="#ffffff", font=font16,size=(10,1),
                    justification="rigth", key="-TEXTO_TOTAL-")
        ]
    ]

    window = sg.Window("Sistema integral v1.0", layout=layout, resizable=True)
    return window