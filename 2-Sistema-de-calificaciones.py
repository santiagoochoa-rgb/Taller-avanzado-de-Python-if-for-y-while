cantidad = int(input("ingrese la cantidad de estudiantes: "))

while cantidad <= 0:
    print("la cantidad debe ser mayor que 0")
    cantidad = int(input("ingrese la cantidad de estudiantes: "))

aprobado = 0
reprobados= 0
suma_promedios = 0
promedio_mayor = 0
promedio_menor = 5

for i in range(cantidad):

    print("\nEstudiante", i + 1)

    nota1 = float(input("ingrese la nota 1: "))
    while nota1 < 0 or nota1 > 5:
        print("la nota debe estar entre 0.0 y 5.0")
        nota1 = float(input("ingrese la nota 1: "))

    nota2 = float(input("ingrese la nota 2: "))
    while nota2 < 0 or nota2 > 5:
            print("la nota debe estar entre 0.0 y 5.0")
            nota2 = float(input("ingrese la nota 2: "))

    nota3 = float(input("ingrese la nota 3: "))
    while nota3 < 0 or nota3 > 5:
                print("la nota debe estar entre 0.0 y 5.0")
                nota3 = float(input("ingrese la nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio <= 2.9:
          print("reprobado")
          aprobados = aprobados + 1

    elif promedio <= 3.9:
          print("aprobado")
          aprobados = aprobados + 1

    elif promedio <= 4.5:
          print("sobresaliente")
          aprobados = aprobados + 1

    else:
          print("excelente")
          aprobados = aprobados + 1

    suma_promedios = suma_promedios + promedio

    if promedio > promedio_mayor:
          promedio_mayor = promedio

    if promedio < promedio_menor:
          promedio_menor = promedio

promedio_general = suma_promedios / cantidad

print("\nRESULTADOS")
print("cantidad de aprobados:", aprobados)
print("cantidad de reprobados:", reprobados)
print("promedio general:", promedio_general)
print("promedio mas alto:", promedio_mayor)
print("promedio mas bajo:", promedio_menor)