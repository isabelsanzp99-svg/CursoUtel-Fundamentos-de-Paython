emoji_diccionario = {"sonrisa": "😀", "feliz": "😊", "risa": "😂", "amor": "❤️",\
    "corazon": "💖","triste": "😢","enojado": "😡","sorprendido": "😮","guino": "😉",\
        "fuego": "🔥","estrella": "⭐","sol": "☀️","luna": "🌙","perro": "🐶",\
            "gato": "🐱","pizza": "🍕","manzana": "🍎","casa": "🏠",}
    





frase = input("Escribe una frase:")
frase = frase.lower()
palabras = frase.split()

respuesta = ""

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + " "
    else:
        respuesta = respuesta + palabra + " "
print(respuesta)