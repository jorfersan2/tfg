import feedparser
import requests
import time
import os
import csv

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
    try:
        # Separar nombre del periódico y URL
        name, url = line.split(':', 1)
        name = name.strip().replace(' ', '_')  # Reemplazar espacios por guiones bajos
        url = url.strip()

        print(f"\n========== {name} ==========")

        # Crear carpeta del periódico
        carpeta_periodico = os.path.join(carpeta_raiz, name)
        os.makedirs(carpeta_periodico, exist_ok=True)

        # Obtener fecha actual en formato epoch
        fecha_epoch = int(time.time())

        # Parsear el feed
        feed = feedparser.parse(url)
        if not feed.entries:
            print(f"No se encontraron entradas en {name}")
            continue

        # Nombre del archivo CSV
        nombre_archivo = f"{name}_{fecha_epoch}.csv"
        ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

        # Guardar los datos en formato CSV
        with open(ruta_completa, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Título', 'Descripción'])  # Cabecera

            for entry in feed.entries:
                title = entry.title
                description = entry.get('description', entry.get('summary', 'Sin descripción'))
                writer.writerow([title, description])

                # Mostrar por consola
                print(f"Título: {title}")
                print(f"Descripción: {description}")
                print("-" * 50)

        print(f"RSS de {name} guardado en: {ruta_completa}")

    except Exception as e:
        print(f"Error procesando línea '{line}': {e}")
