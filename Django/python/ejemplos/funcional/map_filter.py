from functools import reduce

# map
def sustituir(x):
        return ord(x)


# filter
def esPalindromo(s):
        i=0;j=-1
        while i<len(s):                
                if s[i] != s[j]:
                        return False
                i+=1; j-=1
        return True
        

# reduce
def reducir(a,b):
        return chr(a%255)+chr(b%255)


print ("\nmap:")
cadena = "hola que tal"
L2 = list(map(sustituir,list(cadena)))
print ("Cadena: " + cadena)
print ("L: ", L2 )


print ("\nfilter:")
L = ["hola","ana","oso","abbccdccbba","abcdeba"]
L2 = list(filter(esPalindromo, L))
print (L)
print (L2)


a = 12
b = 56

s=chr(a)+chr(b)
print ("\ns: "+s)

print ("\nreduce:")
L=[65,56,74,93,96,88,99]
#s = reduce(reducir, L)
#print (s)
