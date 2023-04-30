import PySimpleGUI as sg
from src.consts.font import font_name, font_size

def build():
    sg.theme('SystemDefault')

    categorias = ["tipo1","tipo2","tipo3"]

    layout =[
        [sg.Text('Ingresar expediente',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text("Codigo",size=(15,1)), sg.Spin(list(range(99999)),size=(10,1),key="-CODIGO-")],
        [sg.Text("Empresa",size=(15,1)), sg.Input(size=(30,1),key="-EMPRESA-")],
        [sg.Text("CUIT",size=(15,1)), sg.Input(size=(30,1),key="-CUIT-")],
        [sg.Text("Telefono",size=(15,1)), sg.Input(size=(30,1),key="-TELEFONO-")],
        [sg.Text("Categoria",size=(15,1)),sg.Combo(categorias,default_value=categorias[0], key="-CATEGORIA-",readonly=True)],
        [sg.Button("Guardar",size=(10,1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Ingresar expediente', layout=layout, font=(font_name,font_size), modal=True)
    return window