def profundidad(L):
        for i in L:
                if isList(i):
                        profundidad(i)
                else:
                        print (i)
        

def isList(L):
        #if 'list' in str(type(L)):
        if type(L)==list:
                return True
        else:
                return False

def desanidar(L,LR):
        for i in L:
                if isList(i):
                        desanidar(i,LR)
                else:
                        LR.append(i)

#codigo 1:
L = [1,2,['a','b',[23,25,[100,345],34],['c','d']]]
print (L)

print ("\nResultado:")
profundidad(L)

#codigo 2:
L = [1,2,['a','b',[23,25,[100,345],34],['c','d']]]
print (L)

print ("\nResultado:")
LR = []
desanidar(L,LR)
print (LR)
        



        
