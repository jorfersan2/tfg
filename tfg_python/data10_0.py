import feedparser
import time
import os
import json
import argparse
from pymongo import MongoClient

def limpiar_para_json(obj):
    if isinstance(obj, dict):
        return {k: limpiar_para_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [limpiar_para_json(i) for i in obj]
    elif isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    else:
        return str(obj)

def cargar_credenciales(path='credenciales.txt'):
    creds = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if '=' in line:
                clave, valor = line.strip().split('=', 1)
                creds[clave.strip()] = valor.strip()
    return creds.get('usuario'), creds.get('contraseña')

def ejecutar_tarea():
    archivo_rss = 'rss_periodicos.txt'
    carpeta_raiz = 'rss_guardadas'
    os.makedirs(carpeta_raiz, exist_ok=True)

    # Leer credenciales
    usuario, contraseña = cargar_credenciales()
    if not usuario or not contraseña:
        print("Error: No se pudieron leer las credenciales de MongoDB.")
        return

    client = MongoClient(f"mongodb://{usuario}:{contraseña}@my-mongo:27017/")
    db = client['tfg_db']

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

        try:
            datos_rss_dict = limpiar_para_json(dict(feed))
            nombre_archivo = f"{name}_{fecha_epoch}.json"
            ruta_completa = os.path.join(carpeta_periodico, nombre_archivo)

            with open(ruta_completa, 'w', encoding='utf-8') as f:
                json.dump(datos_rss_dict, f, ensure_ascii=False, indent=4)

            print(f"RSS de {name} guardado en: {ruta_completa}")
        except Exception as e:
            print(f"Error al guardar JSON para {name}: {e}")

        coleccion = db[name]
        entradas = []
        for entry in feed.entries:
            titulo = entry.get('title', 'Sin título')
            descripcion = entry.get('description', entry.get('summary', 'Sin descripción'))

            if coleccion.count_documents({'titulo': titulo, 'descripcion': descripcion}, limit=1) == 0:
                entrada = {
                    'titulo': titulo,
                    'descripcion': descripcion,
                    'fecha_guardado': fecha_epoch
                }
                entradas.append(entrada)

        if entradas:
            coleccion.insert_many(entradas)
            print(f"Insertadas {len(entradas)} entradas nuevas en la colección '{name}' en MongoDB.")
        else:
            print(f"No hay entradas nuevas para insertar de {name}.")

# === Argumentos CLI ===
parser = argparse.ArgumentParser(description="Ejecuta el script una vez o periódicamente.")
parser.add_argument("--duracion", help="Duración total en minutos (o '*' para infinito).")
parser.add_argument("--intervalo", type=int, help="Intervalo entre ejecuciones en minutos.")
args = parser.parse_args()

# === Ejecutar según modo ===
if args.duracion is None or args.intervalo is None:
    ejecutar_tarea()
else:
    intervalo_seg = args.intervalo * 60

    if args.duracion == "*":
        print("\nEjecutando en modo infinito.")
        while True:
            print(f"\n Ejecutando a las {time.strftime('%Y-%m-%d %H:%M:%S')}")
            ejecutar_tarea()
            time.sleep(intervalo_seg)
    else:
        try:
            duracion_total_seg = int(args.duracion) * 60
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
        except ValueError:
            print("Error: --duracion debe ser un número entero o '*'.")
