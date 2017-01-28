'''Escribe un programa que pida por teclado dos valores de tipo numérico que se han de
   guardar en sendas variables. ¿Qué instrucciones habría que utilizar para intercambiar su
   contenido? (es necesario utilizar una variable auxiliar). Para comprobar que el algoritmo
   ideado es correcto, muestra en pantalla el contenido de las variables una vez leídas, y
  vuelve a mostrar su contenido una vez hayas intercambiado sus valores.'''
    
variableA = int(input("Introduzca un número: "))
variableB = int(input("Introduzca otro número: "))
print("Los números introducidos son: ", variableA ,'y',variableB)

variableAux = variableA
variableA = variableB
variableB = variableAux

print ("Los números intercambiados son: ", variableA, 'y', variableB)


