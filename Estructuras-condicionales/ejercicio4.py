#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad por favor: "))

if edad < 12 :
    categoria = "niño/a"
elif edad >= 12 and edad < 18 :
    caterogia = "adolescente"
elif edad >=18 and edad < 30 :
    categoria = "adulto/a joven"
else :
    categoria = "adulto"


print(f"Usted es un {categoria}")