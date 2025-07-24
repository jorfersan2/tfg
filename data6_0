import feedparser
import requests
import time
import os
import json
import argparse

def ejecutar_tarea():
    archivo_rss = 'rss_periodicos.txt'
    carpeta_raiz = 'rss_guardadas'
    os.makedirs(carpeta_raiz, exist_ok=True)

    with open(archivo_rss, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    for line in lines:
        name, url = line.split(':', 1)
        name = name.strip().replace(' ', '_')
        url = url.strip()

        print(f"\n========== {name} ==========")

        carpeta_periodico = os.path.join(carpeta_raiz, name)
        os.makedirs(carpeta_periodico, exist_ok=True)

        fecha_epoch = int(time.time())
        feed = feedparser.parse(url)

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

        nombre_archivo = f"{name}_{fecha_epoch}.json"
        ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

        with open(ruta_completa, 'w', encoding='utf-8') as f:
            json.dump(datos_rss, f, ensure_ascii=False, indent=4)

        print(f"RSS de {name} guardado en: {ruta_completa}")

# === Argumentos CLI ===
parser = argparse.ArgumentParser(description="Ejecuta el script una vez o periódicamente.")
parser.add_argument("--duracion", type=int, help="Duración total en minutos.")
parser.add_argument("--intervalo", type=int, help="Intervalo entre ejecuciones en minutos.")
args = parser.parse_args()

# === Ejecutar según modo ===
if args.duracion is None or args.intervalo is None:
    ejecutar_tarea()
else:
    duracion_total_seg = args.duracion * 60
    intervalo_seg = args.intervalo * 60

    inicio = time.time()
    fin = inicio + duracion_total_seg

    while time.time() < fin:
        print(f"\n Ejecutando a las {time.strftime('%Y-%m-%d %H:%M:%S')}")
        ejecutar_tarea()
        tiempo_restante = fin - time.time()
        if tiempo_restante > intervalo_seg:
            time.sleep(intervalo_seg)
        else:
            break
