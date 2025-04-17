#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
# como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
# llamar ambas funciones para mostrar los resultados.

import math

pi = math.pi

def calcular_area_circulo(radio):
    calculo = pi * (radio**2)
    return calculo

def calcular_perimetro_circulo(radio):
   calculo = 2 * pi * radio
   return calculo

radio = int(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es de: {area:.2f} \n y el perimetro es de: {perimetro:.2f}")