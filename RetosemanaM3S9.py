def mostrar_adyacentes(letra):
    # Definimos el abecedario para minúsculas y mayúsculas
    minis = "abcdefghijklmnopqrstuvwxyz"
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Verificamos si es minúscula
    if letra in minis:
        pos = minis.find(letra)
        
        # Obtenemos la anterior
        if pos > 0:
            anterior = minis[pos - 1]
        else:
            anterior = "No tiene (es la 'a')"
            
        # Obtenemos la siguiente
        if pos < len(minis) - 1:
            siguiente = minis[pos + 1]
        else:
            siguiente = "No tiene (es la 'z')"
            
        print(f"La letra anterior es: {anterior}")
        print(f"La letra siguiente es: {siguiente}\n")
        
    # Verificamos si es mayúscula
    elif letra in mayus:
        pos = mayus.find(letra)
        
        if pos > 0:
            anterior = mayus[pos - 1]
        else:
            anterior = "No tiene (es la 'A')"
            
        if pos < len(mayus) - 1:
            siguiente = mayus[pos + 1]
        else:
            siguiente = "No tiene (es la 'Z')"
            
        print(f"La letra anterior es: {anterior}")
        print(f"La letra siguiente es: {siguiente}\n")
        
    else:
        print("Ese carácter no es una letra del abecedario.\n")


# --- Código principal ---
print("--- PROGRAMA DE LETRAS ADYACENTES ---")
print("Escribe 'salir' para terminar el programa.\n")

# Bucle infinito para solicitar la letra continuamente
while True:
    entrada = input("Ingresa una letra: ")
    
    # Condición para salir del programa
    if entrada == "salir":
        print("¡Hasta luego!")
        break
        
    # Validamos que sea solo una letra
    if len(entrada) == 1 and entrada.isalpha():
        # Llamamos a nuestra función pasándole la letra
        mostrar_adyacentes(entrada)
    else:
        print("Error: Ingresa únicamente una sola letra.\n")