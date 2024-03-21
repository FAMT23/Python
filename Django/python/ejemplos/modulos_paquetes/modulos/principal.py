#-*- coding: cp1252 -*-

import fecha, hora, fechahora

# pruebas con la clase Time

h1 = hora.Time(8,39)
h2 = hora.Time(5,23,7)

# 8:39:45 + 5:23:07 = 14:02:52

print ('h1 ' + str(h1) + ' h2 ' + str(h2))
print ('segundos de h1: ' + str(h1.ss))
suma = h1 + h2 
print ('suma: ' + str(suma))
print ('suma en sg: ' + str(suma.toSegundos()))
suma.hh = 20
print ('suma: ' + str(suma))

# pruebas con la clase Date:
d1 = fecha.Date(8,5,2020)
if d1.esBisiesto():
    print (str(d1.yy) + " es un año bisiesto")
print (d1)

#pruebas con la clase DateTime:
dt = fechahora.DateTime(31,5,2015,6,8,34)
print (str(dt))


