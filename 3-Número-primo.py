numero = int(input("ingrese un numero entero mayor que 1: "))

while numero <= 1:
    print("el numero debe ser mayor que 1")
    numero = int(input("ingrese un numero entero mayor que 1: "))

cantidad_divisores = 0

print("divisores:", end=" ")

for i in range(1, numero + 1):

    if numero % i == 0:
        print(i, end=" ")
        cantidad_divisores = cantidad_divisores + 1

print()

if cantidad_divisores == 2:
    print("el numero", numero, "es primo")

else:
    print("el numero", numero, "no es primo")
