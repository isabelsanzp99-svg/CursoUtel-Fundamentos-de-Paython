# --- FUNCIÓN 1: Crear una lista ---
def crear_lista(nombre):
    print(f"\n--- Creando la {nombre} ---")
    
    # Pedir la longitud
    longitud = int(input(f"¿Cuántos elementos tendrá la {nombre}?: "))
    
    # Pedir los elementos uno por uno
    lista = []
    for i in range(longitud):
        elemento = input(f"Ingresa el elemento {i + 1}: ")
        lista.append(elemento)
        
    return lista  # Valor de retorno


# --- FUNCIÓN 2: Eliminar duplicados ---
def eliminar_duplicados(lista1, lista2):
    # Filtramos la lista1 dejando solo los elementos que NO estén en la lista2
    lista_filtrada = []
    for elemento in lista1:
        if elemento not in lista2:
            lista_filtrada.append(elemento)
            
    return lista_filtrada  # Valor de retorno


# --- PROGRAMA PRINCIPAL ---
print("¡Bienvenido a tu programa de gestión y filtrado de listas!")

# 1 y 2. Crear dos listas con datos del usuario
lista_1 = crear_lista("Lista 1")
lista_2 = crear_lista("Lista 2")

# 3. Imprimir las listas indicando que son las originales
print("\n--- LISTAS ORIGINALES ---")
print("Lista 1 original:", lista_1)
print("Lista 2 original:", lista_2)

# 4. Eliminar de la primera lista los elementos de la segunda
lista_1_modificada = eliminar_duplicados(lista_1, lista_2)

# 5. Imprimir la primera lista indicando que se eliminaron los elementos
print("\n--- LISTA MODIFICADA ---")
print("Lista 1 después de eliminar los elementos de la Lista 2:", lista_1_modificada)