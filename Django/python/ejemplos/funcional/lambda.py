# funciones lambda:

f = lambda x: x**2
print (f(3))

f2 = lambda x,y,z: x+y+z
print (f2(1,2,3))

def incrementador(n):
        return lambda x: x+n


f = incrementador(10)
print ("f(3): " + str(f(3)))



