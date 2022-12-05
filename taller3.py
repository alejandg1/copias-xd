import json


def publicaciones():
    profesores= []

    publicaciones= open('datos/publicacion.json','r')
    datos = json.load(publicaciones)

    for i in datos:
        cedula= i['cedula']
        nombre= i['apellidos']
        if not(profesores.__contains__(i['cedula'])):
            
            profesores.append({'cedula': cedula,'nombre': nombre})
    newprofesor= []
    for i in profesores:
        cedula= i['cedula']
        
        publicaciones = 0
        for k in datos:
            if cedula == k['cedula']:
                publicaciones= +1
        newprofesor.append({'cedula':cedula,'nombre':i['nombre'], 'publicaciones': publicaciones})
    for i in newprofesor:
        print(f"el docente {i['nombre']} con C.I: {i['cedula']} tiene: {i['publicaciones']} publicacion()")






if __name__== "__main__":
    publicaciones()
