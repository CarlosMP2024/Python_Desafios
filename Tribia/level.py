def choose_level(n_pregunta, p_level):
    if p_level == 1:
        if n_pregunta % 3 == 1:
            return "basicas"
        elif n_pregunta % 3 == 2:
            return "intermedias"
        else:
            return "avanzadas"
    elif p_level == 2:
        if n_pregunta <= 2:
            return "basicas"
        elif n_pregunta <= 4:
            return "intermedias"
        else:
            return "avanzadas"
    elif p_level == 3:
        if n_pregunta <= 3:
            return "basicas"
        elif n_pregunta <= 6:
            return "intermedias"
        else:
            return "avanzadas"
    else:
        raise ValueError("El número de preguntas por nivel debe ser 1, 2 o 3.")

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(1, 1)) # basicas
    print(choose_level(2, 1)) # intermedias
    print(choose_level(3, 1)) # avanzadas
    print(choose_level(2, 2)) # basicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # basicas
    print(choose_level(5, 3)) # intermedias
    print(choose_level(9, 3)) # avanzadas
