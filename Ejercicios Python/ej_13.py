''' Diseña un programa que calcule el importe final de una venta considerando que sobre el
valor bruto se hace un descuento según la siguiente tabla:
a. Valores <=20 implican un descuento del 0%
b. Valores >20 y <=100 implican un descuento descuento del 5%
c. Valores >100 implican un descuento 10%.'''
    
valor = int(input("Introduzca el valor bruto: "))

if (valor <= 20):
    print ("El importe final es: ", valor)
elif valor > 20 and valor <=100:
    print ("El importe final es: ", valor*0.95)
else:
    print ("El importe final es: ", valor*0.9)



