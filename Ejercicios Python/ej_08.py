''' Escribe un programa que pida por teclado dos números y que muestre en pantalla uno de
    los dos mensajes siguientes en función de los números leídos: a) el primer número
    (valor) es mayor que el segundo (valor) (introduciendo el valor de los números en el
    mensaje); b) el primer número (valor) es menor que el segundo (valor ; c) los
    dos números son iguales (valor)'''
    
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

if numero_1 > numero_2:
    print ("El primer número",'(',numero_1,')', "es mayor que el segundo",'(',numero_2,').')
elif numero_1 < numero_2:
    print ("El primero número",'(',numero_1,')',"es menor que el segundo", '(',numero_2,').')
else: 
    print ("Los dos números son iguales.")



