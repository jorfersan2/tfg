import feedparser
import requests
import time
import os
import json

# Ruta del archivo con nombres y URLs
archivo_rss = 'rss_periodicos.txt'

# Carpeta raíz para guardar las subcarpetas por periódico
carpeta_raiz = 'rss_guardadas'
os.makedirs(carpeta_raiz, exist_ok=True)

# Leer líneas del archivo
with open(archivo_rss, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

# Procesar cada línea del archivo
for line in lines:
    # Separar nombre del periódico y URL
    name, url = line.split(':', 1)
    name = name.strip().replace(' ', '_')
    url = url.strip()

    print(f"\n========== {name} ==========")

    # Crear carpeta del periódico
    carpeta_periodico = os.path.join(carpeta_raiz, name)
    os.makedirs(carpeta_periodico, exist_ok=True)

    # Obtener fecha actual en formato epoch
    fecha_epoch = int(time.time())

    # Parsear el feed
    feed = feedparser.parse(url)

    # Construir estructura JSON
    datos_rss = {
        "titulo_general": feed.feed.get("title", "Sin título"),
        "fecha_actualizacion": feed.feed.get("updated", "Sin fecha de actualización"),
        "entradas": []
    }

    for entry in feed.entries:
        entrada = {
            "titulo": entry.get("title", "Sin título"),
            "descripcion": entry.get("description", entry.get("summary", "Sin descripción"))
        }
        datos_rss["entradas"].append(entrada)

    # Guardar como archivo JSON
    nombre_archivo = f"{name}_{fecha_epoch}.json"
    ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

    with open(ruta_completa, 'w', encoding='utf-8') as f:
        json.dump(datos_rss, f, ensure_ascii=False, indent=4)

    print(f"RSS de {name} guardado en: {ruta_completa}")
