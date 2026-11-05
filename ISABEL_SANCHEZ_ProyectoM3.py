import random
import matplotlib.pyplot as plt

def calcular_galton(num_canicas=3000, niveles=12):
    """
    Simula la caída de las canicas a través de niveles de obstáculos.
    Cada nivel representa una decisión aleatoria: 
    0 para la izquierda y 1 para la derecha.
    Retorna una lista con la posición final (contenedor) de cada canica.
    """
    resultados = []

    
    #Ciclo para simular cada una de las 3000 canicas
    for _ in range(num_canicas):
        posicion = 0
        #Cada canica atraviesa 12 niveles de obstáculos
        for _ in range(niveles):
            #Se elige de forma aleatoria si va a la izquierda (0) o derecha (1)
            posicion += random.choice([0, 1])
            
        #Se guarda el contenerdor final, donde cayó la canica
        resultados.append(posicion)
        
    return resultados

def graficar_histograma(resultados):
    """
    Recibe la lista de resultados de las canicas y genera un histograma 
    con los títulos, etiquetas y diseño requeridos.
    """
    # Configuramos el tamaño de la figura
    plt.figure(figsize=(8, 6))
    
    # Creamos el histograma con los contenedores correspondientes (de 0 a 12)
    plt.hist(resultados, bins=range(13), align='left', rwidth=0.85, color='tab:pink', edgecolor='black')
    
    # Añadir títulos y nombres a los ejes
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Distribución de canicas (Contenedores)")
    plt.ylabel("Cantidad de canicas")
    
    # Mostrar el gráfico en pantalla
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Parámetros solicitados 
    CANTIDAD_CANICAS = 3000
    NIVELES_OBSTACULOS = 12
    
    print("Ejecutando simulación de la Máquina de Galton...")
    
    # 1. Llama a la función para calcular los resultados
    posiciones_finales = calcular_galton(CANTIDAD_CANICAS, NIVELES_OBSTACULOS)
    
    # 2. Llama a la función para graficar el histograma
    graficar_histograma(posiciones_finales)