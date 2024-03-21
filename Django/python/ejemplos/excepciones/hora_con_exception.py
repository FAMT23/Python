# -*- coding: cp1252 -*-
# ejemplos de objetos:

import time

class TimeException(Exception):

    def __init__(self,mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

class Time(object):

    def __init__(self,hh=0,mm=0,ss=0):
        if hh < 0 or hh > 23:
            raise TimeException("Error en las horas: " + str(hh))

        if mm < 0 or mm > 59:
            raise TimeException("Error en los minutos: " + str(mm))

        if ss < 0 or ss > 59:
            raise TimeException("Error en los segundos: " + str(ss))
        
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    # Getters, Setters.
    def getHH(self):
        return self.__hh

    def setHH(self,hh):
        if hh < 0 or hh > 23:
            raise TimeException("Error en las horas: " + str(hh)) 
        self.__hh = hh

    def getMM(self):
        return self.__mm

    def setMM(self,mm):
        if mm < 0 or mm > 59:
            raise TimeException("Error en los minutos: " + str(mm))
        self.__mm = mm

    def getSS(self):
        return self.__ss

    def setSS(self,ss):
        if ss < 0 or ss > 59:
            raise TimeException("Error en los segundos: " + str(ss))
        self.__ss = ss


    # definición de propiedades:
    hh = property(getHH, setHH)
    mm = property(getMM, setMM)
    ss = property(getSS, setSS)
    
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.__hh,self.__mm,self.__ss)


    def __add__(self,hora2):
        segundos = self.__ss + hora2.__ss
        minutos = self.__mm + hora2.__mm
        horas = self.__hh + hora2.__hh

        if segundos > 59:
            segundos -= 60
            minutos += 1

        if minutos > 59:
            minutos -= 60
            horas += 1

        horas %= 24
        return Time(horas,minutos,segundos)

    def toSegundos(self):
        return self.__hh * 3600 + self.__mm * 60 + self.__ss



# pruebas con la clase Time

try:
    h1 = Time(8,39)
    print (h1)
    
    h2 = Time(5,23,7)
    print (h2)

    h1.ss = 100
    
except TimeException as e:
    print (e)
except:
    print ('otro error')



