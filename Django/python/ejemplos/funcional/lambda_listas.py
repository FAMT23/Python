# Ejemplos de funciones lambda para crear los operadores:
# car devuelve la cabeza de la lista, el primer elemento
# cdr devuelve el resto de la lista, todos menos el primero

car = lambda L: L[0]
cdr = lambda L: L[1:]
empty = lambda L: len(L)==0


def invertir(L):
        if not empty(L):                
                invertir(cdr(L))
                print (car(L))

def desanidar(L):
        if empty(L):
                return []
        elif type(car(L))==list:
                return desanidar(car(L)) + desanidar(cdr(L))
        else:
                return [car(L)] + desanidar(cdr(L))
        
                


# prueba de los operadores:
L = [1,2,3,4,5]

print ("car L: ")
print (car(L))

print ("cdr L: ")
print (cdr(L))

L=[]
print ("empty L: ")
print (empty(L))

print ("Invertir: ")
L=[1,2,3,4,5]
invertir(L)


print ("\nDesanidar: ")
L=[1,2,[3,4,[5,6],8],9,10]
print (L)
print (desanidar(L))



