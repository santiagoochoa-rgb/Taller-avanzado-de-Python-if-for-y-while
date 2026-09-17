numero = int(input("Número decimal: "))

while numero <= 0:
    print("El número debe ser positivo.")
    numero = int(input("Número decimal: "))

binario = ""

while numero > 0:

    residuo = numero % 2
    cociente = numero // 2

    print(numero, "÷ 2 =", cociente, ", residuo", residuo)

    if residuo == 0:
        binario = "0" + binario

    else:
        binario = "1" + binario

    numero = cociente

print("\nResultado binario:", binario)
