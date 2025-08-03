#ESTE SCRIPT SE ENCARGA DE GENERAR AUTOMATICAMENTE LAS COLECCIONES Y LAS CARPETAS DE LA BBDD (MONGODB), Y SE AÑADEN LOS FICHEROS
import os
import csv
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/") #Forma de conectarse al servidor MongoDB, siempre en el puerto 27017
db = client["prueba2"] #Nombre que le doy a la coleccion. ¡¡¡CAMBIAR NOMBRE DESPUES DE PRUEBAS!!!

# Lista de carpetas (cada una será una colección)
carpetas = [
    "ABC", "El_Correo", "El_Mundo", "El_Pais", "La_Vanguardia", "La_Verdad"
]
ruta_base = "C:\\Users\\Lenovo\\Desktop\\TFG\\rss_guardadas"  #Ruta a las carpetas, se ponen dos veces \\ para que se lea como una ruta y no como una secuencia de escape

for nombre_carpeta in carpetas:
    ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
    coleccion = db[nombre_carpeta]

    print(f"\n Procesando carpeta: {nombre_carpeta}")
    documentos_insertados = 0

    # Procesar cada archivo CSV en la carpeta
    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".csv"):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            try:
                with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    documentos = list(reader)

                    if documentos:
                        coleccion.insert_many(documentos)
                        documentos_insertados += len(documentos)
                        print(f"   + {archivo}: {len(documentos)} documentos insertados.")
                    else:
                        print(f"   - {archivo}: vacío o sin cabecera.")

            except Exception as e:
                print(f"Error al procesar {archivo}: {e}")

    print(f"Total insertado en '{nombre_carpeta}': {documentos_insertados} documentos")

print("\n Proceso finalizado con éxito.")
