from pizza import Pizza

# Requerimiento 5a
print("Atributos de clase de la clase Pizza:")
print("Ingredientes proteicos posibles:", Pizza.ingredientes_proteicos_posibles)
print("Ingredientes vegetales posibles:", Pizza.ingredientes_vegetales_posibles)
print("Tipos de masa posibles:", Pizza.tipos_de_masa_posibles)

# Requerimiento 5b
print("\n¿La salsa de tomate está presente en la lista de ingredientes posibles?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Requerimiento 5c
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# Requerimiento 5d
print("\nDetalle de la pizza creada:")
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Tipo de masa:", mi_pizza.tipo_de_masa)
print("¿Es una pizza válida?:", mi_pizza.es_pizza_valida)

# Requerimiento 5e
print("\n¿La clase Pizza es una pizza válida?")
print(Pizza.es_clase_pizza_valida)
