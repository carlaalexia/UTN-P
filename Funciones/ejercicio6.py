#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tablar_multiplicar(numero):
    for i in range(1, 11):
        print(f"🔸 {i} x {numero}: {numero * i}")


numero = int(input("Ingrese un numero: "))

tabla = tablar_multiplicar(numero)

