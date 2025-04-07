#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

num = int(input("Ingrese un numero entero: "))

digitos = 0

while num > 0:
        num = num // 10
        digitos += 1

print("El numero tiene", digitos, "digitos")
