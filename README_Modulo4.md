POKEDEX

El programa consume la API pública PokéAPI https://pokeapi.co/ para consultar estadísticas e imágenes de cualquier Pokémon, valida respuestas HTTP y almacena automáticamente los resultados en archivos .json

¿Cómo funciona y cómo lo construí?

El proyecto está estructurado de forma modular dentro del archivo `ISABEL_SANCHEZ_proyectoM4.py`
1. Entrada: Se solicita al usuario el nombre de un Pokémon y se normaliza con ".strip().lower()" para evitar fallos por espacios extra o mayúsculas.
2. Consumo de la API "obtener_datos_pokemon" 
3. Se realiza una petición "GET" al endpoint "https://pokeapi.co/api/v2/pokemon/{nombre}" mediante la librería "requests".
4. Validación de códigos de estado HTTP, si "status_code != 200" (por ejemplo, `404` cuando el Pokémon no existe), el programa notifica el error al usuario de forma controlada sin detenerse abruptamente.
5. Extracción y despliegue ("extraer_informacion" y "mostrar_estadisticas")
6. Se procesa el JSON recibido para extraer y mostrar en consola el ID, nombre, peso, tamaño, tipos, habilidades, una muestra de movimientos y la URL de su imagen frontal.
7. Persistencia en JSON utilizando "pathlib" y "json", el programa crea automáticamente la carpeta "pokedex/" (si no existe) y guarda la información del Pokémon consultado en un archivo.
8. Visualización de imagen ("mostrar_imagen") Descarga el sprite frontal desde `sprites "front_default", lo procesa en memoria con "BytesIO" y "Pillow", y lo despliega en una ventana gráfica con "matplotlib".

![Resultado de búsqueda Pokédex](captura_pokémon.png) 


REFLEXIONES DEL MODULO 
Este módulo marcó un salto muy importante en mi forma de programar porque pasé de trabajar únicamente con datos locales a conectar mis programas con servicios reales en internet a través de una API. Al construir la Pokédex comprendí mejor cómo funciona una petición HTTP, qué significa validar los códigos de estado (como responder con claridad cuando un Pokémon no existe en lugar de que el programa falle) y cómo extraer únicamente la información necesaria desde estructuras JSON,
me permitió integrar varios temas clave del módulo en un solo proyecto: consumo de APIs con requests, validación de respuestas HTTP, manejo de errores, creación de carpetas.
Más allá del código, el mayor aprendizaje fue aprender a leer los mensajes de error, revisar cada paso con calma y documentar el proceso para que cualquier persona pueda entender y ejecutar el proyecto.
