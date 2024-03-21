#-*- coding: utf-8 -*-

# Unión, intersección, mezcla de listas:

def union(L1, L2):
        LU = []

        for i in L1:
                if i not in LU:
                        LU.append(i)
        for j in L2:
                if j not in LU:
                        LU.append(j)
        LU.sort()
        return LU

def interseccion(L1, L2):
        LI = []
        for i in L1:
                if i in L2 and i not in LI:
                        LI.append(i)

        LI.sort()                
        return LI

def unionALL(L1,L2):
        L = L1+L2
        L.sort()
        return L
        

# código principal:
L1 = [1,3,4,6,7,8,9]
L2 = [1,3,4,5,7,7,7,9,10]

print ("L1 ",L1)
print ("L2 ", L2)

LU = union(L1,L2)
print ("Union: ",LU)

LI = interseccion(L1,L2)
print ("Interseccion: ",LI)

LM = unionALL(L1,L2)
print ("Union ALL: ", LM)
