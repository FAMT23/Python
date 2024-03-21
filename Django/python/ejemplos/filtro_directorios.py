"""
Extraer la extensión de un fichero y utilizarlo para filtrar ficheros
de un directorio.
"""
import os

# Filtrar ficheros por extensión
L = os.listdir()
extensiones = ('txt','ipynb')
for i in L:
    if i.partition('.')[2] in extensiones:
        print(i)

# Obtener las distintas extensiones de los ficheros de una carpeta:
c = set()
for i in L:
    c.add(i.partition('.')[2])
print('Extensiones de los ficheros: ', c)

# Clasificar ficheros por ext. por una lado los: py, los pdf, los xlsx, etc.
directorio = dict()
for i in L:
    ext = i.partition('.')[2]
    if ext in directorio:
        # La lista ya existe. Se añade otro fichero de la misma extensión
        directorio[ext] += [i]
    else:
        # Creamos la lista con el primer fichero
        directorio[ext] = [i]

print('Directorio:')
for ext, L in directorio.items():
    print(ext)
    for i in L:
        print('\t',i)




