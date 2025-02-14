print("EJERCICIO 1")
"""
1. Desarrolle un algoritmo que lea un número, en caso de ser negativo lo
imprima junto con su positivo.

"""

# numero = int(input("Ingrese el numero: "))

# if (numero < 0):
#   print(f"{numero}  {numero.__abs__()}")
# else: 
#   print("El numero debe ser negativo")

print("EJERCICIO 2")
"""
2. desarrollar un programa que, dado una calificación de un alumno en un
parcial, escribe aprobado si la calificación es superior a 3.

"""

# calificacion = float(input("Ingrese su calificación: "))


# if (calificacion >= 3 and calificacion <= 5):
#   print("Estudiante aprobado")
# elif (calificacion > 5):
#   print("La calificación debe ser entre 1 a 5")
# else:
#   print("Estudiante no aprobado")

print("EJERCICIO 3")
"""
3. desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
un aumento del 15% si su sueldo es inferior a $300.000.

"""

# sueldo = int(input("Ingrese su sueldo: "))

# if (sueldo < 300000):
#   nuevoSueldo = sueldo * 1.15
#   print(f"Su sueldo con un aumento del 15% es de {nuevoSueldo} ")
# else:
#   print(f"Su sueldo sin aumento es de: {sueldo}")

print("EJERCICIO 4")
"""
4. desarrollar un algoritmo que asigne el sueldo a cinco empleados, teniendo
en cuenta su categoría.

"""
# empleados = 5
# sueldo = 0

# for i in range(empleados): 
#   print(f"Empleado #{i}")
#   categoriaEmpleado = input("Ingrese su categoria para asignarle su sueldo: ")

#   match categoriaEmpleado:
#     case "Programador":
#       sueldo = 5000000
#     case "Profesor":
#       sueldo = 4000000
#     case "Administrador":
#       sueldo = 3000000
#     case "Aprendiz":
#       sueldo = 2000000
#     case "Vendedor":
#       sueldo = 1000000
#   print(f"El empleado {i} pertenece al categoria: {categoriaEmpleado} y tiene un sueldo de: ${sueldo}")

print("EJERCICIO 5")

"""
Desarrollar un programa que capture tres números e imprima por pantalla
cual es el número mayor, el menor, cuales son iguales, si los tres
diferentes.

"""

# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))
# numero3 = int(input("Ingrese el numero 3: "))

# if numero1 == numero2 == numero3:
#   print("Los tres numero son iguales.")
# else:
#   if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
#     print("Hay dos numeros iguales.")
#   else:
#     print("Los tres numeros son diferentes.")

#   mayor = max(numero1, numero2, numero3)
#   menor = min(numero1, numero2, numero3)

#   print(f"El numero mayor es: {mayor}")
#   print(f"El numero menor es: {menor}")

print("EJERCICIO 6")

"""
Escriba el algoritmo que al capturar un numero entero convierta grados
centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5,
y si captura un carácter escriba su nombre.

"""

# gradosCentigrados = int(input("Introduzca los grados centígrados a convertir: "))
# kelvin = gradosCentigrados + 273.15

# print(f"La conversion de {gradosCentigrados} grados centígrados a Kelvin es: {kelvin} ")

print("EJERCICIO 7")

"""
Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
el estado civil de cualquier persona e imprima el nombre de la persona, si
corresponde a un hombre casado mayor de 40 años o a una mujer soltera
menor de 50 años.

"""

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# sexo = input("Ingrese su sexo: ")
# estadoCivil = input("Ingrese su estado civil: ")

# if sexo == "Masculino" and edad > 40 and estadoCivil == "Casado":
#   print(f"El SR {nombre} corresponde a un hombre casado mayor de 40 años ")
# elif sexo == "Femenino" and estadoCivil == "Soltera" and edad < 50:
#   print(f"La SR {nombre} corresponde a una mujer soltera menor de 50 años ")
# else:
#   print(f"La informacion corresponde a: {sexo} - {nombre} - {edad} años - {estadoCivil}")

print("EJERCICIO 8")

"""
Prepare un algoritmo que identifique e imprima el número medio de un
conjunto de tres números únicos. El número medio es aquel que no es el
menor ni el mayor.

"""

# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))
# numero3 = int(input("Ingrese el numero 3: "))

# if (numero1 > numero2 and numero1 < numero3 ) or (numero1 < numero2 and numero1 > numero3):
#   medio = numero1
# elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
#   medio = numero2
# else:
#   medio = numero3

# print(f"El número medio es: {medio}")

print ("EJERCICIO 9")

"""
Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
ordene de mayor a menor e imprímalos.

"""

# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))
# numero3 = int(input("Ingrese el numero 3: "))

# if (numero1 > numero2 and numero1 < numero3 ) or (numero1 < numero2 and numero1 > numero3):
#   medio = numero1
# elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
#   medio = numero2
# else:
#   medio = numero3

# mayor = max(numero1, numero2, numero3)
# menor = min(numero1, numero2, numero3)

# print(f"El orden de mayor a menor es: {mayor} - {medio} - {menor} ")


