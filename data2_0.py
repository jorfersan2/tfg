import feedparser

# Leer las líneas del archivo con nombre y URL
with open('rss_periodicos.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

# Procesar cada línea (medio + URL)
for line in lines:
    # Separar por el primer ':' (nombre del medio y la URL)
    name, url = line.split(':', 1)
    name = name.strip()
    url = url.strip()

    print(f"\n========== {name} ==========")

    # Parsear el feed RSS
    feed = feedparser.parse(url)

    # Recorrer las noticias
    for entry in feed.entries:
        title = entry.title
        description = entry.get('description', entry.get('summary', 'Sin descripción'))

        print(f"Título: {title}")
        print(f"Descripción: {description}")
        print("-" * 50)

