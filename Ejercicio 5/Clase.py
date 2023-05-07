
class PlanAhorro:
    def __init__(self, codigo_plan, modelo, version, valor_vehiculo, cant_cuotas, cant_cuotas_licitacion):
        self.codigo_plan = codigo_plan
        self.modelo = modelo
        self.version = version
        self.valor_vehiculo = valor_vehiculo
        self.cant_cuotas = cant_cuotas
        self.cant_cuotas_licitacion = cant_cuotas_licitacion

    def mostrar_datos(self):
        print(f"Código del plan: {self.codigo_plan}")
        print(f"Modelo del vehículo: {self.modelo}")
        print(f"Versión del vehículo: {self.version}")
        print(f"Valor del vehículo: ${self.valor_vehiculo}")
        print(f"Cantidad de cuotas: {self.cant_cuotas}")
        print(f"Cantidad de cuotas para licitar: {self.cant_cuotas_licitacion}")

    @staticmethod
    def actualizar_valor_vehiculo(plan, nuevo_valor):
        plan.valor_vehiculo = nuevo_valor
        print("El valor del vehículo ha sido actualizado correctamente.")

    @staticmethod
    def calcular_importe_cuota(plan):
        importe_cuota = (plan.valor_vehiculo / plan.cant_cuotas) + (plan.valor_vehiculo * 0.10)
        return importe_cuota * 0.10
