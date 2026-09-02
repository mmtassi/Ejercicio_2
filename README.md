**Punto 1 – Identificación de clases**

Los conceptos que aparecen que haria clases son: orden de trabajo, ítem de trabajo, vehículo, mecánico, taller, 
en cambio, presupuesto no vale la pena hacerlo clase porque es la suma de los precios de los items, no necesita 
nada mas.

**Punto 2 – Tarjetas CRC**

**OrdenDeTrabajo**
Responsabilidades: agregar los trabajos que se van a realizar, calcular el presupuesto, asignar un mecánico y controlar el estado de la orden.
Colaboradores: ItemDeTrabajo, Vehiculo y Mecanico.

**ItemDeTrabajo**
Responsabilidades: guardar la descripción del trabajo y su costo, y saber a qué orden pertenece.
Colaboradores: OrdenDeTrabajo.

**Vehiculo**
Responsabilidades: guardar los datos necesarios para identificar el vehículo, como la patente.
Colaboradores: OrdenDeTrabajo.

**Mecanico**
Responsabilidades: guardar los datos del mecánico y trabajar sobre las órdenes que tenga asignadas.
Colaboradores: Taller y OrdenDeTrabajo.

**Taller**
Responsabilidades: administrar los mecáicos y las órdenes de trabajo.
Colaboradores: Mecanico y OrdenDeTrabajo.

**Punto 3 – Relaciones entre clases**

**OrdenDeTrabajo – ItemDeTrabajo: Composición**

Un ítem de trabajo pertenece a una orden y no tiene sentido que exista sin ella. Si se elimina la orden, también se eliminan sus ítems.

No es agregación porque el ítem no puede existir de forma independiente. Tampoco es asociación porque hay una relación de pertenencia entre ambos, ni dependencia porque el ítem queda formando parte de la orden.

**Taller – Mecanico: Agregación**

El taller tiene una lista de mecánicos, pero cada mecánico puede existir independientemente del taller.

No es composición porque el mecánico no depende del taller para existir. Tampoco es asociación porque los mecánicos forman parte de la plantilla del taller, ni dependencia porque el taller mantiene la relación con ellos.

**OrdenDeTrabajo – Vehiculo: Asociación**

Una orden de trabajo corresponde a un vehículo, pero el vehículo puede existir antes y después de esa orden.

No es composición ni agregación porque el vehículo no forma parte de la orden, solamente está relacionado con ella. Tampoco es dependencia porque la orden mantiene la referencia al vehículo.

**Cálculo del presupuesto: Dependencia**

Para calcular el presupuesto se puede utilizar algo externo, como una tabla de precios o descuentos, solamente en el momento de hacer el cálculo.

Ademas, presupuesto no es una clase.
