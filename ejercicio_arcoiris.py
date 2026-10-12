# Diccionario con los colores del arcoíris en dos idiomas diferentes
colores_diccionario = {
    "rojo": {"ingles": "red", "frances": "rouge"},
    "naranja": {"ingles": "orange", "frances": "orange"},
    "amarillo": {"ingles": "yellow", "frances": "jaune"},
    "verde": {"ingles": "green", "frances": "vert"},
    "azul": {"ingles": "blue", "frances": "bleu"},
    "violeta": {"ingles": "violet", "frances": "violet"},
}


print("Idiomas disponibles:")
print("- ingles")
print("- frances")

# 2. El usuario elige a cuál de los idiomas quiere traducir[span_1](start_span)[span_1](end_span)
idioma_elegido = input("¿A qué idioma quieres traducir? (escribe 'ingles' o 'frances'): ").lower()

if idioma_elegido != "ingles" and idioma_elegido != "frances":
  print("Idioma no válido.")
else:
  frase = input("Escribe una oración en español que incluya un color: ")
  frase = frase.lower()
  palabras = frase.split()

  encontrado = False

  
  for palabra in palabras:
    if palabra in colores_diccionario:
      traduccion = colores_diccionario[palabra][idioma_elegido]

      print(f"El color '{palabra}' en {idioma_elegido} se dice: '{traduccion}' [cite: 2]")
      
      encontrado = True

  if not encontrado:
    print("No se encontró ningún color del arcoíris en la oración.")