import re,io,sys

# Listar los metodos y atributos de un modulo:

L = dir(re)
for i in L:
        print( i)

L = dir(io)
for i in L:
        print (i)

L = dir(sys)
for i in L:
        print (i)


