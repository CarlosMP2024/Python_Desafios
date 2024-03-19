from te import Te

# Crea dos instancias
te1 = Te()
te2 = Te()

# Almacenar el tipo de dato de cada instancia
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrar por pantalla el valor de cada tipo de dato almacenado
print("Tipo de dato de la primera instancia:", tipo_te1)
print("Tipo de dato de la segunda instancia:", tipo_te2)

# Verificar si los tipos almacenados son iguales
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
