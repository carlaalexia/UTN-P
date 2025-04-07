#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese un numero: "))
numeroInvertido = 0

while numero > 0:
    digito = numero % 10
    numeroInvertido = numeroInvertido * 10 + digito
    numero = numero // 10

print("Numero invertido:", numeroInvertido)
