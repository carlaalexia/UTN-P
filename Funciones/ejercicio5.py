# Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#3600 segundos --> una horaa

def segundos_a_horas(segundos):
    calculo = segundos / 3600
    return calculo

segundos = int(input("Ingrese los segundos: "))

hora = segundos_a_horas(segundos)

print(f"Los segundos ingresados corresponden a {hora:.2f} horas")
