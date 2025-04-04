from flask import Flask, render_template, request, redirect, url_for, session
import qrcode
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = "supersecretkey"

def get_db_connection():
    return mysql.connector.connect(
        host='idor-db',
        user='root',
        password='root',
        database='eventos'
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['username']
            return redirect(url_for('index'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eventos")
    eventos = cursor.fetchall()
    conn.close()
    return render_template('index.html', eventos=eventos)

@app.route('/comprar', methods=['POST'])
def comprar():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    evento_id = request.form['evento_id']
    cantidad = int(request.form['cantidad'])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO facturas (user_id, evento_id, cantidad) VALUES (%s, %s, %s)", (user_id, evento_id, cantidad))
    factura_id = cursor.lastrowid
    
    for _ in range(cantidad):
        cursor.execute("INSERT INTO tickets (factura_id, evento_id) VALUES (%s, %s)", (factura_id, evento_id))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('factura', factura_id=factura_id))

@app.route('/factura/<int:factura_id>')
def factura(factura_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT f.id, f.cantidad, e.nombre AS evento FROM facturas f JOIN eventos e ON f.evento_id = e.id WHERE f.id = %s", (factura_id,))
    factura = cursor.fetchone()
    conn.close()
    
    if not factura:
        return "Factura no encontrada", 404
    
    url = f"http://127.0.0.1:5012/ver_factura/{factura_id}"
    
    qr = qrcode.make(url)
    qr_path = f"static/qrs/factura_{factura_id}.png"
    qr.save(qr_path)
    
    return render_template('factura.html', factura=factura, qr_path=qr_path)

@app.route('/ver_factura/<int:factura_id>')
def ver_factura(factura_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT f.id, f.cantidad, e.nombre AS evento, u.username AS usuario
        FROM facturas f
        JOIN eventos e ON f.evento_id = e.id
        JOIN users u ON f.user_id = u.id
        WHERE f.id = %s
    """, (factura_id,))
    factura = cursor.fetchone()
    
    cursor.execute("SELECT * FROM tickets WHERE factura_id = %s", (factura_id,))
    tickets = cursor.fetchall()
    
    conn.close()
    
    if not factura:
        return "Factura no encontrada", 404
    
    return render_template('ver_factura.html', factura=factura, tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
