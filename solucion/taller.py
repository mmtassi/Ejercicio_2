class Vehiculo:
    def __init__(self, patente):
        self.patente = patente


class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre


class ItemDeTrabajo:
    def __init__(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo
        self.orden = None


class OrdenDeTrabajo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.items = []
        self.mecanico = None
        self.cerrada = False

    def agregar_item(self, item):
        if self.cerrada:
            raise ValueError("La orden está cerrada")

        if item.orden is not None:
            raise ValueError("El item ya pertenece a una orden")

        self.items.append(item)
        item.orden = self

    def calcular_presupuesto(self):
        total = 0

        for item in self.items:
            total += item.costo

        return total

    def asignar_mecanico(self, mecanico):
        self.mecanico = mecanico

    def cerrar(self):
        self.cerrada = True


class Taller:
    def __init__(self):
        self.mecanicos = []

    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)