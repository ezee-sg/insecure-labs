import pickle
import base64
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

class Reserva:
    def __init__(self, nombre, fecha, hora, personas):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.personas = personas

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reserva")
def index():
    datos_cookie = request.cookies.get("reserva")
    if datos_cookie:
        try:
            datos = base64.b64decode(datos_cookie)
            reserva = pickle.loads(datos)
            return render_template("reserva.html", reserva=reserva)
        except:
            return render_template("reserva.html", error="Error al cargar la reserva")
    return render_template("reserva.html", reserva=None)

@app.route("/reservar", methods=["POST"])
def reservar():
    nombre = request.form.get("nombre")
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")
    personas = request.form.get("personas")
    
    reserva = Reserva(nombre, fecha, hora, personas)
    
    datos = pickle.dumps(reserva)
    datos_b64 = base64.b64encode(datos).decode()

    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("reserva", datos_b64)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
