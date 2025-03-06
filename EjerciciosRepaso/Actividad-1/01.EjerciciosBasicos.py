import math

print("EJERCICIO 1 ")
"""
Se desea calcular la distancia recorrida (D) por un automóvil que tiene velocidad constante
(m/s) durante un tiempo T (Sg), considerar que es un MRU (Movimiento Rectilíneo
Uniforme). Tenga en cuenta que la formula del movimiento rectilíneo es:

D = V * T

"""

# velocidad = int(input("Digite la velocidad en la que anduvo:" ))
# tiempo = int(input("En que tiempo recorrió esa distancia: "))
# distanciaRecorrida = velocidad * tiempo

# print(f"La distancia recorrida es de: {distanciaRecorrida} m/s")



print("EJERCICIO 2 ")
"""
Se necesita obtener el promedio de un estudiante a partir de sus tres notas parciales. El
estudiante debe digitar sus tres notas y el sistema deberá darle el promedio del semestre.

"""

# nota1 = float(input("Digite su nota #1: "))
# nota2 = float(input("Digite su nota #2: "))
# nota3 = float(input("Digite su nota #3: "))
# sumaNotas = nota1 + nota2 + nota3
# promedio = sumaNotas / 3

# print(f"El promedio de sus notas: [{nota1}, {nota2}, {nota3}] es: {promedio}")


print("EJERCICIO 3 ")
"""
Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y
empatados, de un equipo en un torneo de futbol. Se debe de imprimir el puntaje total del
equipo, tenga en cuenta que:
  a. Por cada partido ganado obtendrá 3 puntos.
  b. Por cada partido empatado 1 punto.
  c. Por cada partido perdido 0 puntos.
Se desea imprimir la cantidad de partidos ganados, perdidos, empatados y el cálculo
completo de la cantidad de puntos obtenidos del equipo de futbol.

"""

# partidosGanados = int(input("Cuantos partidos gano? "))
# partidosEmpatados = int(input("Cuantos partidos empato? "))
# partidosPerdidos = int(input("Cuantos partidos perdió? "))

# puntosGanado = 3
# puntosEmpate = 1
# puntosPerdido = 0

# victorias = partidosGanados * puntosGanado
# empate= partidosEmpatados * puntosEmpate
# perdida = partidosPerdidos * puntosPerdido

# puntosTotales = victorias + empate + perdida

# print(f"Los puntos por partidos ganados son: {victorias}")
# print(f"Los puntos por partidos empates son: {empate}")
# print(f"Los puntos por partidos perdidos son: {perdida}")

# print(f"Los puntos totales son: {puntosTotales}")




print("EJERCICIO 4 ")
"""
Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello se debe digitar:
nombre del empleado, la cantidad de horas laboradas en el mes y la tarifa por hora. Se debe
calcular el total devengado por el empleado en el mes e imprimir: Nombre del empleado,
cantidad de horas laboradas y total devengado.

"""

# nombreEmpleado = input("Ingrese su nombre: ")
# horasPorMes = int(input("Ingrese las horas trabajadas por mes: "))
# tarifaPorHora = float(input("Ingrese la tarifa por hora: "))
# devengado = horasPorMes * tarifaPorHora

# print(f"El empleado {nombreEmpleado} ha laborado {horasPorMes} horas en el mes, dandole un total de: ${devengado} en su salario mensual")

print("EJERCICIO 5 ")
"""
Se tiene un triángulo rectángulo cuyos lados deberán ser digitados por el usuario. Se debe
hallar la hipotenusa teniendo en cuenta la formula: H = raíz cuadrada (a**2 + b**2)

"""

ladoA = int(input("Ingrese el lado A: "))
ladoB = int(input("Ingrese en lado B: "))
raizCuadrada = math.sqrt(ladoA**2 + ladoB**2)
hipotenusa = raizCuadrada

print(f"La hipotenusa del triangulo con lados: {ladoA} y {ladoB} es: {hipotenusa}")

print("EJERCICIO 6 ")
"""
Se tiene un horno en casa con temperaturas en grados Celsius centígrado), requiere
transformar la temperatura de 70°C a grados Fahrenheit. Para ello tenga en cuenta la
siguiente fórmula.

"""

# gradoCelsius = int(input("Ingrese los grados Celsius que desea transformar: "))
# fahrenheit = (gradoCelsius * 1.8) + 32

# print(f"Los grados Celsius {gradoCelsius} transformados en Fahrenheit son: {fahrenheit} ")



