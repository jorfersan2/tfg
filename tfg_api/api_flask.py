from flask import Flask, jsonify, request
from pymongo import MongoClient

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

    try:
        limite = int(request.args.get('limite', 20))
        pagina = int(request.args.get('pagina', 1))
    except ValueError:
        return jsonify({"error": "Parámetros 'limite' y 'pagina' deben ser enteros"}), 400

    skip = (pagina - 1) * limite

    filtro_fecha = {}
    try:
        fecha_desde = request.args.get('fecha_desde')
        fecha_hasta = request.args.get('fecha_hasta')
        if fecha_desde:
            filtro_fecha['$gte'] = int(fecha_desde)
        if fecha_hasta:
            filtro_fecha['$lte'] = int(fecha_hasta)
    except ValueError:
        return jsonify({"error": "Parámetros 'fecha_desde' y 'fecha_hasta' deben ser enteros (timestamp)"}), 400

    filtro = {}
    if filtro_fecha:
        filtro['fecha_guardado'] = filtro_fecha

    cursor = coleccion.find(filtro, {'_id': 0}).skip(skip).limit(limite)
    entradas = list(cursor)

    return jsonify({
        "periodico": periodico,
        "pagina": pagina,
        "limite": limite,
        "filtro_fecha": filtro_fecha if filtro_fecha else None,
        "entradas": entradas
    })

# Ejecutar el servidor Flask directamente con 'flask run' o desde otro script
app.run(host='0.0.0.0', port=5000)
