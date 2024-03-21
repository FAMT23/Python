# List compresion

# Potencias de 2:
L = [2**i for i in range(0,20)]
print ("POTENCIAS DE DOS")
print (L)

# Numeros pares del 0 al 100
L2 = [i for i in range(0,100) if i % 2 == 0]
print ("\nPARES DEL 0 AL 100")
print (L2)

# los numeros que no estan en la lista anterior:
L3 = [i for i in range(0,100) if i not in L2]
print ("\nLOS QUE NO ESTAN  EN LA ANTERIOR")
print (L3)

# tablas de multiplicar:
tablas = [(i,j,i*j) for i in range(1,11) for j in range(1,11)]
print ("\nTABLAS:")
print (tablas)


# Numeros primos
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print ("\nPRIMOS:")
print (primes)
