#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import *

random = randint(0, 9)
suma = 1

while True:
    num = int(input("Adivine el numero entre 0 y 9: "))
    if random == num: 
        break
    suma += 1

print(f"El numero oculto era: {random}")
print(f"El numero de intentos fue de: {suma}")