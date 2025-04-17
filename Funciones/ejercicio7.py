#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = 0

    if(a > b):
        resta = a - b
    else:
        resta = b - a

    multiplicacion = a * b

    if(b == 0):
        division = b / a
    else:
        division = a / b

    return suma, resta, multiplicacion, division


print("Ingrese dos numeros")
num1 = int(input("\nNumero 1: "))
num2 = int(input("Numero 2: "))

operaciones = operaciones_basicas(num1, num2)

print("\nOperaciones realizadas:")
print(f"Suma: {operaciones[0]}")
print(f"Resta: {operaciones[1]}")
print(f"Multiplicación: {operaciones[2]}")
print(f"División: {operaciones[3]}") 