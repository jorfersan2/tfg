#ESTE FUE EL SEGUNDO SCRIPT, OBTIENE LAS MISMAS ETIQUETAS QUE ANTES, PERO AHORA NO SOLO DE UN PERIÓDICO. LO OBTIENE DE UNA LISTA CONCRETA DE UN ARCHIVO .TXT
import feedparser

# Leer las líneas del archivo con nombre y URL
with open('rss_periodicos.txt', 'r') as file: #Se abre el archivo solo con permisos de lectura
    lines = [line.strip() for line in file if line.strip()] #Creo la variable de forma que no se iteren lineas en blanco

# Procesar cada línea (periodico + URL)
for line in lines:
    # Separar por el primer ':' (periodico y la URL)
    name, url = line.split(':', 1)
    name = name.strip()
    url = url.strip()

    print(f"\n========== {name} ==========")

    # Parsear el feed RSS
    feed = feedparser.parse(url)

#Reutilizado de data.py
    # Recorrer las noticias
    for entry in feed.entries:
        title = entry.title
        description = entry.get('description', entry.get('summary', 'Sin descripción'))

        print(f"Título: {title}")
        print(f"Descripción: {description}")
        print("-" * 50)

