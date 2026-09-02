from solucion.taller import OrdenDeTrabajo, ItemDeTrabajo, Vehiculo, Mecanico


# 1ER TEST ("CAMINOI FELIZ")

vehiculo = Vehiculo("AB123CD")
mecanico = Mecanico("Juan")

orden = OrdenDeTrabajo(numero=1, vehiculo=vehiculo)

item1 = ItemDeTrabajo("Cambio de pastillas", costo=8000)
item2 = ItemDeTrabajo("Cambio de aceite", costo=5000)

orden.agregar_item(item1)
orden.agregar_item(item2)
orden.asignar_mecanico(mecanico)

assert orden.calcular_presupuesto() == 13000
assert orden.mecanico == mecanico


# 2DO TEST ("RECHAZO")

orden1 = OrdenDeTrabajo(numero=1, vehiculo=Vehiculo("AB123CD"))
orden2 = OrdenDeTrabajo(numero=2, vehiculo=Vehiculo("XY987ZW"))

item = ItemDeTrabajo("Cambio de pastillas", costo=8000)

orden1.agregar_item(item)

try:
    orden2.agregar_item(item)
    assert False
except ValueError:
    pass


# 3ER TEST: despues del error el item tiene que seguir en la orden original

assert item.orden == orden1
assert item in orden1.items
assert item not in orden2.items

# COMPROBACION
try:
    orden2.agregar_item(item)
    assert False
except ValueError:
    print("Se rechazo correctamente el item repetido")

print("Todos los tests pasaron correctamente")