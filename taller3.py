import json
import time
directorio = open('datos/directorio.json','r')
datos = json.load(directorio)

def direct():

    exten=[]
    docente=[]
    cargos =[]
    departamentos = []
    for persona in datos:
        if not(exten.__contains__(persona['extension'])):
            exten.append(persona['extension'])
            docente.append({'nombre':persona['nombres'],'apellidos':persona['apellidos'],'cargo':persona['cargo'],'departamento':persona['departamento']})
        if not(cargos.__contains__(persona['cargo'])):
            cargos.append(persona['cargo'])
        if not(departamentos.__contains__(persona['departamento'])):
            departamentos.append(persona['departamento'])
    print(f"el total de cargos en la base de datos es de: {len(cargos)}")
    print(f"el total de departamentos es de: {len(departamentos)}")
    time.sleep(3)
    for i in docente:
        print("_________________________________________________________")
        print(f"nombres:  {i['nombre']}")
        print(" ")
        print(f"apellidos: {i['apellidos']}")
        print(" ")
        print(f"cargo: {i['cargo']}")
        print(" ")
        print(f"departamento: {i['departamento']}")

if __name__ == "__main__": 
    direct()
