''' Modifica el programa anterior para que en vez de mostrar un mensaje genérico en el caso
    de que alguno o los dos números sean negativos, escriba una salida diferenciada para cada
    una de las situaciones que se puedan producir, utilizando los siguientes mensajes:
    a. No se calcula la suma porque el primer número es negativo .
    b. No se calcula la suma porque el segundo número es negativo .
    c. No se calcula la suma porque los dos números son negativos .'''
    
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

if (numero_1 >= 0) and  (numero_2 >= 0):
    print ('La suma es:', numero_1 + numero_2,)
elif (numero_1 < 0) and (numero_2 > 0):
    print ("No se calcula la suma porque el primer número es negativo.")
elif (numero_1 > 0) and (numero_2 < 0):
    print ("No se calcula la suma porque el segundo número es negativo.")
else:
    print ("No se calcula la suma porque los dos números son negativos.")



