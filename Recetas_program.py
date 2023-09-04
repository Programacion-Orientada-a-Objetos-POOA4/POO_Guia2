
class Ingrediente:
    def __init__(self, nombre, cantidad, unidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad

class PasoPreparacion:
    def __init__(self, descripcion):
        self.descripcion = descripcion

class Receta:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria
        self.ingredientes = []
        self.pasos_preparacion = []

    def agregar_ingrediente(self, nombre, cantidad, unidad):
        ingrediente = Ingrediente(nombre, cantidad, unidad)
        self.ingredientes.append(ingrediente)

    def agregar_paso_preparacion(self, descripcion):
        paso = PasoPreparacion(descripcion)
        self.pasos_preparacion.append(paso)

    def mostrar_receta(self):
        print(f"Receta: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print("\nIngredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente.cantidad} {ingrediente.unidad} de {ingrediente.nombre}")
        print("\nPasos de Preparación:")
        for i, paso in enumerate(self.pasos_preparacion, start=1):
            print(f"{i}. {paso.descripcion}")


mi_receta = Receta("Tarta de Manzana", "Postre")

mi_receta.agregar_ingrediente("Manzanas", 4, "unidades")
mi_receta.agregar_ingrediente("Azúcar", 200, "gramos")
mi_receta.agregar_ingrediente("Harina", 150, "gramos")
mi_receta.agregar_ingrediente("Canela", 1, "cucharadita")


mi_receta.agregar_paso_preparacion("Pelar y cortar las manzanas en rodajas.")
mi_receta.agregar_paso_preparacion("Mezclar las manzanas con el azúcar y la canela.")
mi_receta.agregar_paso_preparacion("Forrar un molde con la masa de harina y verter la mezcla de manzanas.")
mi_receta.agregar_paso_preparacion("Hornear a 180°C durante 40 minutos.")

mi_receta.mostrar_receta()
