import json
import subprocess
import sys

# Comprobar argumentos
if len(sys.argv) != 3:
    print("Uso: python script.py <modelo> <archivo_salida>")
    sys.exit(1)

modelo = sys.argv[1]          # Ejemplo: "gemma2:2b"
output_file = sys.argv[2]     # Ejemplo: "resultados.txt"

# Cargar JSON local
with open('rss_manual.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Contadores
contador_si = 0
contador_no = 0

with open(output_file, 'w', encoding='utf-8') as out_f:
    for i, noticia in enumerate(data['noticias'], start=1):
        print(f"[INFO] Procesando noticia {i}/{len(data['noticias'])}")  # log

        # Construir prompt
        prompt = (
            f"Responde solo con SI o NO. "
            f"Responde SI si la palabra 'tiempo' aparece literalmente en el título o la descripción. "
            f"Si no aparece, responde NO. "
            f"Título: {noticia['titulo']} "
            f"Descripción: {noticia['descripcion']}"
        )

        # Llamada al modelo
        result = subprocess.run(
            ['ollama', 'run', modelo, prompt],
            capture_output=True, text=True
        )

        respuesta = result.stdout.strip()

        # Guardar resultado
        out_f.write(respuesta + '\n')

        # Contar SI / NO
        if respuesta.upper() == "SI":
            contador_si += 1
        elif respuesta.upper() == "NO":
            contador_no += 1

        print(f"[INFO] Respuesta: {respuesta}")

    # Guardar conteo final
    resumen = f"\n--- RESUMEN ---\nSI: {contador_si}\nNO: {contador_no}\n"
    out_f.write(resumen)

print(f"[INFO] Proceso completado. Resultados guardados en {output_file}")
print(f"[INFO] Conteo final -> SI: {contador_si}, NO: {contador_no}")
