cantidad_productos = int(input("Ingrese la cantidad de productos: "))

while cantidad_productos <= 0:
    print("La cantidad debe ser mayor que 0.")
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))

subtotal_general = 0
total_descuentos = 0

for i in range(cantidad_productos):

    print("\nProducto", i + 1)

    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))

    while precio <= 0:
        print("El precio debe ser positivo.")
        precio = float(input("Ingrese el precio: "))

    cantidad = int(input("Ingrese la cantidad: "))

    while cantidad <= 0:
        print("La cantidad debe ser positiva.")
        cantidad = int(input("Ingrese la cantidad: "))

    tipo = input("Ingrese el tipo (alimento, aseo u otro): ")
    tipo = tipo.lower()

    subtotal = precio * cantidad
    descuento = 0

    if tipo == "alimento":

        descuento = subtotal * 0.05

    elif tipo == "aseo":

        if cantidad >= 3:
            descuento = subtotal * 0.10

    else:

        descuento = 0

    total_producto = subtotal - descuento

    subtotal_general = subtotal_general + subtotal
    total_descuentos = total_descuentos + descuento

    print("Subtotal del producto: $", subtotal)
    print("Descuento aplicado: $", descuento)
    print("Total del producto: $", total_producto)

descuento_general = 0

if subtotal_general > 300000:
    descuento_general = subtotal_general * 0.05

total_descuentos = total_descuentos + descuento_general
total_antes_descuento_general = subtotal_general - descuento_general
total_definitivo = subtotal_general - total_descuentos

print("\nFACTURA FINAL")
print("Subtotal general: $", subtotal_general)
print("Total antes del descuento general: $", total_antes_descuento_general)
print("Descuento general: $", descuento_general)
print("Total de descuentos: $", total_descuentos)
print("Total definitivo: $", total_definitivo)
