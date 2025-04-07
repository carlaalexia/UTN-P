#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 10
suma = 0

for i in range(cantidad):

    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / cantidad

print(f"La media de los valores ingresados es de: {media}")