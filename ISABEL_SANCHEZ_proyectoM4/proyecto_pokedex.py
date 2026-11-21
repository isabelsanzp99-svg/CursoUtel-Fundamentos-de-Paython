import json #Permite guardar los datos en formato JSON
from pathlib import Path #Facilita crear carpetas y rutas de forma segura 
from urllib.request import urlopen
import matplotlib.pyplot as plt #Permite abrir una ventana y graficar la imagen del Pokémon
from PIL import Image #Perimite abrir y manipular la imagen descargada 
import requests #Permite hacer peticiones http a la PokéAPI y descargar la imagen del Pokémon
from io import BytesIO #Permite leer los bytes de la imagen descargada en memoria


def obtener_datos_pokemon(nombre_pokemon: str) -> dict | None:
    """Consulta la PokéAPI y devuelve el JSON si el Pokémon existe."""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    respuesta = requests.get(url, timeout=10)

    # Validación de status code: si no es 200, el Pokémon no existe o hubo un error HTTP
    if respuesta.status_code != 200:
        print(
            f"Error (código {respuesta.status_code}): No se encontró el Pokémon '{nombre_pokemon}'."
        )
        return None

    return respuesta.json()


def extraer_informacion(datos: dict) -> dict:
    """Extrae las estadísticas solicitadas y el link de la imagen frontal."""
    # Extraer tipos (lista de strings)
    tipos = [item["type"]["name"] for item in datos.get("types", [])]

    # Extraer habilidades (lista de strings)
    habilidades = [
        item["ability"]["name"] for item in datos.get("abilities", [])
    ]

    # Extraer movimientos (tomamos los primeros 10 para mantener legible la consola)
    movimientos = [
        item["move"]["name"] for item in datos.get("moves", [])[:10]
    ]

    # Link de la imagen frontal por defecto
    url_imagen = datos.get("sprites", {}).get("front_default")

    return {
        "id": datos.get("id"),
        "nombre": datos.get("name"),
        "peso": datos.get("weight"),
        "tamano": datos.get("height"),
        "tipos": tipos,
        "habilidades": habilidades,
        "movimientos_muestra": movimientos,
        "total_movimientos": len(datos.get("moves", [])),
        "url_imagen_frontal": url_imagen,
    }


def mostrar_estadisticas(info: dict) -> None:
    """Imprime en consola las estadísticas del Pokémon."""
    print("\n=== DATOS DEL POKÉMON ===")
    print(f"Nombre: {info['nombre'].capitalize()} (#{info['id']})")
    print(f"Peso: {info['peso']}")
    print(f"Tamaño (altura): {info['tamano']}")
    print(f"Tipos: {', '.join(info['tipos']) if info['tipos'] else 'N/A'}")
    print(
        "Habilidades: "
        f"{', '.join(info['habilidades']) if info['habilidades'] else 'N/A'}"
    )
    print(
        f"Movimientos (primeros {len(info['movimientos_muestra'])} de {info['total_movimientos']}): "
        f"{', '.join(info['movimientos_muestra'])}"
    )
    print(f"Link imagen frontal: {info['url_imagen_frontal']}")


def mostrar_imagen(nombre: str, url_imagen: str | None) -> None:
    """Descarga y muestra la imagen frontal usando requests, PIL y matplotlib."""
    if not url_imagen:
        print("Este Pokémon no cuenta con imagen frontal disponible.")
        return

    try:
    
        respuesta_img = requests.get(url_imagen,timeout=10)
        respuesta_img.raise_for_status() 
        imagen = Image.open(BytesIO(respuesta_img.content))
           
        plt.figure(figsize=(4, 4))
        plt.title(nombre.capitalize())
        plt.imshow(imagen)
        plt.axis("off")
        plt.show()
    except Exception as error:
        print(f"No se pudo cargar la imagen del Pokémon ({error}).")


def guardar_en_json(info: dict, carpeta: str = "pokedex") -> Path:
    """Crea la carpeta 'pokedex' si no existe y guarda la información en un .json."""
    ruta_carpeta = Path(carpeta)
    ruta_carpeta.mkdir(parents=True, exist_ok=True)

    archivo_json = ruta_carpeta / f"{info['nombre']}.json"
    with archivo_json.open("w", encoding="utf-8") as archivo:
        json.dump(info, archivo, indent=4, ensure_ascii=False)

    print(f"\nInformación guardada correctamente en: {archivo_json}")
    return archivo_json


def main() -> None:
    nombre = input("Introduce el nombre de un Pokémon: ").strip().lower()
    if not nombre:
        print("Debes ingresar un nombre válido.")
        return

    datos_raw = obtener_datos_pokemon(nombre)
    if datos_raw is None:
        return

    info_pokemon = extraer_informacion(datos_raw)
    mostrar_estadisticas(info_pokemon)
    guardar_en_json(info_pokemon, carpeta="pokedex")
    mostrar_imagen(info_pokemon["nombre"], info_pokemon["url_imagen_frontal"])


if __name__ == "__main__":
    main()