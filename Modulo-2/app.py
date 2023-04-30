#importamos
import PySimpleGUI as sg

#Definimos el contenido de la ventana
layout = [ 
    [sg.Text("Hola soy una ventana")],
    [sg.Input()],
    [sg.Button('ok')]
]

#creamos la ventana
window = sg.Window("Titulo de la ventana", layout) #definimos la ventana

#dibujamos la ventana y leemos los eventos
event, values = window.read()

#hacemos algo con la inoformacion obtenida
print('Hola', values[0],"Esto funciona?")

#cerramos la ventana
window.close()