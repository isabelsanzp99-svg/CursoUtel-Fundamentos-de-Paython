def crear_listas():
    """
    Solicita al usuario cuántas listas desea crear y la longitud de cada una,
    utilizando una lista de listas para almacenarlas.
    """
    lista_de_listas = []
    
    num_listas = int(input("¿Cuántas listas deseas crear?: "))
    
    for i in range(num_listas):
        print(f"\n--- Creando la Lista {i + 1} ---")
        longitud = int(input(f"Ingresa la cantidad de elementos para la lista {i + 1}: "))
        
        sublista = []
        for j in range(longitud):
            elemento = input(f"Ingresa el elemento {j + 1}: ")
            sublista.append(elemento)
            
        lista_de_listas.append(sublista)
        
    return lista_de_listas


def imprimir_listas(lista_de_listas, mensaje):
    """
    Imprime las listas en pantalla indicando un mensaje personalizado 
    (por ejemplo, si son las originales o las modificadas).
    """
    print(f"\n--- {mensaje} ---")
    for i, lista in enumerate(lista_de_listas):
        print(f"Lista {i + 1}: {lista}")


def eliminar_elementos_posteriores(lista_de_listas):
    """
    Elimina de cada lista los elementos que también aparezcan 
    en las listas posteriores.
    """
    lista_modificada = []
    
    for i in range(len(lista_de_listas)):
        actual = lista_de_listas[i]
        
        # Recopilamos todos los elementos de las listas que están después de la actual
        elementos_posteriores = set()
        for j in range(i + 1, len(lista_de_listas)):
            for item in lista_de_listas[j]:
                elementos_posteriores.add(item)
                
        # Filtramos la lista actual para conservar solo los elementos que NO estén en las posteriores
        nueva_sublista = [item for item in actual if item not in elementos_posteriores]
        lista_modificada.append(nueva_sublista)
        
    return lista_modificada