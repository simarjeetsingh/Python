''' Escribe un programa que nos pida por teclado dos números enteros y que a continuación
    muestre en pantalla la suma de los dos números solamente si son los dos positivos. Si no
    se cumple que los dos números sean positivos se visualizará un mensaje indicándolo. La
    salida ha de tener el siguiente formato: “La suma de los dos números es: XXX” o “No se
    calcula la suma porque alguno de los números o los dos no son positivos”.'''
    
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

if numero_1 >= 0 and  numero_2 >= 0:
    print ('La suma es:', numero_1 + numero_2,)

else: 
    print ("No se calcula la suma porque alguno de los números o los dos no son positivos.")



