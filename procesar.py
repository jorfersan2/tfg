import json
import subprocess

# Carga el JSON local
with open("rss_manual.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("resultados.txt", "w", encoding="utf-8") as f:
    for noticia in data["noticias"]:
        texto = f"Responde solo con SI o NO. Responde SI si la palabra 'tiempo' aparece literalmente en el texto. Si no aparece, responde NO.\nTitulo: {noticia['titulo']}\nDescripcion: {noticia['descripcion']}"
        
        # Llamada al modelo por cada noticia
        result = subprocess.run(
            ["ollama", "run", "gemma3:12b", texto],
            capture_output=True,
            text=True
        )
        
        respuesta = result.stdout.strip()
        
        # Escribir solo la respuesta en el txt
        f.write(f"{respuesta}\n")

