from te import Te

# Solicitar al usuario ingresar los datos del pedido
sabor_input = int(input("Ingrese el número correspondiente al sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato_input = int(input("Ingrese el formato del té (300 o 500 gramos): "))

# Obtener el resto de valores necesarios para el pedido
tiempo, recomendacion = Te.obtener_info_preparacion(sabor_input)
precio = Te.obtener_precio(formato_input)

# Mostrar en pantalla el detalle del pedido
print("\nDetalle del pedido:")
print("Sabor del té:", end=" ")
if sabor_input == 1:
    print("Té negro")
elif sabor_input == 2:
    print("Té verde")
else:
    print("Agua de hierbas")

print("Formato:", end=" ")
if formato_input == 300:
    print("300 gramos")
elif formato_input == 500:
    print("500 gramos")
else:
    print("Formato no válido")

print("Precio: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
