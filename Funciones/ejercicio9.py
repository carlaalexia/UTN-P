#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = int(input("Ingrese la temperatura en grados celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"\n🌡️  {celsius}°C equivale a {fahrenheit:.0f}°F")