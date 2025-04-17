#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):

    mensaje = (f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return mensaje

print("Ingrese los siguientes datos: ")
nombre = input("\n✏️  Nombre: ")
apellido = input("✏️  Apellido: ")
edad = input("✏️  Edad: ")
residencia = input("✏️  Residencia: ")

mensaje_personalizado = informacion_personal(nombre, apellido, edad, residencia)

print(mensaje_personalizado)