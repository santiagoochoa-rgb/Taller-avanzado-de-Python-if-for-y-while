n = int(input("Ingrese un número entre 3 y 10: "))

while n < 3 or n > 10:
    print("El número debe estar entre 3 y 10.")
    n = int(input("Ingrese un número entre 3 y 10: "))

for fila in range(1, n + 1):

    for numero in range(1, fila + 1):
        print(numero, end=" ")

    print()

for fila in range(n - 1, 0, -1):

    for numero in range(1, fila + 1):
        print(numero, end=" ")

    print()