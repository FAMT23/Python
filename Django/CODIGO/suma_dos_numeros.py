"""
Leer dos numeros de teclado y sumarlos
"""

# Lee de un número como texto y lo convierte a entero
numero1 = int(input('Teclear numero entero:'))
numero2 = int(input("Teclear otro numero entero: "))
print(numero1 + numero2)

# Lee de un número como texto y lo convierte a float
numero1 = float(input('Teclear numero:'))
numero2 = float(input("Teclear otro numero: "))
print('El resultado de la suma es: ',numero1 + numero2,' numero entero')

# Con las f-string: lo mismo se escribe:
print(f'El resultado de la suma de {numero1} + {numero2} = {numero1+numero2}')

