import feedparser
import requests
import time
import os

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

        # Descargar contenido del RSS
        response = requests.get(url)
        if response.status_code == 200:
            # Nombre del archivo: nombre_fecha.xml
            nombre_archivo = f"{name}_{fecha_epoch}.xml"
            ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

            # Guardar el contenido XML
            with open(ruta_completa, 'wb') as f:
                f.write(response.content)

            print(f"RSS guardada en: {ruta_completa}")
        else:
            print(f"Error al descargar {name}: código {response.status_code}")
            continue

        # Mostrar título y descripción de cada entrada (opcional)
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title
            description = entry.get('description', entry.get('summary', 'Sin descripción'))

            print(f"Título: {title}")
            print(f"Descripción: {description}")
            print("-" * 50)

    except Exception as e:
        print(f"Error procesando línea '{line}': {e}")
