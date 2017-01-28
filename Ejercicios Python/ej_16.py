''' Escribeun programa que escriba en pantalla los 30 primeros números naturales (del 1 al
30), así como su media aritmética.'''

suma = 0

for num in range(1, 31):
    print (num)
    suma = suma + num

print ("La media aritmética es: ", suma/30)


