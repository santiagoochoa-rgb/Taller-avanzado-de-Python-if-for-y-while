saldo = 1500000
cantidad_depositos = 0
cantidad_retiros = 0
movimientos = ""
opcion = 0

while opcion != 5:

    print("\nCAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver movimientos realizados")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        print("Saldo disponible: $", saldo)

    elif opcion == 2:

        deposito = float(input("Ingrese el valor a depositar: "))

        if deposito <= 0:
            print("No se permiten depósitos negativos o iguales a cero.")

        else:
            saldo = saldo + deposito
            cantidad_depositos = cantidad_depositos + 1
            movimientos = movimientos + "Depósito: $" + str(deposito) + "\n"

            print("Depósito realizado.")
            print("Nuevo saldo: $", saldo)

    elif opcion == 3:

        retiro = float(input("Ingrese el valor a retirar: "))

        if retiro < 10000:
            print("El retiro mínimo es de $10.000.")

        elif retiro + 4500 > saldo:
            print("No hay suficiente saldo para realizar el retiro.")

        else:
            saldo = saldo - retiro - 4500
            cantidad_retiros = cantidad_retiros + 1
            movimientos = movimientos + "Retiro: $" + str(retiro) + "\n"

            print("Retiro realizado.")
            print("Costo del retiro: $4500")
            print("Nuevo saldo: $", saldo)

    elif opcion == 4:

        print("\nMOVIMIENTOS")

        if movimientos == "":
            print("No se han realizado movimientos.")

        else:
            print(movimientos)

        print("Cantidad de depósitos:", cantidad_depositos)
        print("Cantidad de retiros:", cantidad_retiros)

    elif opcion == 5:

        print("Gracias por utilizar el cajero.")

    else:

        print("Opción inválida.")
