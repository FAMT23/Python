# -*- coding: Cp1252 -*-
# ejemplos de objetos:

import time

class Time(object):

    def __init__(self,hh=0,mm=0,ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    # Getters, Setters.
    def getHH(self):
        return self.__hh

    def setHH(self,hh):
        self.__hh = hh

    def getMM(self):
        return self.__mm

    def setMM(self,mm):
        self.__mm = mm

    def getSS(self):
        return self.__ss

    def setSS(self,ss):
        self.__ss = ss


    # definición de propiedades:
    hh = property(getHH, setHH)
    mm = property(getMM, setMM)
    ss = property(getSS, setSS)

    def __cmp__(self, hora):       
        ss1 = self.toSegundos()
        ss2 = hora.toSegundos()
        
        if ss1 == ss2:
            return 0
        elif ss1 < ss2:
            return -1
        else:
            return 1       

    def __eq__(self, hora):
        print ("salta eq")
        return (self.__hh == hora.__hh) and (self.__mm == hora.__mm) and (self.__ss == hora.__ss)
    
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


class Date(object):

    def __init__(self, dd,mm,yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd,self.__mm,self.__yy)

    def esBisiesto(self):
        anyo = self.__yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

    def getYY(self):
        return self.__yy

    def setYY(self,yy):
        self.__yy = yy

    yy = property(getYY,setYY)

class DateTime(Date,Time):

    def __init__(self,dd=0,MM=0,yy=0,hh=0,mm=0,ss=0):
        Date.__init__(self,dd,MM,yy)
        Time.__init__(self,hh,mm,ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)

# pruebas con la clase Time

h1 = Time(8,39)
h2 = Time(5,23,7)

# Prueba operador eq
if h1 == h2:
    print ("h1 == h2")
else:
    print ("h1 != h2")


print ("__cmp__ con h1 y h2: ", h1.__cmp__(h2))
print ("__cmp__ con h2 y h1: ", h1.__cmp__(h2))
print ("__cmp__ con h1 y h1: ", h1.__cmp__(h2))

# 8:39:45 + 5:23:07 = 14:02:52

print ('h1 ' + str(h1) + ' h2 ' + str(h2))
print ('segundos de h1: ' + str(h1.ss))
suma = h1 + h2 
print ('suma: ' + str(suma))
print ('suma en sg: ' + str(suma.toSegundos()))
suma.hh = 20
print ('suma: ' + str(suma))

# pruebas con la clase Date:
d1 = Date(8,5,2020)
if d1.esBisiesto():
    print (str(d1.yy) + " es un año bisiesto")
print (d1)

#pruebas con la clase DateTime:
dt = DateTime(31,5,2015,6,8,34)
print (str(dt))


