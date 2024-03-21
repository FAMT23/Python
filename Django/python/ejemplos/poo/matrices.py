# -*- coding: cp1252 -*-

import random

class Matriz:

    def __init__(self, filas=10,cols=10):
        # Crear n filas
        self.__datos = [None]*filas

        # Por cada fila crear las columnas rellenas de ceros
        for i in range(0,filas):
            self.__datos[i] = [0]*cols


    def __str__(self):
        s = ""
        for fila in self.__datos:            
            for columna in fila:
                s += str(columna) + " "
            s+="\n"

        return s

    def dimensiones(self):
        return len(self.__datos), len(self.__datos[0])

    def setVal(self,i,j,valor):
        self.__datos[i][j] = valor

    def getVal(self,i,j):
        return self.__datos[i][j]

    def __add__(self,m):
        dim = self.dimensiones()
        
        if dim == m.dimensiones():
            r = Matriz(dim[0],dim[1])

            for i in range(dim[0]):
                for j in range(dim[1]):
                    suma = self.getVal(i,j)+m.getVal(i,j)
                    r.setVal(i,j,suma)
            return r

        else:
            return None

    def __mul__(self,m):
        # Comprobar dimensiones, cols de m1 == filas de m2
        dim1 = self.dimensiones()
        dim2 = self.dimensiones()

        if dim1[1] == dim2[0]:
            r = Matriz(dim1[1],dim2[0])

            for i in range(dim1[1]):
                for j in range(dim2[0]):

                    val = 0                   
                    for k in range(dim1[1]):                       
                        val += self.getVal(i,k) * m.getVal(k,j)
                  
                    r.setVal(i,j,val)
                    
            return r
                    
        else:
            return None
        

m1 = Matriz(3,3)
m2 = Matriz(3,3)


# Generar las matrices con número aleatorios:
for i in range(3):
    for j in range(3):
        m1.setVal(i,j,random.randint(0,5))
        m2.setVal(i,j,random.randint(0,5))
print (m1)
print()
print (m2)
print ("\nSUMA:")
m3 = m1 + m2
print (m3)
print()
m3 = m1 * m2
print ("\nMULTIPLICACION: ")
print (m3)

