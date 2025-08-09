from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime, timedelta
import time

app = Flask(__name__)

def leer_credenciales():
    with open('credenciales.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    user = lines[0].split('=')[1].strip()
    password = lines[1].split('=')[1].strip()
    return user, password

usuario, contrasena = leer_credenciales()
mongo_uri = f"mongodb://{usuario}:{contrasena}@my-mongo:27017/"
client = MongoClient(mongo_uri)
db = client['tfg_db']

@app.route('/periodicos', methods=['GET'])
def listar_periodicos():
    colecciones = db.list_collection_names()
    return jsonify({"periodicos": colecciones})

@app.route('/entradas/<periodico>', methods=['GET'])
def entradas_periodico(periodico):
    coleccion = db[periodico]

    fecha_str = request.args.get('fecha')     # dd-mm-aaaa
    hora_str = request.args.get('hora')       # hora inicio (0-23)
    horafin_str = request.args.get('horafin') # hora fin opcional (0-23)

    if not fecha_str or not hora_str:
        return jsonify({"error": "Debe indicar al menos fecha (dd-mm-aaaa) y hora (0-23)"}), 400

    try:
        fecha_dt = datetime.strptime(fecha_str, "%d-%m-%Y")
        hi = int(hora_str)

        if horafin_str:
            hf = int(horafin_str)
        else:
            hf = hi  # si no hay hora fin, usar la misma

        hi_dt = fecha_dt.replace(hour=hi, minute=0, second=0)

        if hf < hi:
            # Cruza medianoche → sumamos un día a la hora final
            hf_dt = (fecha_dt + timedelta(days=1)).replace(hour=hf, minute=59, second=59)
        else:
            hf_dt = fecha_dt.replace(hour=hf, minute=59, second=59)

        ts_inicio = int(time.mktime(hi_dt.timetuple()))
        ts_fin = int(time.mktime(hf_dt.timetuple()))

    except ValueError:
        return jsonify({"error": "Formato incorrecto. Fecha debe ser dd-mm-aaaa y horas deben ser enteros (0-23)"}), 400

    filtro = {"fecha_guardado": {"$gte": ts_inicio, "$lte": ts_fin}}

    cursor = coleccion.find(filtro, {'_id': 0})
    entradas = list(cursor)

    return jsonify({
        "periodico": periodico,
        "fecha": fecha_str,
        "hora_inicio": hi,
        "hora_fin": hf,
        "total_entradas": len(entradas),
        "entradas": entradas
    })

app.run(host='0.0.0.0', port=5000)

