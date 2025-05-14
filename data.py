#ESTE SCRIPT FUE EL PRIMERO, USADO SIMPLEMENTE PARA OBTENER EL CONTENIDO DE LAS ETIQUETAS "title" Y "description" DEL RSS DE UN SOLO PERIODICO

import feedparser

# URL del RSS de El País
rss_url = 'https://www.laverdad.es/rss/2.0/portada/'

# Parsear
feed = feedparser.parse(rss_url)

# Recorrer y mostrar solo título y descripción completa
for entry in feed.entries:
    title = entry.title
    description = entry.get('description', entry.get('summary', 'Sin descripción')) #Busca etiquetas description, summary o una por defecto

    print(f"Título: {title}")
    print(f"Descripción: {description}")
    print("-" * 50) #Esto simplemente se usa como metodo para separar cada conjunto titulo-descripción

