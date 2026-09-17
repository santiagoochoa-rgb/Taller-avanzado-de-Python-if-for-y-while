lado1 = float(input("ingrese el lado 1: "))
lado2 = float(input("ingrese el lado2: "))
lado3 = float(input("ingrese el lado3: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("los lados deben ser positivos")

else:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        if lado1 == lado2 and lado2 == lado3:
            print("triangulo equilatero")

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("triangulo isosceles")

        else:
            print("triangulo escaleno")

    else:
        print("los lados no pueden formar un triangulo")
