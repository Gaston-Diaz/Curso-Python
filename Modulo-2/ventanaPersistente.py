import PySimpleGUI as sg

layout = [
    [sg.Text('Ingresar Primer Valor'), sg.InputText()],
    [sg.Text('Ingresa Segundo Valor'), sg.InputText()],
    [sg.Button('OK'), sg.Button('Cancelar')]
]

window = sg.Window("Ventana Persistente",layout, margins=(200,150))

while True:
    event, values = window.read()

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break

    print('Datos ingresado', values)
window.close()