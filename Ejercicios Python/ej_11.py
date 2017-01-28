''' Escribe un programa que pida por teclado tres valores de tipo entero, y que calcule si se
    cumple que la suma de dos de ellos es igual al tercero. La salida del programa tiene que
    tener el formato:
    Números introducidos: N1N2 N3 (tabulador)
    Y una de las cuatro líneas de salida siguientes:
    Se cumple que N1 = N2 + N3
    Se cumple que N2 = N1 + N3
    Se cumple que N3 = N1 + N2
    Los números no cumplen la condición'''
    
numero_1 = int(input("Introduzca el primer número: "))
numero_2 = int(input("Introduzca el segundo número: "))
numero_3 = int(input("Introduzca el tercer número: "))

print ("Números introducidos: ", numero_1, "\t", numero_2, "\t", numero_3)

if numero_1 == (numero_2 + numero_3):
	print ("Se cumple que N1 = N2 + N3")
elif numero_2 == (numero_1 + numero_3):
	print ("Se cumple que N2 = N1 + N3")
elif numero_3 == (numero_1 + numero_2):
	print ("Se cumple que N3 = N1 + N2")
else:
	print ("Los números no cumplen la condición.")



