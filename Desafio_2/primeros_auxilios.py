def primeros_auxilios():
    print("Inicio:")
    
    respuesta_estimulos = input("¿Responde a estímulos? (Si/No): ").lower()

    if respuesta_estimulos == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
    else:
        print("Abrir la vía aérea.")
        
        respira = input("¿Respira? (Si/No): ").lower()
        
        if respira == "si":
            print("Permitirle posición de suficiente ventilación.")
        else:
            print("Administrar 5 ventilaciones y llamar a la ambulancia.")
            
            signos_vida = input("¿Signos de vida? (Si/No): ").lower()

            while signos_vida == "no":
                print("Administrar compresiones hasta que llegue la ambulancia.")
                
                llego_ambulancia = input("¿Llegó la ambulancia? (Si/No): ").lower()

                if llego_ambulancia == "si":
                    return
                else:
                    signos_vida = input("¿Signos de vida? (Si/No): ").lower()

            if signos_vida == "si":
                print("Reevaluar a la espera de la ambulancia.")

                llego_ambulancia = input("¿Llegó la ambulancia? (Si/No): ").lower()

                if llego_ambulancia == "si":
                    return  
                else:
                    while signos_vida == "si":
                        signos_vida = input("¿Signos de vida? (Si/No): ").lower()
                    
                        if signos_vida == "no":
                            print("Administrar compresiones hasta que llegue la ambulancia.")
                            llego_ambulancia = input("¿Llegó la ambulancia? (Si/No): ").lower()
                            
                            if llego_ambulancia == "si":
                                return  
                            else:
                                signos_vida = input("¿Signos de vida? (Si/No): ").lower()

if __name__ == "__main__":
    primeros_auxilios()
