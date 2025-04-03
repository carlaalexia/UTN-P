texto = input("Ingrese una frase o palabra: ").strip() 

vocales = "aeiouAEIOU"

if texto and texto[-1] in vocales: 
    texto += "!"

print(texto)
