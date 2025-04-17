#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado 
# con dos decimales.

def calcular_imc(peso, altura):
    calculo = peso / (altura**2)
    return calculo

print("Ingrese los siguientes datos: ")
peso = float(input("\nIngrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es de: {imc:.2f}")
