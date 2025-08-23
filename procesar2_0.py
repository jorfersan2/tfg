import json
import subprocess

# Cargar JSON local
with open('rss_manual.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Archivo de salida
output_file = 'resultados_gemma2_2b (2).txt'

with open(output_file, 'w', encoding='utf-8') as out_f:
    for i, noticia in enumerate(data['noticias'], start=1):
        print(f"[INFO] Procesando noticia {i}/{len(data['noticias'])}")  # log simplificado
        
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
            ['ollama', 'run', 'gemma2:2b', prompt],
            capture_output=True, text=True
        )
        
        respuesta = result.stdout.strip()
        out_f.write(respuesta + '\n')
        
        print(f"[INFO] Respuesta: {respuesta}")  # log simplificado

print(f"[INFO] Proceso completado. Resultados guardados en {output_file}")
