x = 60
y = 0
try: 
        z = x / y
except ZeroDivisionError: 
        print ("Division por cero")
finally: 
        print ("Limpiando")
