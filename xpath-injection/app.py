from flask import Flask, request, render_template, redirect, url_for
from lxml import etree

app = Flask(__name__)

def load_users():
    return etree.parse("users.xml")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        tree = load_users()
        root = tree.getroot()
        
        query = f".//user[username='{username}' and password='{password}']"
        user = root.xpath(query)

        if user:
            name = user[0].findtext("name")
            email = user[0].findtext("email")
            username = user[0].findtext("username")
            admin = user[0].findtext("admin") == "true"  # Verifica si es administrador

            return redirect(url_for("panel", username=username, name=name, email=email, admin=admin))
        return render_template("login.html", error="Invalid credentials")
    
    return render_template("login.html")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        identifier = request.form.get("username", "")
        tree = load_users()
        root = tree.getroot()

        user_query = f".//user[username='{identifier}']"
        user = root.xpath(user_query)

        if user:
            return render_template("forgot_password.html", message="Te hemos enviado un correo con instrucciones")
        return render_template("forgot_password.html", error="Usuario no encontrado")

    return render_template("forgot_password.html")

@app.route("/panel")
def panel():
    username = request.args.get("username")
    name = request.args.get("name")
    email = request.args.get("email")
    admin = request.args.get("admin") == "True"
    return render_template("panel.html", username=username, name=name, email=email, admin=admin)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
