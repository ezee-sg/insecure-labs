from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "username": "j.perez", "password": "1234"},
    {"id": 2, "username": "a.garcia", "password": "abcd"},
    {"id": 3, "username": "c.lopez", "password": "password123"},
    {"id": 4, "username": "l.martinez", "password": "qwerty"}
]

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "endpoints": [
            {"url": "/api/users", "method": "GET", "description": "Devuelve la lista de usuarios con id, username y password"},
            {"url": "/api/users/{id}", "method": "GET", "description": "Devuelve un usuario específico por id"}
        ]
    })

@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify({"users": USERS})

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((user for user in USERS if user["id"] == id), None)
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
