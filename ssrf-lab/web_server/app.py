from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/check_matches", methods=["GET"])
def check_matches():
    api_url = request.args.get("api_url")
    
    if not api_url:
        return render_template("check_matches.html", error="No se proporcionó la URL de la API de partidos")
    
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            matches = response.json().get("matches", {})
            return render_template("check_matches.html", matches=matches)
        else:
            return render_template("check_matches.html", error="No se pudo obtener la lista de partidos")
    except requests.exceptions.RequestException as e:
        return render_template("check_matches.html", error=f"Error al consultar la API de partidos: {e}")

@app.route("/check_stock", methods=["GET"])
def check_stock():
    match_id = request.args.get('match_id')
    quantity = request.args.get('quantity', type=int)
    api_url = request.args.get('api_url')

    if match_id and quantity:
        try:
            response = requests.get(api_url, params={'matchId': match_id, 'quantity': quantity})
            
            if response.status_code == 200:
                stock = response.json()
                return render_template("check_stock.html", stock=stock)
            else:
                return render_template("check_stock.html", error="No hay suficientes entradas disponibles")

        except requests.exceptions.RequestException as e:
            return render_template("check_stock.html", error=f"Error al consultar la API de stock: {e}")

    return render_template("check_stock.html", error="Faltan parámetros en la solicitud")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
