numero = int(input("Ingrese un número entero (0 para terminar): "))

cantidad = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma = 0
mayor = 0
menor = 0

while numero != 0:

    cantidad = cantidad + 1
    suma = suma + numero

    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if cantidad == 1:
        mayor = numero
        menor = numero

    else:

        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero

    numero = int(input("Ingrese otro número (0 para terminar): "))

if cantidad == 0:

    print("No se ingresaron números.")

else:

    promedio = suma / cantidad

    print("\nRESULTADOS")
    print("Cantidad de números:", cantidad)
    print("Cantidad de positivos:", positivos)
    print("Cantidad de negativos:", negativos)
    print("Cantidad de pares:", pares)
    print("Cantidad de impares:", impares)
    print("Suma total:", suma)
    print("Promedio:", promedio)
    print("Número mayor:", mayor)
    print("Número menor:", menor)
