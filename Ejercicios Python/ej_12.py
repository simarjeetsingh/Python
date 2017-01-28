''' Escribe un programa que pida por teclado dos números y que calcule y muestre su suma
    solamente si:
    a. los dos son pares
    b. el primero es menor que cincuenta
    c. y el segundo está dentro del intervalo cerrado 100-500.
    En el caso de que no se cumplan las condiciones, en vez de la suma ha de visualizarse un
    mensaje de error.'''
    
numero_1 = int(input("Introduzca el primer número: "))
numero_2 = int(input("Introduzca el segundo número: "))


if (numero_1%2 == 0) and (numero_2%2 == 0):
    if numero_1 < 50:
        if (numero_2 >=100) and (numero_2 <= 500):
            print ("La suma de los dos números es: ", numero_1 + numero_2)
        else:
            print ("Error.")
    else:
        print ("Error")
else:
    print ("Error.")



