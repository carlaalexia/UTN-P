#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

num = int(input("Ingrese un numero positivo: "))

suma = 0

for i in range(0, num):
    suma += i

print(f"La suma total fue de: {suma}")