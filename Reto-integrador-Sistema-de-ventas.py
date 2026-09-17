opcion = 0

cantidad_ventas = 0
total_bruto = 0
total_descuentos = 0
total_recargos = 0
total_recibido = 0

venta_mayor = 0
venta_menor = 0

pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0

clientes_descuento = 0

while opcion != 5:

    print("\nSISTEMA DE VENTAS")
    print("1. Registrar una venta")
    print("2. Consultar resumen de ventas")
    print("3. Consultar venta mayor y menor")
    print("4. Aplicar cierre de caja")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        print("\nREGISTRAR VENTA")

        nombre = input("Nombre del cliente: ")

        cantidad_productos = int(input("Cantidad de productos: "))

        while cantidad_productos <= 0:
            print("La cantidad debe ser positiva.")
            cantidad_productos = int(input("Cantidad de productos: "))

        subtotal = 0

        for i in range(cantidad_productos):

            print("\nProducto", i + 1)

            precio = float(input("Precio del producto: "))

            while precio <= 0:
                print("El precio debe ser positivo.")
                precio = float(input("Precio del producto: "))

            cantidad = int(input("Cantidad: "))

            while cantidad <= 0:
                print("La cantidad debe ser positiva.")
                cantidad = int(input("Cantidad: "))

            subtotal_producto = precio * cantidad
            subtotal = subtotal + subtotal_producto

        descuento = 0
        recargo = 0

        if subtotal > 500000:

            descuento = subtotal * 0.10
            clientes_descuento = clientes_descuento + 1

        total_con_descuento = subtotal - descuento

        print("\nMEDIO DE PAGO")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Transferencia")

        medio = int(input("Seleccione el medio de pago: "))

        while medio < 1 or medio > 3:
            print("Medio de pago inválido.")
            medio = int(input("Seleccione el medio de pago: "))

        if medio == 1:

            pagos_efectivo = pagos_efectivo + 1

            if subtotal > 200000:

                descuento_adicional = total_con_descuento * 0.03
                descuento = descuento + descuento_adicional
                total_con_descuento = total_con_descuento - descuento_adicional

        elif medio == 2:

            pagos_tarjeta = pagos_tarjeta + 1
            recargo = total_con_descuento * 0.02

        else:

            pagos_transferencia = pagos_transferencia + 1

        total_final = total_con_descuento + recargo

        cantidad_ventas = cantidad_ventas + 1

        total_bruto = total_bruto + subtotal
        total_descuentos = total_descuentos + descuento
        total_recargos = total_recargos + recargo
        total_recibido = total_recibido + total_final

        if cantidad_ventas == 1:

            venta_mayor = total_final
            venta_menor = total_final

        else:

            if total_final > venta_mayor:
                venta_mayor = total_final

            if total_final < venta_menor:
                venta_menor = total_final

        print("\nVENTA REGISTRADA")
        print("Cliente:", nombre)
        print("Subtotal: $", subtotal)
        print("Descuento: $", descuento)
        print("Recargo: $", recargo)
        print("Total definitivo: $", total_final)

    elif opcion == 2:

        if cantidad_ventas == 0:

            print("Todavía no existen ventas.")

        else:

            promedio = total_recibido / cantidad_ventas

            print("\nRESUMEN DE VENTAS")
            print("Cantidad de ventas:", cantidad_ventas)
            print("Valor total antes de descuentos: $", total_bruto)
            print("Total de descuentos: $", total_descuentos)
            print("Total de recargos: $", total_recargos)
            print("Dinero definitivo recibido: $", total_recibido)
            print("Promedio de las ventas: $", promedio)
            print("Venta más alta: $", venta_mayor)
            print("Venta más baja: $", venta_menor)
            print("Pagos en efectivo:", pagos_efectivo)
            print("Pagos con tarjeta:", pagos_tarjeta)
            print("Pagos por transferencia:", pagos_transferencia)
            print("Clientes que recibieron descuento:", clientes_descuento)

    elif opcion == 3:

        if cantidad_ventas == 0:

            print("Todavía no existen ventas.")

        else:

            print("\nVENTA MAYOR Y MENOR")
            print("Venta más alta: $", venta_mayor)
            print("Venta más baja: $", venta_menor)

    elif opcion == 4:

        if cantidad_ventas == 0:

            print("No existen ventas para realizar el cierre.")

        else:

            print("\nCIERRE DE CAJA")
            print("Cantidad de ventas:", cantidad_ventas)
            print("Total bruto: $", total_bruto)
            print("Total descuentos: $", total_descuentos)
            print("Total recargos: $", total_recargos)
            print("Total recibido: $", total_recibido)
            print("Pagos en efectivo:", pagos_efectivo)
            print("Pagos con tarjeta:", pagos_tarjeta)
            print("Pagos por transferencia:", pagos_transferencia)
            print("Caja cerrada correctamente.")

    elif opcion == 5:

        print("Programa finalizado.")

    else:

        print("Opción inválida.")

