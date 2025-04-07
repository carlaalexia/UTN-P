#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0

while True:
    num = int(input("Ingrese un numero entero: "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)
