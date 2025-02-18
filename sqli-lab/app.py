from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='sqli-db',
        user='root',
        password='root',
        database='shop'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, price FROM products')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', products=products)

@app.route('/search')
def buscar():
    name = request.args.get('name')
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT id, name, price FROM products WHERE name LIKE '%" + name + "%'"
    cursor.execute(query)

    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify({'products': products})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

