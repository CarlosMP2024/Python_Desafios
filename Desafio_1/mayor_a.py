import sys

def filtrar_por_umbral(ventas, umbral):
    meses_superiores = {mes: ventas[mes] for mes, valor in ventas.items() if valor > umbral}
    return meses_superiores

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python mayor_a.py <umbral>")
        sys.exit(1)

    umbral = int(sys.argv[1])

    ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
    }

    resultado = filtrar_por_umbral(ventas, umbral)
    print(resultado)
