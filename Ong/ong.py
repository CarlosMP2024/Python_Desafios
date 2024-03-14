def calcular_factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def calcular_productoria(lista):
    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def calcular(*args):
    for i in range(0, len(args), 2):
        tipo_calculo = args[i]
        valor = args[i + 1]
        if tipo_calculo == "fact":
            resultado_factorial = calcular_factorial(valor)
            print(f"El factorial de {valor} es {resultado_factorial}")
        elif tipo_calculo == "prod":
            resultado_productoria = calcular_productoria(valor)
            print(f"La productoria de {valor} es {resultado_productoria}")

def main():
    calcular("fact", 5, "prod", [4,6,7,4,3], "fact", 6)

if __name__ == "__main__":
    main()
