# ordenar por la longitud de los elementos de la lista

def order(a):
	return len(a)
	
	
L = ['zzz','a','x','23xxx','aaaaavfg']
print(L)
L.sort()
print(L)

L.sort(key=order,reverse=True)
print(L)
