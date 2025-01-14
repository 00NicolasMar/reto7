# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RS8egExFAoCNwyI5uC7f4ZIqLF7qDym1

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
"""

for n in range (1,101): #establecemos un rango sobre el cual va a funcionar el codigo
  print(n, "=", n**2) #establecemos una impresion en donde se vea el numero y su cuadrado

"""Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

"""

print("listado numeros impares") #esta imprecion sirve para identificar el listado
for n in range (1, 1000, 2):  #para cada numero en el rango 1 a 1000 imprimirlos en salto de 2, lo cual nos daria como resultados los numeros impares
  print(n)
print("listado numeros pares") #esta impresion funciona para identificar listado y separar uno del otro
for n in range (2, 1001, 2): #para cada numero en el rango 2 a 1001 imprimirlos en salto de 2, lo cual nos daria los numeros pares
  print(n)

"""Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado"""

n = int(input("ingrese un numero natural mayor que 2: ")) #aqui se da el ingreso al numero natural mayor que 2
if n % 2 != 0: #es el condicional que nos presenta el caso en el cual el numero dado es natural par
  n-=1
for n in range (n, 1, -2): #se nos da un rango apartir del cual trabajara siendo hasta 1, con saltos de menos 2 numeros
  print(n) #se imprimen todos los n

"""Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial"""

n = int(input("Ingrese un número natural: ")) # se da el ingreso del numero natural
fact = 1 # se establece su comienzo desde 1, de tal manera a partir de este empieza a multiplicar el siguiente entero
for i in range(1,n+1): # el rango de operacion siendo hasta 1 mas que el valor ingresado en la primera linea
  fact = fact * i # es la operacion factorial a realizar
  print(i, fact) # se imprime el resultado

"""Calcular el valor de 2 elevado a la potencia n usando ciclos for."""

n = int(input("ingrese un numero como potencia: ")) #se ingresa el numero que sera la potencia a la cual sera elevado el numero
x = 2 #se establece que 2 es el numero el cual se elevara
for i in range (1,n): #es el ciclo en el cual se realizara la potencia
  x = x * 2 #es la operacion a realizar
print(x) #imprime el resultado

"""Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**)."""

n = int(input("ingrese un numero natural: ")) #se ingresa la potencia
x = float(input("ingrese un numero real: ")) #se ingresa el numero a elevar
p = x #se establece que x es el valor que va a ser elevado a la potencia n
for i in range (1,n): # el ciclo que nos da pie a la operacion de potencia que se va a realizar
  p = p * x
print("La potencia de " + str(x) + "^" + str(n) + " es: " + str(p)) #nos da la imprecion del resultado de manera detallada

"""Diseñe un programa que muestre las tablas de multiplicar del 1 al 9."""

for i in range(1,10): # aqui se establecen los multiplicandos que son hasta 9
  print("la tabla del " + str(i) + " " + "es: ") # es por asi decirlo comop el titulo de cada tabla de multiplicar
  for n in range(1,11): # estos son los muoltiplicadores de la operacion que van de 1 a 10
    x = n * i # establece la operacion a realizar
    print(i, "x", n, "=", x) # imprime la tabla de multiplicar

"""Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
e
x
≈
e
x
p
(
x
,
n
)
≈
∑
i
=
0
n
x
i
i
!
"""

import math

def factorial(n): #definimos la funcion factorial que utilizaremos
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def aproximacion_exponencial(x, n):
    suma = 0 # definimos este dato como nuestro valor de inicio indicando que suma
    for i in range(n + 1):
        num = (x**i) / factorial(i) #esta es la formula representada como una variable
        suma += num
    return suma

if __name__ == "__main__":
    x = float(input("Ingrese un número real: ")) #se ingresa el numero
    n = int(input("ingrese una cantidad de términos a utilizar: ")) #se ingresan los terminos

    c = aproximacion_exponencial(x, n)
    v = math.exp(x)
#se imprimen los resultados
    print("resultado: " + str(c))
    print("resultado verdadero: " + str(v))
    print("se desvia " + str(abs(c - v)) + " del resultado verdadero.")

"""Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
s
i
n
(
x
)
≈
s
i
n
(
x
,
n
)
≈
∑
i
=
0
n
(
−
1
)
i
x
2
i
+
1
(
2
i
+
1
)
!
"""

import math

def factorial (n): #definimos el factorial que vamos a utilizar después.
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return fact

def sin(x,n):
  suma = 0 # definimos este dato como nuestro valor de inicio indicando que suma
  for i in range(n+1):
    num = ((-1)**i)*((x**(2*i+1))/factorial(2*i+1)) #esta es la formula representada como una variable
    suma += num
  return suma

if __name__ == "__main__":
  x = float(input("Ingrese un número real: ")) #se ingresa el numero
  n = int(input(" Ingrese una cantidad de términos a utilizar: ")) #se ingresan los terminos
  c = sin(x,n)
  v = math.sin(x)
#se imprimen los resultados
print("resultado: " + str(c))
print( "resultado verdadero: " + str(v))
print("el resultado se desvia " + str(abs(c - v)) + " del resultado verdadero.")