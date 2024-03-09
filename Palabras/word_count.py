import sys

def contar_caracteres_distintos(texto):
    caracteres_distintos = set(texto)
    return len(caracteres_distintos)

def contar_palabras_distintas(texto):
    palabras = texto.split()
    palabras_distintas = set(palabras)
    return len(palabras_distintas)

def main():
    # Manejo de errores si no se proporciona un nombre de archivo
    if len(sys.argv) != 2:
        print("Por favor, proporcione el nombre del archivo de texto.")
        return

    # Intenta leer el archivo especificado en la línea de comandos
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

        # Cuenta caracteres distintos
        num_caracteres_distintos = contar_caracteres_distintos(texto)
        print(f'Número de caracteres distintos: {num_caracteres_distintos}')

        # Cuenta palabras distintas
        num_palabras_distintas = contar_palabras_distintas(texto)
        print(f'Número de palabras distintas: {num_palabras_distintas}')

    except FileNotFoundError:
        print(f'Error: No se pudo encontrar el archivo "{sys.argv[1]}".')

if __name__ == "__main__":
    main()
