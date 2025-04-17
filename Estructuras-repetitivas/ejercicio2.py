#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

while True:
    entrada = input("Ingrese un número entero: ")

    if entrada.replace('-', '', 1).replace('.', '', 1).isdigit():
        numero = float(entrada)
        if numero.is_integer():
            num = int(numero)
            break
        else:
            print("Eso es un número decimal, no un entero.")
    else:
        print("Eso no es un número válido.")

digitos = 0

while num > 0:
        num = num // 10
        digitos += 1


print("El numero tiene", digitos, "digitos")
