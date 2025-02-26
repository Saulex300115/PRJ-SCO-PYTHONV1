def calcularIva(precio):
    precio = precio *0.19
    print("El costo total es: $",precio)

def calculoDesc(precio,descuento):
    precio = precio - (precio * (descuento / 100))
    return precio

def calcularIMC(peso,estatura):
    imc = peso/(estatura**2)
    if imc < 18.5:
        print("Bajo peso")
    elif imc < 24.9:
        print("Adecuado")
    elif imc < 29.9:
        print("Sobre peso")
    elif imc < 34.9:
        print("Obesidad grado 1")
    elif imc < 39.9:
        print("Obesidad grado 2")
    else:
        print("Obesidad grado 3")
