import json

def agregar_expedientes(datos_nuevos):
    """
    Guarda los datos de un nuevo expediente en el archivo de expedientes.json
    """
    with open('Modulo-4/files/expedientes.json','r') as archivo:
        lista_expedientes = json.load(archivo) #carga tos los expedientes
    if not lista_expedientes:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_expedientes, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_expedientes.append(datos_nuevos)
    with open('Modulo-4/files/expedientes.json','w') as archivo:
        json.dump(lista_expedientes,archivo,indent=4)

def leer_archivo():
    """
    Lee todos los datos de expedientes.json y los deveuleve como una lista de diccionarios
    """
    with open('Modulo-4/files/expedientes.json','r') as file:
        datos = json.load(file) #para leerlo como diccionario
        #convierte los datos a una lista de listas para que se pueda mostrar en la tabla
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-CODIGO-"], dato["-EMPRESA-"],dato["-CUIT-"], dato["-TELEFONO-"],dato["-CATEGORIA-"]])
    return datos_para_tabla