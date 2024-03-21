# -*- coding: cp1252 -*-

def generador_primos(ini,fin):
        """ Utiliza una funcion interna para comprobar si n es primo"""
        def esPrimo(n):
                if n <= 0:
                        return False
                
                for i in range(2,n):
                        if n % i == 0:
                                return False
                return True

        n = ini
        while(n <= fin):
                if esPrimo(n):
                        yield n
                n += 1


# Utilizar el generador para iterar por los número primos:
for n in generador_primos(0, 50):
        print (n,end=" ")
print()        


