import sys

def filtrar_productos(precios, umbral, operacion='mayor'):
    productos_filtrados = []
    for producto, precio in precios.items():
        if operacion == 'mayor':
            if precio > umbral:
                productos_filtrados.append(producto)
        elif operacion == 'menor':
            if precio < umbral:
                productos_filtrados.append(producto)
    return productos_filtrados

def main():
    precios = {'Notebook': 700000,
               'Teclado': 25000,
               'Mouse': 12000,
               'Monitor': 250000,
               'Escritorio': 135000,
               'Tarjeta de Video': 1500000}

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        productos_filtrados = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ', '.join(productos_filtrados))
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        operacion = sys.argv[2]
        if operacion not in ['mayor', 'menor']:
            print("Lo sentimos, no es una operación válida")
            return
        productos_filtrados = filtrar_productos(precios, umbral, operacion)
        if operacion == 'mayor':
            print("Los productos mayores al umbral son:", ', '.join(productos_filtrados))
        else:
            print("Los productos menores al umbral son:", ', '.join(productos_filtrados))
    else:
        print("Uso: python filtro.py umbral [mayor|menor]")

if __name__ == "__main__":
    main()
