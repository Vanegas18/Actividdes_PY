import math


print("EJERCICIO 10")

"""
A ciertos estudiantes se les dice que su calificación final será el promedio
de las dos calificaciones más altas de entre las tres que se han obtenido en
el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
correspondiente a su nota final.

"""

nota1 = float(input("Ingrese su nota #1: "))
nota2 = float(input("Ingrese su nota #2: "))
nota3 = float(input("Ingrese su nota #3: "))

if nota1 <= nota2 and nota1 <= nota3:
  sumaNotas = nota2 + nota3
elif nota2 <= nota1 and nota2 <= nota3:
  sumaNotas = nota1 + nota3
else: 
  sumaNotas = nota1 + nota2

promedio = sumaNotas / 2
print(f"SU CALIFICACIÓN FINAL ES: {promedio}")

print("EJERCICIO 11")

"""
Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
para una empresa de acuerdo a los siguientes criterios:
  a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
  b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
  c. Por ningún motivo su masa debe exceder los 5.8 cm
  i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5Gr/cm

"""

# longitud = float(input("Ingrese la longitud de la varilla: "))
# diametro = float(input("Ingrese el diámetro de la varilla: "))
# densidad = 3.5
# masa = diametro * longitud / densidad

# if (longitud > 7.5 and longitud <= 9) and (diametro >= 0.5 and diametro <= 1.3) and (masa <= 5.8):
#   print("ACEPTADA")
# else:
#   print("RECHAZADA")

# print(f"LONGITUD = {longitud} - DIAMETRO = {diametro} - MASA = {masa}")

print("EJERCICIO 12")

"""
Un vendedor desea calcular su comisión total sobre las ventas de varios
artículos. Al vendedor le corresponde el 3% de comisión sobre artículos
cuyo precio es menor de $2.000.oo y el 5% de comisión sobre artículos
cuyo precio es de $2000.oo o más. El vendedor hizo 50 ventas y desea
saber también cuántas ventas hizo menores de 2000 y cuantas mayores o
iguales a 2000.

"""

# menorDOSMIL = 0
# mayorDOSMIL = 0

# for i in range(10):
#   precio = float(input(f"Ingrese el precio del producto #{i+1}: "))

#   if precio < 2000:
#     menorDOSMIL += 1
#   else:
#     mayorDOSMIL += 1

# print(f"Los productos mayores a 2000 son: {mayorDOSMIL} y los menores a 2000 son: {menorDOSMIL}") 

print("EJERCICIO 13")

"""
Desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
determine si la gano o la reprobó

"""

# nota1 = float(input("Ingrese su nota 1: "))
# nota2 = float(input("Ingrese su nota 2: "))
# nota3 = float(input("Ingrese su nota 3: "))
# sumaNotas = nota1 + nota2 + nota3
# promedio = sumaNotas / 3


# if promedio < 3.0:
#   print(f"Desaprobó con una nota de: {promedio}")
# else: 
#   print(f"Aprobó con una nota de: {promedio}")

print("EJERCICIO 14")

"""
Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.

"""

# numero = int(input("Ingrese un numero: "))

# if numero != 0:
#   resultado = 1 / numero
#   print(f"El resultado de 1/{numero} es: {resultado}")
# else:
#   print("No se puede dividir entre cero")


print("EJERCICIO 15")

"""
Desarrollar el algoritmo que evalué la formula cuadrática o general.

"""

# a = float(input("Ingrese el numero a: "))
# b = float(input("Ingrese el numero b: "))
# c = float(input("Ingrese el numero c: "))

# discriminante = b**2 - 4*a*c

# if discriminante >= 0:
#   raiz1 = (-b+ math.sqrt(discriminante)) / (2*a)
#   raiz2 = (-b- math.sqrt(discriminante)) / (2*a)
#   print(f"Las raíces son: {raiz1} y {raiz2}")
# else:
#   print("No tiene raíces reales")

print("EJERCICIO 16")

"""
Desarrollar un algoritmo que capture un número y diga si es par o impar.

"""

# numeroAEvaluar = int(input("Ingrese el numero: "))

# if numeroAEvaluar % 2 == 0:
#   print("El numero es par!")
# else:
#   print("El numero es impar!")

print("EJERCICIO 17")

"""
Desarrollar el algoritmo que lea tres números y diga si uno es divisible del
otro.

"""

# a = int(input("Ingrese el numero 1: "))
# b = int(input("Ingrese el numero 2: "))
# c = int(input("Ingrese el numero 3: "))

# if a % b == 0 or a % c == 0 or b % c == 0:
#   print("Un numero es divisible por otro")
# else: 
#   print("Ningún numero es divisible por otro")


print("EJERCICIO 18")

"""
Desarrollar un algoritmo que capture un número y diga si negativo o
positivo.

"""

# numero = int(input("Ingrese el numero a evaluar: "))

# if numero < 0:
#   print("El numero es NEGATIVO!")
# else: 
#   print("El numero es POSITIVO!")
  
  