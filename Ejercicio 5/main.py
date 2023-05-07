import csv
from Clase import PlanAhorro

# Leer datos de planes desde archivo csv
planes = []
with open('planes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        plan = PlanAhorro(row[0], row[1], row[2], float(row[3]), int(row[4]), int(row[5]))
        planes.append(plan)


while True:
    print("Seleccione una opción:")
    print("1. Actualizar valor del vehículo de un plan")
    print("2. Mostrar plan con cuota inferior a un valor dado")
    print("3. Mostrar monto a pagar para licitar el vehículo")
    print("4. Modificar cantidad de cuotas para licitar")
    print("5. Salir")
    opcion = int(input())

    if opcion == 1:
        print("Ingrese el código del plan:")
        codigo = input()
        print("Ingrese el modelo del vehículo:")
        modelo = input()
        print("Ingrese la versión del vehículo:")
        version = input()
        print("Ingrese el nuevo valor del vehículo:")
        nuevo_valor = float(input())

        encontrado = False
        for plan in planes:
            if plan.codigo_plan == codigo and plan.modelo == modelo and plan.version == version:
                PlanAhorro.actualizar_valor_vehiculo(plan, nuevo_valor)
                encontrado = True
                break

    if opcion == 2:
         print("Ingrese el valor máximo de la cuota:")
         valor_max = float(input())
         for plan in planes:
         importe_cuota = PlanAhorro.calcular_importe_cuota(plan)
         if importe_cuota < valor_max:
            plan.mostrar_datos()

    elif opcion == 3:
    for plan in planes:
        monto_licitacion = PlanAhorro.calcular_importe_cuota(plan) * plan.cant_cuotas_licitacion
        print(f"Plan {plan.codigo_plan}: ${monto_licitacion}")

    elif opcion == 4:
    print("Ingrese el código del plan:")
    codigo = input()
    print("Ingrese la nueva cantidad de cuotas para licitar:")
    cant_cuotas_licitacion = int(input())

    encontrado = False
    for plan in planes:
        if plan.codigo_plan == codigo:
            plan.cant_cuotas_licitacion = cant_cuotas_licitacion
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un plan con ese código.")

    elif opcion == 5:
    break

    else:
    print("Opción inválida. Intente nuevamente.")
