#ESTE ES EL TERCER SCRIPT, EL CUAL HACE LO MISMO QUE LOS DOS ANTERIORES (REUTILIZANDO CÓDIGO) Y HEMOS AÑADIDO QUE LOS RSS SE DESCARGUEN EN FORMATO .XML Y SE GUARDEN EN LOCAL EN LAS RUTAS PROPORCIONADAS
import feedparser
import requests
import time
import os

# Ruta del archivo con nombres y URLs
archivo_rss = 'rss_periodicos.txt'

# Carpeta raíz para guardar las subcarpetas por periódico
carpeta_raiz = 'rss_guardadas'
os.makedirs(carpeta_raiz, exist_ok=True) #exist_ok es un argumento específico de la función os.makedirs(), no puede tener otro nombre y sirve para saber si ya existe el directorio que se quiere crear.

# Leer líneas del archivo
with open(archivo_rss, 'r', encoding='utf-8') as file: #La opción encoding sirve para soportar caracteres como "ñ"
    lines = [line.strip() for line in file if line.strip()]

# Procesar cada línea del archivo
for line in lines:
    # Separar nombre del periódico y URL
    name, url = line.split(':', 1)
    name = name.strip().replace(' ', '_')  # Reemplazar espacios por guiones bajos, por comodidad para trabajar desde un terminal.
    url = url.strip()

    print(f"\n========== {name} ==========")

    # Crear carpeta del periódico
    carpeta_periodico = os.path.join(carpeta_raiz, name)
    os.makedirs(carpeta_periodico, exist_ok=True)

    # Obtener fecha actual en formato epoch
    fecha_epoch = int(time.time())

    # Descargar contenido del RSS
    response = requests.get(url)
    if response.status_code == 200: #Estado de solicitud exitosa
        # Nombre del archivo: nombre_fechaepoch.xml
        nombre_archivo = f"{name}_{fecha_epoch}.xml"
        ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

        # Guardar el contenido XML
        with open(ruta_completa, 'wb') as f: #wb es para copiar en formato binario, ya que un RSS viene en ese formato (XML)
            f.write(response.content)

        print(f"RSS guardada en: {ruta_completa}")
    else:
        print(f"Error al descargar {name}: código {response.status_code}") #Si la solicitud no es exitosa, nos da error e imprime el codigo de estado
        continue

    # Mostrar título y descripción de cada entrada
    feed = feedparser.parse(url)
    for entry in feed.entries:
        title = entry.title
        description = entry.get('description', entry.get('summary', 'Sin descripción'))

        print(f"Título: {title}")
        print(f"Descripción: {description}")
        print("-" * 50)


