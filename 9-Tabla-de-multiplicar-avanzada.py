pares = 0
impares = 0
mayores_50 = 0

for tabla in range(1, 11):

    print("\nTABLA DEL", tabla)

    for numero in range(1, 11):

        resultado = tabla * numero

        print(tabla, "x", numero, "=", resultado)

        if resultado % 2 == 0:
            pares = pares + 1

        else:
            impares = impares + 1

        if resultado > 50:
            mayores_50 = mayores_50 + 1

print("\nRESULTADOS")
print("Resultados pares:", pares)
print("Resultados impares:", impares)
print("Resultados mayores que 50:", mayores_50)