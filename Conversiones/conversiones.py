import sys

def convertir_pesos_chilenos(tasas, cantidad):
    sol_peruano = tasas[0] * cantidad
    peso_argentino = tasas[1] * cantidad
    dolar_americano = tasas[2] * cantidad
    return sol_peruano, peso_argentino, dolar_americano

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error: Se esperan 3 tasas de conversión y un valor en peso chileno como argumentos.")
        sys.exit(1)

    try:
        tasas = [float(arg) for arg in sys.argv[1:4]]
        valor_en_pesos_chilenos = float(sys.argv[4])
    except ValueError:
        print("Error: Los argumentos deben ser números.")
        sys.exit(1)

    resultados = convertir_pesos_chilenos(tasas, valor_en_pesos_chilenos)

    print(f"Los {valor_en_pesos_chilenos} pesos equivalen a:")
    print(f"{resultados[0]} Soles")
    print(f"{resultados[1]} Pesos Argentinos")
    print(f"{resultados[2]} Dólares")
