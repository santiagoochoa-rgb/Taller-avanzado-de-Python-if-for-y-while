usuario_correcto = "administrador"
clave_correcta = "Python2026"

intentos = 0
acceso = False

while intentos < 3 and acceso == False:

    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso correcto.")

    elif usuario != usuario_correcto and clave != clave_correcta:
        print("Usuario y contraseña incorrectos.")
        intentos = intentos + 1

    elif usuario != usuario_correcto:
        print("Usuario incorrecto.")
        intentos = intentos + 1

    else:
        print("Contraseña incorrecta.")
        intentos = intentos + 1

    if acceso == False:
        print("Intentos restantes:", 3 - intentos)

if acceso == False:
    print("Sistema bloqueado.")

else:
    opcion = 0

    while opcion != 3:

        print("\nMENÚ")
        print("1. Consultar información")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Información del sistema.")

        elif opcion == 2:

            clave_actual = input("Ingrese la contraseña actual: ")

            if clave_actual == clave_correcta:
                nueva_clave = input("Ingrese la nueva contraseña: ")
                clave_correcta = nueva_clave
                print("Contraseña cambiada correctamente.")

            else:
                print("Contraseña actual incorrecta.")

        elif opcion == 3:
            print("Sesión cerrada.")

        else:
            print("Opción inválida.")