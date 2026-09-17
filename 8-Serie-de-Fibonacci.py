cantidad = int(input("Ingrese la cantidad de términos: "))

while cantidad <= 0:
    print("La cantidad debe ser mayor que 0.")
    cantidad = int(input("Ingrese la cantidad de términos: "))

anterior = 0
actual = 1
suma = 0
pares = 0
impares = 0

print("\nSerie:")

for i in range(cantidad):

    print(anterior, end=" ")

    suma = suma + anterior

    if anterior % 2 == 0:
        pares = pares + 1

    else:
        impares = impares + 1

    siguiente = anterior + actual
    anterior = actual
    actual = siguiente

print()

print("Suma de los términos:", suma)
print("Cantidad de términos pares:", pares)
print("Cantidad de términos impares:", impares)