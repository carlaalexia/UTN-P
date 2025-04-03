import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

moda = mode(numeros_aleatorios) 

print(f"Numeros: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if moda is not None:
    if media > mediana > moda:
        print("Sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda)")
    elif media == mediana == moda:
        print("No hay sesgo")
    else:
        print("No se puede determinar el sesgo con precisión")
else:
    print("No se puede calcular la moda, por lo que el sesgo no puede determinarse con certeza.")
