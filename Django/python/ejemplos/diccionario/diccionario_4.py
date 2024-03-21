# ocurrencias de una lista.

L = [1,5,4,3,2,1,5,6,7,5,4,3,2,2,1]

dic = {}
for i in L:
        if i not in dic:
                dic[i] = 1;
        else:
                dic[i]+=1

print ("L: ",L)
print ("Dic: ",dic)
        
