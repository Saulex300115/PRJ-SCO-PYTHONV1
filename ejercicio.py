import funciones as fn

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
        fn.calcularIva(precio)
    elif op == 2:
        precio = int(input("Ingrese precio del producto: "))
        descuento = int(input("Ingrese el % de descuento (0-100): "))
        precio = fn.calculoDesc(precio,descuento)
        print("El total a pagar con un descuento del",descuento,"% es: $",precio)
    elif op == 3:
        peso = float(input("Ingrese su peso: "))
        estatura = float(input("Ingrese estatura: "))
        fn.calcularIMC(peso,estatura)