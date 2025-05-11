from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos ficticia de partidos con aforo
MATCHES = {
    "1": {"name": "Real Madrid vs Barcelona", "capacity": 81044},
    "2": {"name": "Atlético Madrid vs Sevilla", "capacity": 68000},
    "3": {"name": "Valencia vs Real Sociedad", "capacity": 55000},
    "4": {"name": "Athletic Club vs Villarreal", "capacity": 53000},
    "5": {"name": "Real Betis vs Getafe", "capacity": 60000},
}

# Base de datos ficticia de stock de entradas
STOCK = {
    "1": 23,
    "2": 123,
    "3": 67,
    "4": 78,
    "5": 443,
}

@app.route('/api', methods=['GET'])
def api_info():
    return jsonify({
        "routes": {
            "/api/matches": "Lista todos los partidos y su aforo",
            "/api/stock?matchId=<id>&quantity=<cantidad>": "Consulta si hay suficientes entradas disponibles para un partido",
        }
    })


@app.route('/api/matches', methods=['GET'])
def list_matches():
    return jsonify({"matches": MATCHES})

@app.route("/api/stock", methods=["GET"])
def check_stock():
    match_id = request.args.get("matchId")
    quantity = request.args.get("quantity", type=int)

    if not match_id or quantity is None:
        return jsonify({"error": "Faltan parámetros en la solicitud"}), 400

    if match_id in STOCK and STOCK[match_id] >= quantity:
        return jsonify({"entradas disponibles": STOCK[match_id]})
    
    return jsonify({"error": "No hay suficientes entradas disponibles"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
