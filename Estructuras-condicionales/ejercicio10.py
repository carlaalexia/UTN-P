#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().lower()
mes = input("Ingrese el mes en el que se encuentra: ").strip().lower()
dia = int(input("Ingrese el dia en el que se encuentra: "))

if hemisferio not in ["norte", "sur"]:
    print("Hemisferio invalido. Debe ingresar 'norte' o 'sur'.")
else:
    if (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20):
        estacion = "invierno" if hemisferio == "norte" else "verano"
    elif (mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20):
        estacion = "primavera" if hemisferio == "norte" else "otoño"
    elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20):
        estacion = "verano" if hemisferio == "norte" else "invierno"
    elif (mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20):
        estacion = "otoño" if hemisferio == "norte" else "primavera"
    else:
        estacion = "desconocida"

    print(f"Es {estacion}.")
