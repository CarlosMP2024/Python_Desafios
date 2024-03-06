from string import ascii_lowercase
from getpass import getpass

def fuerza_bruta(password):
    intentos = 0
    longitud_password = len(password)
    
    for letra in ascii_lowercase:
        if letra == password[0]:
            intentos += 1
            break
        intentos += 1

    for i in range(1, longitud_password):
        for letra in ascii_lowercase:
            if letra == password[i]:
                intentos += 1
                break
            intentos += 1

    return intentos

if __name__ == "__main__":
    contraseña_oculta = getpass("Ingrese la contraseña: ").lower()  # Convierte a minúsculas
    intentos_necesarios = fuerza_bruta(contraseña_oculta)
    
    print(f"La contraseña fue forzada en {intentos_necesarios} intentos")

