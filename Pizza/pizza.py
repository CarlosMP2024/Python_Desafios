class Pizza:
    # Atributos de clase
    ingredientes_proteicos_posibles = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales_posibles = ["tomate", "aceitunas", "champiñones"]
    tipos_de_masa_posibles = ["tradicional", "delgada"]
    es_clase_pizza_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_de_masa = None
        self.es_pizza_valida = False

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        ingrediente1 = input("Ingrese el primer ingrediente vegetal: ")
        ingrediente2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_de_masa = input("Ingrese el tipo de masa (tradicional, delgada): ")

        # Agregar ingredientes a la lista 
        self.ingredientes_vegetales.append(ingrediente1)
        self.ingredientes_vegetales.append(ingrediente2)

        # Verifica si los ingredientes son válidos
        if (Pizza.validar_elemento(self.ingrediente_proteico, Pizza.ingredientes_proteicos_posibles) and
                all(ingrediente in Pizza.ingredientes_vegetales_posibles for ingrediente in self.ingredientes_vegetales) and
                Pizza.validar_elemento(self.tipo_de_masa, Pizza.tipos_de_masa_posibles)):
            self.es_pizza_valida = True


