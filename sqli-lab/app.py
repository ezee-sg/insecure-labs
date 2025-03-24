from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='sqli-db',
        user='root',
        password='root',
        database='tienda'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos')
    productos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', productos=productos)

@app.route('/buscar')
def buscar():
    name = request.args.get('nombre')
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT id, nombre, precio FROM productos WHERE nombre LIKE '%" + name + "%'"
    cursor.execute(query)

    productos = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify({'productos': productos})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

