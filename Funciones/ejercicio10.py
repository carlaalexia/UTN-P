#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

def calcular_promedio(a,b,c):
    calculo = (a + b + c) / 3
    return calculo

print("Ingrese 3 numeros: ")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"\nSu promedio es de: {promedio:.0f}")
