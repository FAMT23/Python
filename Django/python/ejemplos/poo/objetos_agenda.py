#-*- coding: utf-8 -*-
# Agenda de teléfonos:
# mantener el nombre y el teléfono de cada contacto:
# añadir contacto, listar contactos, buscar un contacto, borrar contacto.

class Contacto(object):

    def __init__(self,nombre,telefono):
        self.__nombre = nombre
        self.__telefono = telefono

    def __str__(self):
        return self.__nombre + " -> " + str(self.__telefono)

    def getNombre(self):
        return self.__nombre

    def getTelefono(self):
        return self.__telefono


class Agenda(object):

    def __init__(self):
        self.__listin = []

    def addContacto(self,contacto):
        self.__listin.append(contacto)

    def listContactos(self):
        print ('Listado de contactos:')
        for contacto in self.__listin:
            print (str(contacto))

    def buscarContacto(self, nombre):
        for contacto in self.__listin:
            if nombre == contacto.getNombre():
                return contacto.getTelefono()
            
        return "No existe"


miAgenda = Agenda()
miAgenda.addContacto( Contacto('Ana',606067788))
miAgenda.addContacto( Contacto('Juan',647060797))
miAgenda.listContactos()

print (miAgenda.buscarContacto('Miguel'))
print (miAgenda.buscarContacto('Juan'))

