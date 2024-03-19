class Te:
    # Atributos de clase
    precios = {
        300: 3000,
        500: 5000
    }

    tiempos_preparacion = {
        1: 3,  # Té negro
        2: 5,  # Té verde
        3: 6   # Agua de hierbas
    }

    recomendaciones = {
        1: "Al desayuno",
        2: "Al medio día",
        3: "Al atardecer"
    }

    @staticmethod
    def obtener_info_preparacion(sabor):
        tiempo = Te.tiempos_preparacion.get(sabor)
        recomendacion = Te.recomendaciones.get(sabor)
        return tiempo, recomendacion

    @staticmethod
    def obtener_precio(formato):
        precio = Te.precios.get(formato)
        if precio is None:
            print("Formato no válido.")
            return "Formato no válido"
        return precio
