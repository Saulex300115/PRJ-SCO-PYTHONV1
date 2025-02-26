def calcularIva(precio):
    precio = precio *0.19
    return precio

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


op = 3

while  op != 4:
    print("   MENU   ")
    print("*"*10)
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Ingresar opción: (1-4)"))

    if op == 1:
        precio = int(input("Ingrese precio del producto: "))
        precio = calcularIva(precio)
        print("El precio con IVA es: $",precio)
    elif op == 2:
        precio = int(input("Ingrese precio del producto: "))
        descuento = int(input("Ingrese el % de descuento (0-100): "))
        precio = calculoDesc(precio,descuento)
        print("El total a pagar con un descuento del",descuento,"% es: $",precio)
    elif op == 3:
        peso = float(input("Ingrese su peso: "))
        estatura = float(input("Ingrese estatura: "))
        calcularIMC(peso,estatura)